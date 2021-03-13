# path to the file containing filenames with original hash
hash_files=open('hashed_files.txt', 'r')
# path to the file containing filenames to check with original hash
check_files=open('check_hashes.txt', 'r')

# get file names in list with original hash
hash_list=[]
for line in hash_files:
    hash_list.append(line.rstrip())

# get file names with hash in list, to check with original file hash
check_list=[]
for line in check_files:
    check_list.append(line.rstrip())

# below list to compare if file exist but hash broken from original
without_hash_list=[]
for name in check_list:
    without_hash_list.append(name.split(' ',1)[0])

# print(hash_list)
# print(check_list)
# print(without_hash_list)

result_list=[]
for item in hash_list:
    if item not in check_list:
        result=item.split(" ",1)[0]
        if result not in without_hash_list:
            result_list.append(result+" NOT FOUND")
        else:
            result_list.append(result+" FAIL")
    else:
        result_list.append(item.split(" ",1)[0]+" OK")

for file in result_list:
    print(file)





