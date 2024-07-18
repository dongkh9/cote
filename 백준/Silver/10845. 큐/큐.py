import sys
n = int(sys.stdin.readline())
queue = []
for _ in range(n) :
    order = sys.stdin.readline().rstrip()

    if order == 'pop' :
        if queue :
            print(queue.pop(0))
        else :
            print(-1)
    elif order == 'size' :
        print(len(queue))
    elif order == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
    elif order == 'front' :
        if queue :
            print(queue[0])
        else : 
            print(-1)
    elif order == 'back' :
        if queue :
            print(queue[-1])
        else :
            print(-1)
    else :
        queue.append(int(order.split()[-1]))