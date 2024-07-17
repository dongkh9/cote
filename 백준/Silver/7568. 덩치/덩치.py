import sys
# 이차원 리스트로 만들고 각각 비교 후 리스트에 저장 [0번보다큰수,1번보다큰수,,,,]
n = int(sys.stdin.readline())
kgcm_list = []
for _ in range(n) :
    nth_person = list(map(int,sys.stdin.readline().split()))
    kgcm_list.append(nth_person)

nth_list = [1 for _ in range(n)]

for i in range(len(kgcm_list)) :
    me = kgcm_list[i]
    for j in range(len(kgcm_list)) :
        if me[0] < kgcm_list[j][0] and me[1] < kgcm_list[j][1] :
            nth_list[i] += 1

for i in range(len(nth_list)) :
    print(nth_list[i],end=' ')

