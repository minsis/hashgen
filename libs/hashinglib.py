import hashlib

def read_file(file_path, hashed_file):
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)
    return hashed_file.hexdigest()
    
def md5(file_path):
    hashed_file = hashlib.md5()
    return read_file(file_path, hashed_file)

def sha1(file_path):
    hashed_file = hashlib.sha1()
    return read_file(file_path, hashed_file)

def sha224(file_path):
    hashed_file = hashlib.sha224()
    return read_file(file_path, hashed_file)

def sha256(file_path):
    hashed_file = hashlib.sha256()
    return read_file(file_path, hashed_file)

def sha384(file_path):
    hashed_file = hashlib.sha384()
    return read_file(file_path, hashed_file)

def sha512(file_path):
    hashed_file = hashlib.sha512()
    return read_file(file_path, hashed_file)

def run_hash(file_path, algo_hash):
    hashed_file = hashlib.new("algo_hash")
    return read_file(file_path, hashed_file)

def convert_to_dict(hash_list):
    hash_dict = dict()
    for hash_type in hash_list:
        hash_dict[hash_type] = globals()[hash_type]
    return hash_dict

def compare(compare_hash, hash_value):
    if compare_hash == hash_value:
        print("Your hash values match")
    else:
        print("Your hash values do not match")

def get_hashes():
    builtin_hash = list(hashlib.algorithms_guaranteed)
    avial_hash = list(hashlib.algorithms_available)
    for item in openssl_hash:
        if item.upper() in openssl_hash:
            avial_hash.remove(item.upper)
    avial_hash.sort()
