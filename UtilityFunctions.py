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



def readfile(file_name):
    log_func("readfile")
    file = open(file_name)
    data = file.read()
    file.close()
    return data

def writefile(file_name,content):
    with open(file_name,'a') as fp:
        fp.write("".join(content))
    
    