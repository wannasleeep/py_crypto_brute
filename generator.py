import hashlib
import binascii
import os
class gnr():
    b = str()
    def KeyGenerator():
        entropy = str(os.urandom(16).hex()) #entropy generation
        data = entropy.strip()
        data = binascii.unhexlify(data)
        if len(data) not in [16, 20, 24, 28, 32, 64]:
           raise ValueError(
      'Data length should be one of the following: [16, 20, 24, 28, 32], but it is not (%d).' % len(data))
        h = hashlib.sha256(data).hexdigest()
        private_key = h #save private key

        gnr.b = bin(int(binascii.hexlify(data),16))[2:].        zfill(len(data)*8) + bin(int(h,16))[2:].zfill(256)[: len(data)* 8//32]
        return private_key

    def seed_generator():
        try:
            with open('Bip39.txt', 'r') as f:
                 wordlist = [w.strip() for w in f.readlines()]
        except:
            print ("please install Bip39 dictionary from https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt")
        seed = []
        zerno = []
        for i in range(len(gnr.b)//11):
            indx = int(gnr.b[11*i:11*(i+1)],2)
            zerno.append(indx)
            seed.append(wordlist[indx])
        seed = ' '.join(seed) #create mnemonic phrase
        return seed
