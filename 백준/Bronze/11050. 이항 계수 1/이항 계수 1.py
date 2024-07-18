n_k = input().rstrip().split()
n = int(n_k[0])
k = int(n_k[1])
if k == 0 :
    print(1)
else:
    answer = 1
    for i in range(k) :
        answer *= n-i
        answer /= (i+1)
    print(int(answer))
