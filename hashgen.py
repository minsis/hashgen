import os
import time
from libs.hashinglib import *

avial_hash = get_hashes()
dict_hash = dict()
default_hash = "md5"
use_hash = str()
file_path = str()

print("List of available hash algorithms")
for k, v in enumerate(avial_hash, start=1):
    print("({}) {}".format(k,v))

#avial_hash = format_hash(avial_hash)

while use_hash not in avial_hash:
    use_hash = input("Select an algorithm to use [{}]: ".format(default_hash))
    if use_hash == "": use_hash = default_hash; break

while os.path.isfile(file_path) is False:
    file_path = input("Enter a valid file path (type exit to quit): ")
    if file_path == "exit": print("Exiting"); exit()

compare_hash = input("Hash value to compare (enter to skip): ")

start_time = time.time()
hash_value = run_hash(file_path, use_hash)
stop_time = time.time() - start_time

print("Your {} hash value is: {}".format(use_hash,hash_value))
print("Execution Time: {} seconds".format(stop_time))
if compare_hash != "": compare(compare_hash, hash_value)
