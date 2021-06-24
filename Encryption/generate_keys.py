"""Generate keys"""
import sympy
PRIME_1 = sympy.randprime(500, 1000)
PRIME_2 = sympy.randprime(1000, 1500)
PUBLIC_KEY = [sympy.randprime(0, (PRIME_1)*(PRIME_2)), (PRIME_1)*(PRIME_2)]
PRIVATE_KEY = [
    0,
    (PRIME_1)*(PRIME_2)]
i = 0
while True:
    if (i*PUBLIC_KEY[0]) % ((PRIME_1-1)*(PRIME_2-1)) == 1:
        PRIVATE_KEY[0] = i
        break
    i += 1
key_file = open(
    '/Users/home/varun/Projects/Encryption/keys.txt',
    'w'
)
key_file.write(
    str(PUBLIC_KEY[0])
    + ' '
    + str(PUBLIC_KEY[1])
    + ' '
    + str(PRIVATE_KEY[0])
    + ' '
    + str(PRIVATE_KEY[1])
    )
