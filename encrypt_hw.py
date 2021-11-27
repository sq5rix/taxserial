"""
First succesful try
https://github.com/danni/python-pkcs11
"""

import os
import pkcs11
from secrets import PIN

os.environ['PKCS11_MODULE'] = '/opt/proCertumCardManager/sc30pkcs11-3.0.5.60-MS.so'

TOKEN = 'profil standardowy'

def encrypt_file(iv, data):
    # Initialise our PKCS#11 library
    lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
    token = lib.get_token(token_label=TOKEN)
    with token.open(user_pin=PIN) as session:
        # Generate an AES key in this session
        key = session.generate_key(pkcs11.KeyType.AES, 256)
        # Encrypt our data
        crypttext = key.encrypt(data, mechanism_param=iv)
        print('crypttext : ', crypttext )
        return crypttext


