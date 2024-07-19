import sys
n = int(sys.stdin.readline())
size_list = list(map(int,sys.stdin.readline().rstrip().split()))
t_p = list(map(int,sys.stdin.readline().rstrip().split()))
t = t_p[0]
p = t_p[1]

t_sum = 0

for size in size_list :
    t_batch = size // t
    if size % t != 0 :
        t_batch += 1
    t_sum += t_batch

p_batch = n // p
p_solo = n % p

print(t_sum)
print(f'{p_batch} {p_solo}')
