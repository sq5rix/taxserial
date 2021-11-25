"""
First succesful try
https://github.com/danni/python-pkcs11
"""

import os
import pkcs11
from secrets import PIN

os.environ['PKCS11_MODULE'] = '/opt/proCertumCardManager/sc30pkcs11-3.0.5.60-MS.so'

TOKEN = 'profil standardowy'

def encrypt_file(data):
    # Initialise our PKCS#11 library
    lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
    token = lib.get_token(token_label=TOKEN)

    #data = b'INPUT DATA'

    # Open a session on our token
    with token.open(user_pin=PIN) as session:
        # Generate an AES key in this session
        key = session.generate_key(pkcs11.KeyType.AES, 256)
        print('key : ', key )

        # Get an initialisation vector
        iv = session.generate_random(128)  # AES blocks are fixed at 128 bits
        # Encrypt our data
        crypttext = key.encrypt(data, mechanism_param=iv)
        print('crypttext : ', crypttext )
        return crypttext


