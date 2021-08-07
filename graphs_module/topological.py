def tpg_order (graph_elements):
    #print(Elements_Incom)
    Elements_Incom={}
    start_v=[]
    queue = []
    neighbours_list=[]
    for elements in graph_elements:
        Elements_Incom[elements]={}
        Elements_Incom[elements]['Incom']=0
        #print(graph_elements['C'])
        for k in graph_elements:
            if elements in graph_elements[k]:
                Elements_Incom[elements]['Incom'] = Elements_Incom[elements]['Incom']+1

    for elements in Elements_Incom:
        if(  Elements_Incom[elements]['Incom']==0):
            start_v.append(elements)
    print(start_v)
    queue.append(start_v.pop(0))

    print(queue)
    visited=[]
    path=[]
    visited.append(queue[0])


    while queue:
        start=0
        stop=0

        s=queue.pop()


            #visited.append(s)
        for neighbours in graph_elements[s]:

            if neighbours not in visited:
                start=start+1

                queue.append(neighbours)
                visited.append(neighbours)
            # if neighbours in visited and start==0 :
            #     if neighbours not in path:
            #         path.append(neighbours)
            #     if len(graph_elements[s])==0 and s not in path:
            #         path.append(neighbours)

        if start==0 and s in visited:
            if len(graph_elements[s]) == 0 and s not in path:
                path.append(s)
            if len(graph_elements[s]) != 0 and s not in path:
                for neighbours in  graph_elements[s]:
                    if neighbours in path:
                        stop=stop+1
            if stop== len(graph_elements[s]) and s not in path:
                path.append(s)



        if len(queue)==0:
            for elements  in neighbours_list:
                if elements not in path:
                    queue.append(elements)
        if len(queue) == 0 and len(start_v)!=0:
            queue.append(start_v.pop())
            visited.append(queue[len(queue)-1])

        if s not in neighbours_list:
            neighbours_list.append(s)
    print(path)
    print(neighbours_list)












    return graph_elements




infinity = float('inf')

Elements_Incom={'C': {'Incom': 0},
          'A': {'Incom': 0},
          'F': {'Incom': 0},
          'Z': {'Incom': 0},
          'B': {'Incom': 0},
          'D': {'Incom': 0},
          'G': {'Incom': 0},
          'E': {'Incom': 0}}
graph_elements={'C': ['A', 'F', 'Z'],
                'A': ['B', 'D'],
                'F': [],
                'Z': [],
                'B': ['D', 'E'],
                'D': ['F', 'G'],
                'G': ['F'],
                'E': []}
# graph_elements={'A': ['D'],
#                 'B': ['D', 'E'],
#                 'C': ['E','H'],
#                 'D': ['F', 'G','H'],
#                 'E': ['G'],
#                 'F': [],
#                 'G': [],
#
#
#                 'H': []}

# graph_elements={'A': ['B','F'],
#                 'B': ['H'],
#                 'C': [],
#                 'D': ['C', 'I','E'],
#                 'E': ['I'],
#                 'F': [],
#                 'G': ['A','B','C'],
#                 'H': [],
#                 'I':['C'],
#
#
#                 'J': ['E']}


print(tpg_order(graph_elements))