import sys
import math

def rounding(num) :
    return math.floor(num+0.5)

n = int(input())
if n == 0 :
    print(0)
else :
    level_list = []
    for _ in range(n) :
        level = int(sys.stdin.readline())
        level_list.append(level)
        
    level_list.sort()

    fifteen = rounding(len(level_list) * 0.15)
    level_list = level_list[fifteen:len(level_list)-fifteen]
    print(rounding(sum(level_list)/len(level_list)))