# SECURITY-ASSIGNMENT
Implement and attack simple crypto algorithm such as: Caesar, Rail fence permutation and combine between them.

# Caesar algorithm
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

Usage:
You can use:

```
  python run.py -h
```

For more details. And there are examples command line below:

----------------------------------------------------------------
```
python run.py caesar ptext_0.txt 15

python run.py caesar ptext_0.txt 15 --decode=True
```


# Example

In file ptext_0.txt we have the content:

```
TODAYISMONDAY
```


After running CMD

```
python run.py caesar ptext_0.txt 15 --decode=True
```

We get the result in result_ptext_0.txt

```
11
TODAYISMONDAY
```

`First line`: key number

`Second line`: The content is decoded.

# RailFence algorithm

```
run.py railFence encode <Key> <File name>
```
We get the result in ciphertext.txt

```
run.py railFence decode <Key> <File name>
```
We get the result in plaintext.txt

```
run.py railFence attack <File name>
```
We get the result in plaintext.txt

# Product cipher algorithm

```
run.py caesar_railFence key1 key2 <File name>
```

We get the result in ciphertext.txt