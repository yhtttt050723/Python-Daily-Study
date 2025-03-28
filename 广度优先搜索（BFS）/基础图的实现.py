graph = {
    'A' : ['B','C'],
    'B' : ['A','C','D'],
    'C' : ['A','B','D','E'],
    'D' : ['B','C','E','F'],
    'E' : ['C','D'],
    'F' : ['D']
}
#字典的一些用法
print(graph.keys())
print(graph['A'])

def BFS(graph,s):#导入graph图和s初识位置
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    #通过映射找最小生成子树
    parent = {s:None}

    while len(queue)>0:
        vertax = queue.pop(0)#从这个队列中拿一个点出来
        nodes = graph[vertax]#这个点旁边所有的点
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertax
        print(vertax)
    return parent

parent = BFS(graph,'E')
print(parent)
flag = 'B'

while flag != None:
    print(flag)
