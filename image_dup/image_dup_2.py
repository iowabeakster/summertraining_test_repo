import sys
import os
import hashlib

# function to read file one mb at a time
def file_reader(file_name, size=1024):
    """function that reads file_name in 1 MB pieces"""
    while True:
        file_piece = file_name.read(size)
        if not file_piece:
            return
        yield file_piece

# iterate through the given paths for all files, adding files
# and their hashes to the dictionary "hashes" after comparing 
# each new pair to the pairs already in dictionary

def check_for_duplicates(paths, hash=hashlib.sha1):
# create empty ditionary called "hashes"
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
# identify each file using whole pathname
                full_path = os.path.join(dirpath, filename)
                hash_return = hash()
# use file_reader function to break file into file_pieces and read pieces
                for file_piece in file_reader(open(full_path, 'rb')):
# run the hash function on each piece
                    hash_return.update(file_piece)                   
# compare the hash digest and pathname to items is dictionary hashes
                file_id = (hash_return.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
# if a duplicate hash is found, print the pair
# otherwise just add it as another pair to the dictionary
                if duplicate:
                    print "Duplicate found: %s and %s" % (full_path, duplicate)

                else:
                    hashes[file_id] = full_path

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print "Please pass the paths to check as parameters to the script"
