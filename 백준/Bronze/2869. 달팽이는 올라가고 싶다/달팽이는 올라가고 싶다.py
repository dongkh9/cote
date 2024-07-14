import sys
import math
input_nums = list(map(int,sys.stdin.readline().split()))
can_climb = input_nums[0]
down = input_nums[1]
height = input_nums[2]

climb_down = can_climb - down

day_count = math.ceil( ( height - can_climb ) / climb_down ) + 1
print(day_count)