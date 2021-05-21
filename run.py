from UtilityFunctions import *
import argparse
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

