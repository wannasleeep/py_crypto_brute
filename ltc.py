import hashlib
import base58
import codecs
compress_pubkey = True

def hash160(hex_str):
	sha = hashlib.sha256()
	rip = hashlib.new('ripemd160')
	sha.update(hex_str)
	rip.update( sha.digest() )
	return rip.hexdigest()  # .hexdigest() is hex ASCII

def to_wallet(pubkey):
        key_hash = '30' + hash160(codecs.encode(pubkey))
        # Obtain signature:
        sha = hashlib.sha256()
        sha.update( bytearray.fromhex(key_hash) )
        checksum = sha.digest()
        sha = hashlib.sha256()
        sha.update(checksum)
        checksum = sha.hexdigest()[0:8]
        wallet=(base58.b58encode( bytes(bytearray.fromhex(key_hash + checksum)) )).decode('utf-8')
        return wallet
