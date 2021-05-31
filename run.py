from UtilityFunctions import *
import argparse

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

def main():
    run_cesar()


if __name__ == '__main__':
    main()
