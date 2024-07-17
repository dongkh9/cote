import sys
n = int(sys.stdin.readline())
member_list = [[] for i in range(200)]
for _ in range(n) :
    age_name = sys.stdin.readline().rstrip().split()
    age = int(age_name[0])
    name = age_name[1]
    member_list[age-1].append(name)

for i in range(len(member_list)) :
    for j in range(len(member_list[i])) :
        print(str(i+1) + ' ' + member_list[i][j])
