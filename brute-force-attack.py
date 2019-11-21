import time
from itertools import product

target = 'pass'
chars = 'abcdefghijklmnopqrstuvwxyz'

def pass_crack(chars, repeat):
    pws = product(chars, repeat = repeat)
    for pw in pws:
        if ''.join(pw) == target:
            return ''.join(pw)

start = time.time()
password = pass_crack(chars, 4)

if (password is None):
    print('failure')

else:
    print('got it!!!! password is ', password)

finish = time.time() -start
print(finish, ' sec')
