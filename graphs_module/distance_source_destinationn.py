def DistanceCount(graph_elements,Source,Destination):
 infinity = float('inf')
 distance={}
 count=0
 visited=[]
 queue=[]
 g_path=[]
 path_follower=[]
 previous_element=None

 queue.append(Source)
 for elements in graph_elements:
  distance[elements]=[]
  distance[elements].append(infinity)

  if(elements==Source):
   distance[elements][0]=count
   distance[elements].append([None])

 while queue:
  s=queue.pop(0)
  previous_element=s
  if(len(graph_elements[s])>0):
   count=distance[s][0]+1
  for element in graph_elements[s]:
   if element not in visited:
    visited.append(element)
    queue.append(element)
    if(distance[element][0] > count):
     distance[element][0]=count
     distance[element].append( [previous_element])
     # path=distance[previous_element][1][0]
     # if (path!=None):
     #  path_follower=distance[previous_element][2]
     #  path_follower.append(element)
     #  g_path.append(path_follower)
     #
     #  distance[element].append(g_path)
     #  print(g_path)
     #  g_path=[]
     #  path_follower=[]
     # if (path == None):
     #  g_path.append(previous_element)
     #  g_path.append(element)
     #  distance[element].append(g_path)
     # print(g_path)
     # g_path = []
     #







 return distance




# graph_elements={
#     'A': ['C', 'B'],
#     'B': ['E', 'D'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
#
# }

graph_elements={
 'C': ['A','F', 'Z'],
 'A': ['B', 'D'],
 'F': [],
 'Z': [],
 'B': ['D', 'E'],
 'D': ['F', 'G'],
 'G': ['F'],
 'E': []
}
print(DistanceCount(graph_elements,"C","D"))
print(len(graph_elements['A']))