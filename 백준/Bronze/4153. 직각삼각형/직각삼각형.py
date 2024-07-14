import sys
while True :
    temp = list(map(int,sys.stdin.readline().split()))
    if temp[0] == 0 :
        break
    if max(temp) > sum(temp) - max(temp) :
        print('wrong')
    elif max(temp)**2 != temp[0]**2 + temp[1]**2 + temp[2]**2 - max(temp)**2 :
        print('wrong')
    else :
        print('right')