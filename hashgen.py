import os
import time
from libs.hashinglib import *

avial_hash = ["sha384", "sha224", "md5", "sha512", "sha1", "sha256"]
avial_hash.sort()
dict_hash = dict()
default_hash = "md5"

print("List of available hash algorithms")
for k, v in enumerate(avial_hash, start=1):
    print("({}) {}".format(k,v))

while use_hash not in avial_hash:
    use_hash = input("Select an algorithm to use: [%s]") %(default_hash)
    if use_hash == "": use_hash = default_hash; break

while os.path.isfile(file_path) is False:
    file_path = input("Enter a valid file path (type exit to quit): ")
    if file_path == "exit": print("Exiting"); exit()

avial_hash = convert_to_dict(avial_hash)

start_time = time.time()
hash_value = avial_hash[use_hash](file_path)
print("Your {} hash value is: {}".format(use_hash,hash_value)
print("Execution Time: %s seconds" %(time.time() - start_time))
