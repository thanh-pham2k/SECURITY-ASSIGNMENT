import argparse

def log_func(func_name):
    print("-------------------")
    print(func_name)

# Make sure the alphabet is an made of unique letters
def validalpha(alphabet):
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
        
# Plaintext must have specific form which we can check for.
def validptext(T,alpha):
    log_func("validptext")
    if type(T) != str:
        raise Exception("Plaintext must be a string")
    
    for i in T:
        if i not in alpha:
            raise Exception("{} is not a valid plaintext character".format(i))


# Keys must also have specific form which we can check for.
def validkeys(K,types):
    
    if type(types) != list:
        if type(K) != types:
            raise Exception("Key must be {}".format(types))
    
    
    else:
        for pos,pair in enumerate(zip(K,types),1):

            if type(pair[0]) != pair[1]:
                raise Exception("Key #{} must be {}".format(pos,pair[1]))

# Convert letters to numbers according to some alphabet
def alphaToNumber(L,alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return [alpha.index(i) for i in L]


# Convert numbers to letters according to some alphabet
def numberToAlpha(L,alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return [alpha[i] for i in L]


def caesar(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
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
    

    
    if decode == True:
        key = M-key
        
    out = []
    for i in T:
        # Shift the number by the key value
        out.append( (i + key) % M )
    
    return "".join(numberToAlpha(out,alphabet))


def readfile(file_name):
    log_func("readfile")
    file = open(file_name)
    data = file.read()
    file.close()
    return data

def main():
    # we check with 3 testcases
    # short length
    # medium length
    # long length
    log_func("caesarExample")
    parser = argparse.ArgumentParser(
        description='python run.py testcase.txt 17 --decode=True',
        )
    parser.add_argument("file_raw_text", type=str, help="file_name")
    parser.add_argument("key_number", type=int, help="key_number")
    parser.add_argument("--decode", type=str, help="True - False",default=False)
    args = parser.parse_args()
    print("-------------------")
    print(args.decode)
    decode = False
    if args.decode=="True":
        decode = True
    print("Caesar Cipher Example\n")
    key = 17
    print("The Key Is: {}\n".format(key))
    print("\nStandard Mode")
    ptext = readfile(str(args.file_raw_text))
    ctext = caesar(ptext,key)
    dtext = caesar(ctext,key,decode)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    if decode==True:
        print("Decodes As:\n{}".format(dtext))

if __name__ == '__main__':
    main()

