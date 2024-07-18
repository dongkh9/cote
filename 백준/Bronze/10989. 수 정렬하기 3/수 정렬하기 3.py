import sys
n = int(sys.stdin.readline())
num_set = set()
num_dict = {}
for _ in range(n) :
    num = int(sys.stdin.readline())
    num_set.add(num)
    if num not in num_dict :
        num_dict[num] = 1
    else :
        num_dict[num] += 1
num_list = list(num_set)
num_list.sort()

for nums in num_list :
    for _ in range(num_dict[nums]) :
        print(nums)
