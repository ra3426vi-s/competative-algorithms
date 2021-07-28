class GraphCreation:
    def ordered(self,graph_list):
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
    def unordered(self,graph_list):
        graph_elements_unordered={}
        for elements in graph_list:
            (s,d)=elements
            if s not in graph_elements_unordered:
                graph_elements_unordered[s]=[]
            if d not in graph_elements_unordered:
                graph_elements_unordered[d] = []


            if s in graph_elements_unordered:
                graph_elements_unordered[s].append(d)
                graph_elements_unordered[d].append(s)
        return graph_elements_unordered
graph_list=[('C', 'A'), ('C', 'F'), ('C', 'Z'),
                 ('A', 'B'), ('A', 'D'), ('D', 'F'),
                 ('D', 'G'), ('B', 'D'), ('B', 'E'), ('G', 'F')]

y=GraphCreation()
print(y.ordered(graph_list))
#print(y.unordered(graph_list))
#(s,d)=graph_list[3]
# for elements in graph_list:
#     print (elements)



