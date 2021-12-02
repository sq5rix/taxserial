import os
import PyKCS11

# Initialise our PKCS#11 library
print(PyKCS11.CKF_DIGEST)


#os.environ['PYKCS11LIB'] = '/opt/proCertumCardManager/sc30pkcs11-3.0.5.60-MS.so'
#os.environ['PYKCS11LIB'] = '/opt/SimplySignDesktop/libcrypto.so.10'
#os.environ['PYKCS11LIB'] = '/opt/SSD-2.9.6-dist/libcrypto.so'
#os.environ['PYKCS11LIB'] = '/opt/SSD-2.9.6-dist/libcrypto.so.1.0.0'

#os.environ['PYKCS11LIB'] = '/usr/lib/pkcs11/opensc-pkcs11.so'
os.environ['PYKCS11LIB'] = '/opt/SS-8.2.1.1-dist/libcrypto3PKCS.so'

pkcs11 = PyKCS11.PyKCS11Lib()
pkcs11.load()  # define environment variable PYKCS11LIB=YourPKCS11Lib

slots = pkcs11.getSlotList()
print('slots : ', slots )

slot = slots[0]

session = pkcs11.openSession(slot, PyKCS11.CKF_RW_SESSION)
print('session : ', session )


