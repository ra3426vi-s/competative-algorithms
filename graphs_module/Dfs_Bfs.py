class Graph:
    def __init__(self,vertex):
        if vertex is None:
            vertex=[];
        self.vertex=vertex;
    def displayVertices(self,vertex):
        return list(vertex.keys())
    def BFS(self,Node,graph):
        queue=[]
        visited=[]
        visited.append(Node)
        queue.append(Node)
        while queue:
            s=queue.pop(0)
            for element in graph[s]:
               if element not in visited:
                   visited.append(element)
                   queue.append(element)


        return visited
    def DFS(self,Node,graph):
        visited=[]
        currentnode=[]
        leftnode=[]
        currentnode.append(Node)
        while currentnode:
            s=currentnode.pop(0)
           # print(s)
            visited.append(s)
            for element in graph[s]:
                if element not in visited:
                    leftnode.append(element)

            #print(leftnode)
            if len(currentnode)==0 and len(leftnode)!=0:
                currentnode.append(leftnode.pop())
        return visited


graph_elements={
    'A': ['C', 'B'],
    'B': ['E', 'D'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []

}


y = Graph(graph_elements)
print(y.displayVertices(graph_elements))
print(y.BFS('A',graph_elements))
print(y.DFS('A',graph_elements))




# class Dog:
#
#     kind = 'canine'         # class variable shared by all instances
#
#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance
#
# d = Dog('Fido')
# e = Dog('Buddy')
# print( d.kind  )