import sys

def bacon_BFS(me,friend_list):
    visit = []
    queue = [[me,0]]
    bacon_num = 0
    while queue:
        now_person = queue.pop(0)
        if now_person[0] not in visit:
            visit.append(now_person[0])
            bacon_num += now_person[1]

            for friend in friend_list[now_person[0]]:
                if friend not in visit :
                    queue.append([friend,now_person[1]+1])
    return bacon_num        


first_line = list(map(int,sys.stdin.readline().rstrip().split(' ')))

n = first_line[0]
m = first_line[1]
friend_list = [set() for _ in range(n+1)]
for _ in range(m) :
    me,you = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    friend_list[me].add(you)
    friend_list[you].add(me)

answer_list =[]
for i in range(n) :
    answer_list.append(bacon_BFS(i+1,friend_list))
print(answer_list.index(min(answer_list))+1)