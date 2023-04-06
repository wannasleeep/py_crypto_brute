import hashlib
import base58
import codecs

def hash160(hex_str):
	sha = hashlib.sha256()
	rip = hashlib.new('ripemd160')
	sha.update(hex_str)
	rip.update( sha.digest() )
	return rip.hexdigest()  # .hexdigest() is hex ASCII


def dogeaddress(pubkey):
    key_hash = '1e' + hash160(codecs.encode(pubkey))
    # Obtain signature:
    sha = hashlib.sha256()
    sha.update( bytearray.fromhex(key_hash) )
    checksum = sha.digest()
    sha = hashlib.sha256()
    sha.update(checksum)
    checksum = sha.hexdigest()[0:8]
    return base58.b58encode( bytes(bytearray.fromhex(key_hash + checksum)) ).decode('utf-8')
