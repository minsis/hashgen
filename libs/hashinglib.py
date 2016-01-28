import hashlib

def md5hash(file_path):
    hashed_file = hashlib.md5()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    md5_hash = hashed_file.hexdigest()
    print("md5 hash: " + md5_hash)
    return md5_hash

def sha1hash(file_path):
    hashed_file = hashlib.sha1()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha1_hash = hashed_file.hexdigest()
    print("sha1 hash: " + sha1_hash)
    return sha1_hash

def sha224hash(file_path):
    hashed_file = hashlib.sha224()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha224_hash = hashed_file.hexdigest()
    print("sha224 hash: " + sha224_hash)
    return sha224_hash

def sha256hash(file_path):
    hashed_file = hashlib.sha256()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha256_hash = hashed_file.hexdigest()
    print("sha256 hash: " + sha256_hash)
    return sha256_hash

def sha384hash(file_path):
    hashed_file = hashlib.sha384()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha384_hash = hashed_file.hexdigest()
    print("sha384 hash: " + sha384_hash)
    return sha384_hash

def sha512hash(file_path):
    hashed_file = hashlib.sha512()
    with open(file_path, "rb") as open_file:
        read_byte = open_file.read(1048576)

        while read_byte:
            hashed_file.update(read_byte)
            read_byte = open_file.read(1048576)

    sha512_hash = hashed_file.hexdigest()
    print("sha512 hash: " + sha512_hash)
    return sha512_hash

def compare(hash):
