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

def DFS(graph,s):#导入graph图和s初识位置
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack)>0:
        vertax = stack.pop()#从这个队列中拿一个点出来
        nodes = graph[vertax]#这个点旁边所有的点
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertax)

DFS(graph,'A')