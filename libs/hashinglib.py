import hashlib

def md5(file_path):
    hashed_file = hashlib.md5()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    md5_hash = hashed_file.hexdigest()
    return md5_hash

def sha1(file_path):
    hashed_file = hashlib.sha1()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha1_hash = hashed_file.hexdigest()
    return sha1_hash

def sha224(file_path):
    hashed_file = hashlib.sha224()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha224_hash = hashed_file.hexdigest()
    return sha224_hash

def sha256(file_path):
    hashed_file = hashlib.sha256()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha256_hash = hashed_file.hexdigest()
    return sha256_hash

def sha384(file_path):
    hashed_file = hashlib.sha384()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha384_hash = hashed_file.hexdigest()
    return sha384_hash

def sha512(file_path):
    hashed_file = hashlib.sha512()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha512_hash = hashed_file.hexdigest()
    return sha512_hash

def convert_to_dict(hash_list):
    hash_dict = dict()
    for hash_type in hash_list:
        hash_dict[hash_type] = hash_type
    return hash_dict


#def compare(hash):
