def hash_val(index, string, r = 31) :
    return (ord(string) - 96) * r**i

M = 1234567891
L = int(input())
abc_list = list(input())
hash_sum = 0

for i,v in enumerate(abc_list) :
    hash_sum += hash_val(i,v)

print(hash_sum % M )