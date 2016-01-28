import os
import time
from libs.hashinglib import *

avial_hash = ["sha384", "sha224", "md5", "sha512", "sha1", "sha256"]
default_hash = "md5"

print("List of available hash algorithms")
for k, v in enumerate(avial_hash, start=1): print("(%s) %s") %(k,v)

while use_hash not in avial_hash:
    use_hash = input("Select an algorithm to use: [%s]") %(default_hash)
    if use_hash == "": use_hash = default_hash; break

file_path = input("Enter a valid file path: ")
while os.path.isfile(file_path) is False:
    file_path = input("Enter a valid file path: ")

start_time = time.time()
sha1hash(file_path)
print("Execution Time: %s seconds" %(time.time() - start_time))
