import sys
sup = 100000
inf = - 100000

n = int(sys.stdin.readline())
x_set = set()
y_list = [[] for _ in range(sup-inf+1)]
for _ in range(n) :
    point = list(map(int,sys.stdin.readline().strip().split()))
    x = point[1] + sup # 최소값을 0으로 설정
    y = point[0] + sup

    x_set.add(x)
    y_list[x].append(y)
x_list = list(x_set)
x_list.sort()

for sorted_x in x_list :
    y_list[sorted_x].sort()
    for i in range(len(y_list[sorted_x])) :
        print(y_list[sorted_x][i]-sup,end=' ')
        print(sorted_x-sup)
