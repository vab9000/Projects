"""Decrypts file"""
encrypted_file = open(
    '/Users/home/varun/Projects/Encryption/encrypted.txt',
    'r'
    )
encrypted_string = encrypted_file.read()
encrypted_list = encrypted_string.split(' ')
key_file = open(
    '/Users/home/varun/Projects/Encryption/keys.txt',
    'r'
)
key_string = key_file.read()
key_list = key_string.split(' ')
PRIVATE_KEY = [int(key_list[2]), int(key_list[3])]
decrypted_file = open(
    '/Users/home/varun/Projects/Encryption/decrypted.txt',
    'w'
    )
decrypted_list = list()
for char in encrypted_list:
    decrypted_list.append((int(char)**PRIVATE_KEY[0]) % PRIVATE_KEY[1])
DECRYPTED_STRING = str()
for char in decrypted_list:
    DECRYPTED_STRING = DECRYPTED_STRING + chr(int(char))
decrypted_file.write(DECRYPTED_STRING)
decrypted_file.close()
