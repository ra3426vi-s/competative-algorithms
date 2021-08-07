def djk(graph_elements,distance,source,destination):
    print(source)
    print(destination)
    queue=[]
    visited=[]
    path=[]
    queue.append(source)
    path.append(destination)
    visited.append(source)
    if(source in distance):
        distance[source]['Dist']=0


    while queue:
        s=queue.pop(0)
        for neighbours in graph_elements[s]:
            if neighbours not in visited:
                queue.append(neighbours)
                visited.append(neighbours)
                distance[neighbours]['Dist']= min(distance[neighbours]['Dist'],(graph_elements[s][neighbours]+distance[s]['Dist']))
                distance[neighbours]['prev']=s
            if neighbours in visited:
                if(distance[neighbours]['Dist']>(graph_elements[s][neighbours] + distance[s]['Dist'])):
                    distance[neighbours]['prev'] = s
                    distance[neighbours]['Dist']= graph_elements[s][neighbours]+distance[s]['Dist']
    while destination!=source:
        path.append(distance[destination]['prev'])
        destination=distance[destination]['prev']

    path.reverse()

    print(path)
    return distance




















infinity = float('inf')
distance={'C': {'Dist': infinity, 'prev': None},
          'A': {'Dist': infinity, 'prev': None},
          'F': {'Dist': infinity, 'prev': None},
          'Z': {'Dist': infinity, 'prev': None},
          'B': {'Dist': infinity, 'prev': None},
          'D': {'Dist': infinity, 'prev': None},
          'G': {'Dist': infinity, 'prev': None},
          'E': {'Dist': infinity, 'prev': None}}
graph_elements={'C': {'A': 2, 'F': 2, 'Z': 4},
 'A': {'C': 2, 'B': 1, 'D': 3},
 'F': {'C': 2, 'D': 1, 'G': 2},
 'Z': {'C': 4},
 'B': {'A': 1, 'D': 1, 'E': 7},
 'D': {'A': 3, 'F': 1, 'G': 5, 'B': 1},
 'G': {'D': 5, 'F': 2},
 'E': {'B': 7}}
# print(graph_elements['C']['A'])
# print(distance['A']['Dist'])
print(djk(graph_elements,distance,'C','G'))