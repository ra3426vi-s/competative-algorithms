def DistanceCount(graph_elements,Source,Destination):
 infinity = float('inf')
 distance={}
 count=0
 visited=[]
 queue=[]
 queue.append(Source)
 for elements in graph_elements:
  distance[elements]=infinity
  if(elements==Source):
   distance[elements]=count
 while queue:
  s=queue.pop(0)
  if(len(graph_elements[s])>0):
   count=distance[s]+1
  for element in graph_elements[s]:
   if element not in visited:
    visited.append(element)
    queue.append(element)
    if(distance[element] > count):
     distance[element]=count




 return distance






graph_elements={
 'C': ['A', 'F', 'Z'],
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