class GraphCreation:

    def directed(self,graph_list):
        graph_elements={}
        for elements in graph_list:
            (s,d)=elements
            if s not in graph_elements:
                graph_elements[s]=[]
            if d not in graph_elements:
                graph_elements[d] = []

            if s in graph_elements:
                graph_elements[s].append(d)
        return graph_elements
    def undirected(self,graph_list):
        graph_elements_undirected={}
        distance_table={}
        infinity = float('inf')
        for elements in graph_list:
            (s,d,w)=elements
            if s not in graph_elements_undirected:
                graph_elements_undirected[s]={}
                distance_table[s]={}
            if d not in graph_elements_undirected:
                graph_elements_undirected[d] = {}
                distance_table[d] = {}


            if s in graph_elements_undirected:
                graph_elements_undirected[s][d]=w
                graph_elements_undirected[d][s]=w
                distance_table[s]['Dist'] = infinity
                distance_table[s]['prev'] = None
                distance_table[d]['Dist']=infinity
                distance_table[d]['prev'] = None
        print(distance_table)
        return graph_elements_undirected
graph_list=[('C', 'A',2), ('C', 'F',2), ('C', 'Z',4),
                 ('A', 'B',1), ('A', 'D',3), ('D', 'F',1),
                 ('D', 'G',5), ('B', 'D',1), ('B', 'E',7), ('G', 'F',2)]
y=GraphCreation()
print(y.undirected(graph_list))