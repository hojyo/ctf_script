import sys
import string

def _caesar(cipher, num):
    if 'A' <= cipher and cipher <= 'Z':
        return chr((ord(cipher) - ord('A') + int(num)) % 26 + ord('A'))

    if 'a' <= cipher and cipher <= 'z':
        return chr((ord(cipher) - ord('a') + int(num)) % 26 + ord('a'))
    
    return cipher

def caesar(s,b):
    g = (_caesar(cipher,b) for cipher in s)
    return ''.join(g)

def main():
    print('rot13 string input :')
    s = input()
    print('caesar number input :')
    b=input()
    for i in range(int(b)):
        print(str(i) + 'slide : ' + caesar(s,int(i)))
main()
