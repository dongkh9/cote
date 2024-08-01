import sys

def DFS(start,vertexes,unvisit,result):

    now_vertex = list(vertexes[start])
    now_vertex.sort()

    if start in unvisit:
        result.append(unvisit.pop(unvisit.index(start)))
    for node in now_vertex :
        if node in unvisit:
            result.append(unvisit.pop(unvisit.index(node)))  
            result = DFS(node,vertexes,unvisit,result)

    return result

def BFS(start,vertexes,unvisit,result=[]):
    queue = [start]
    now_vertex = list(vertexes[queue[0]])
    now_vertex.sort()

    while queue :
        if queue[0] in unvisit :
            result.append(unvisit.pop(unvisit.index(queue[0])))
            now_vertex = list(vertexes[queue[0]])
            now_vertex.sort()
            for node in now_vertex :
                if node in unvisit:
                    queue.append(node)
        queue.pop(0)

    return result
    
line = list(map(int,sys.stdin.readline().rstrip().split()))
n = line[0]
m = line[1]
v = line[2]

vertexes = [set() for _ in range(n+1)]

for _ in range(m) :
    vertex = list(map(int,sys.stdin.readline().rstrip().split()))
    vertexes[vertex[0]].add(vertex[1])
    vertexes[vertex[1]].add(vertex[0])
DFS_result = DFS(v,vertexes,list(range(1,n+1)),[])
for num in DFS_result :
    print(num,end=' ')

print()

BFS_result = BFS(v,vertexes,list(range(1,n+1)),[])
for num in BFS_result :
    print(num)