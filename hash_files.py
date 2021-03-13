import hashlib

files_1 = ['file_01.bin', 'file_02.bin', 'file_03.bin']
files_2 = ['file_04.txt']

# hashing files to md5 and writing result into hashed_files.txt
hasher = hashlib.md5()
for filename in files_1:
    with open(f'files/{filename}', 'rb') as open_file:
        content=open_file.read()
        hasher.update(content)
        md5_hash=hasher.hexdigest()
        with open('hashed_files.txt', 'a') as hashed_list:
            hashed_list.write(filename+" "+md5_hash+"\n")
            print(f"{filename} successfully hashed to md5")

# hashing files to sha1 and writing result into hashed_files.txt
hasher_1 = hashlib.sha1()
for filename in files_2:
    with open(f'files/{filename}', 'rb') as open_file:
        content=open_file.read()
        hasher_1.update(content)
        sha1_hash=hasher_1.hexdigest()
        with open('hashed_files.txt', 'a') as hashed_list:
            hashed_list.write(filename+" "+sha1_hash+"\n")
            print(f"{filename} successfully hashed to sha1")




