n_k = input().rstrip().split()
n = int(n_k[0])
k = int(n_k[1])

people_list = [i+1 for i in range(n)]
poped_list = []
now_position = 0

while people_list :
    round_of_circle = len(people_list) 
    now_position += k
    if now_position > round_of_circle :
        now_position %= round_of_circle
    if now_position == 0 :
        now_position =round_of_circle
    poped_list.append(people_list.pop(now_position-1))
    now_position -= 1
print('<',end='')
for i in range(len(poped_list)-1) :
    print(f'{poped_list[i]}, ',end='')
print(f'{poped_list[-1]}>')