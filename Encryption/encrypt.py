"""Encrypts file"""
key_file = open(
    '/Users/home/varun/Projects/Encryption/keys.txt',
    'r'
)
key_string = key_file.read()
key_list = key_string.split(' ')
PUBLIC_KEY = [int(key_list[0]), int(key_list[1])]
encrypted_file = open(
    '/Users/home/varun/Projects/Encryption/encrypted.txt',
    'w'
    )
file_text = open('/Users/home/varun/Projects/Encryption/file.txt', 'r')
file_string = file_text.read()
file_text.close()
encrypted_list = list()
for char in file_string:
    encrypted_list.append((ord(char)**PUBLIC_KEY[0]) % PUBLIC_KEY[1])
ENCRYPTED_STRING = str()
for char in encrypted_list:
    ENCRYPTED_STRING = ENCRYPTED_STRING + str(char) + ' '
ENCRYPTED_STRING = ENCRYPTED_STRING.rstrip()
encrypted_file.write(ENCRYPTED_STRING)
encrypted_file.close()
