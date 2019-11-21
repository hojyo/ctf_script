import string
import secrets

def pass_gen(size=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    chars += '%&$#()'

    return ''.join(secrets.choice(chars) for x in range(size))

pass_size = int(input())
print(pass_gen(pass_size))
