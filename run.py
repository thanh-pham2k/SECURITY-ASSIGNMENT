from UtilityFunctions import *
import argparse
import sys

def caesar(text,key,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    log_func("caesar")
    text = text.upper()
    validalpha(alphabet)
    validptext(text,alphabet)
    validkeys(key,int)
    
    M = len(alphabet)
    T = alphaToNumber(text,alphabet)
    
    # Allow key to be specified by letter
    if type(key) == str:
        if key in alphabet:
            key = alphabet.index(key)
    

    out = []
    for i in T:
        # Shift the number by the key value
        out.append( (i + key) % M )
    
    return "".join(numberToAlpha(out,alphabet))

#-----------------------------------ATTACK-----------------------------------
ngrams4 = open('4gramScores.csv', 'r')

quadgrams = {}


for line in ngrams4:
    L = line.split(" ")
    quadgrams[L[0]] = int(L[2])

def quadgramScore(text):
    score = 0
    for i in range(len(text)-1):
        if text[i:i+4] not in quadgrams.keys():
            score -= 3000
        else:
            score += quadgrams[text[i:i+4]]
    return score

def caesarCracker(ctext):

    bestkey = 0
    bestdecode = ""
    bestscore = float("-inf")
    for i in range(0,26):
        
        dtext = caesar(ctext,i)
        s = quadgramScore(dtext)
        if s > bestscore:
            bestkey = i
            bestscore = s
            bestdecode = dtext

    return bestkey,bestdecode


def run_cesar():
    # we check with 3 testcases
    # short length
    # medium length
    # long length
    parser = argparse.ArgumentParser()
    parser.add_argument('algo_name',type=str,help="algorithm's name")
    parser.add_argument('--argument',default=None,help=
                        '''
                        python run.py caesar ptext_1.txt 17 --decode=True
                        ''')
    parser.add_argument("file_raw_text", type=str, help="file_name")
    parser.add_argument("key_number", type=int, help="key_number")
    parser.add_argument("--decode", type=str, help="True - False",default=False)
    args = parser.parse_args()
    
    if parser.parse_args().algo_name == 'caesar':
        ptext = readfile(str(args.file_raw_text))      
        key = args.key_number
        ctext = caesar(ptext,key)
        file_name_dest = "result_" + args.file_raw_text
        if (args.decode=="True"):
            bestKey,bestDecode = caesarCracker(ctext) 
            writefile(file_name_dest ,str(bestKey))
            writefile(file_name_dest,"\n"+bestDecode)
        else:
            writefile(file_name_dest,ctext)

# Rail Fence =============================================================
# ========================================================================
def railfence(text, key, decode=False):
    if decode == False:
        # start on rail 0
        rail = 0
        # move along the rails
        inc = 1
        fence = ["" for i in range(key)]
        for pos, let in enumerate(text):
            fence[rail] += let
            # move to the next rail
            rail += inc
            # if we have reached rail 0 or rail key-1 reverse the direction
            # that we move on the rails
            if rail == 0 or rail == key-1:
                inc *= -1

        return "".join(fence)

    if decode == True:
        # To decode we rebuild the fence

        # First how many letters are on each rail?
        chunks = [0 for i in range(key)]
        rail = 0
        inc = 1
        for pos in text:
            chunks[rail] += 1
            rail += inc
            if rail == 0 or rail == key-1:
                inc *= -1

        # Now rebuild each rail
        fence = ["" for i in range(key)]
        ctr = 0
        for pos, num in enumerate(chunks):
            fence[pos] = text[ctr:ctr+num]
            ctr += num

        # Finally read up and down the rails
        rail = 0
        inc = 1
        out = []
        for pos, let in enumerate(text):
            a, fence[rail] = fence[rail][0], fence[rail][1:]
            out.append(a)
            rail += inc
            if rail == 0 or rail == key-1:
                inc *= -1

        return "".join(out)

def railsFenceCracker(ctext):
    l = len(ctext)
    bestkey = 0
    bestdecode = ""
    bestscore = float("-inf")
    for i in range(2, l):

        dtext = railfence(ctext, i, decode=True)
        s = quadgramScore(dtext)
        if s > bestscore:
            bestkey = i
            bestscore = s
            bestdecode = dtext

    return bestkey, bestdecode

def run_railFence():
    if sys.argv[2] == 'encode':
        if sys.argv[3] and sys.argv[3].isnumeric() and sys.argv[4]:
            fc = open(sys.argv[4], 'r')
            plaintext = fc.read()
            f = open('ciphertext.txt', 'w')
            f.write(railfence(plaintext, int(sys.argv[3])))
        else:
            print('run.py railFence encode <Key> <File name>')
    elif sys.argv[2] == 'decode':
        if sys.argv[3] and sys.argv[3].isnumeric() and sys.argv[4]:
            fc = open(sys.argv[4], 'r')
            ciphertext = fc.read()
            f = open('plaintext.txt', 'w')
            f.write(railfence(ciphertext, int(sys.argv[3]), decode=True))
        else:
            print('run.py railFence decode <Key> <File name>')
    elif sys.argv[2] == 'attack':
        if sys.argv[3]:
            fc = open(sys.argv[3], 'r')
            ciphertext = fc.read()
            print(ciphertext)
            key, plaintext = railsFenceCracker(ciphertext)
            fp = open('plaintext.txt', 'w')
            fp.write(plaintext)
        else:
            print('run.py railFence attack <File name>')
# Use both caesar_railFence
# ========================================================================
def caesar_railFence(text, key1, key2):
    temp = caesar(text, key1)
    return railfence(temp, key2)

def run_caesar_railFence():
    if sys.argv[1] == 'caesar_railFence' and sys.argv[2].isnumeric() and sys.argv[3].isnumeric() and sys.argv[4]:
            fc = open(sys.argv[4], 'r')
            plaintext = fc.read()
            ciphertext = caesar_railFence(plaintext, int(sys.argv[2]), int(sys.argv[3]))
            fp = open('ciphertext.txt', 'w')
            fp.write(ciphertext)
    else:
        print('run.py caesar_railFence key1 key2 <File name>')

def main():
    if sys.argv[1] == 'caesar':
        run_cesar()
    if sys.argv[1] == 'railFence':
        run_railFence()
    if sys.argv[1] == 'caesar_railFence':
        run_caesar_railFence()


if __name__ == '__main__':
    main()
