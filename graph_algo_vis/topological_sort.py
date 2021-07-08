import networkx as nx
import matplotlib.pyplot as plt
 
class Top_Sort:
    
    # A recursive function used by topologicalSort
    def __topologicalSortUtil(self, v, visited, stack, G):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in range(len(G.nodes())):
            if visited[i] == False:
                self.__topologicalSortUtil(i, visited, stack, G)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def __topologicalSort(self, G):
        # Mark all the vertices as not visited
        visited = [False]*len(G.nodes())
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(len(G.nodes())):
            if visited[i] == False:
                self.__topologicalSortUtil(i, visited, stack, G)
 
        # Print contents of the stack
        return stack[::-1]  # return list in reverse order
    
    def __CreateGraph(self, filename):
        G = nx.DiGraph()
        f = open(filename)
        n = int(f.readline())
        for i in range(n):
            adj_list = list(map(int, (f.readline()).split()))
            G.add_edge(adj_list[0], adj_list[1]) 
        return G

    #takes input from the file and creates a directed graph
    def __CreateResultGraph(self, sorted_list):
        D = nx.DiGraph()
        for i in range(len(sorted_list)-1): 
            D.add_edge(sorted_list[i], sorted_list[i+1]) 
        pos = nx.spring_layout(D)
        val_map = {}
        val_map[sorted_list[0]] = 'green'
        val_map[sorted_list[len(sorted_list)-1]] = 'red'
        values = [val_map.get(node, 'blue') for node in D.nodes()]
        options = {
		"node_color": values,
		"edge_color": "#000000",
		"width": 3,
		"edge_cmap": plt.cm.Blues,
		"with_labels" : True,
		}
        nx.draw(D, pos, **options)
    
    #draws the graph
    def __DrawGraph(self, G):
        pos = nx.spring_layout(G)
        options = {
		"node_color": "#A0CBE2",
		"edge_color": "#000000",
		"width": 3,
		"edge_cmap": plt.cm.Blues,
		"with_labels" : True,
		}
        nx.draw(G, pos, **options)  #with_labels=true is to show the node number in the output graph
        return pos

    def topological_sort(self, filename):
        G = self.__CreateGraph(filename=filename)
        plt.figure("Input Graph")
        pos = self.__DrawGraph(G)
        plt.figure("Graph after Topological Sort")
        sorted_list = self.__topologicalSort(G=G)
        self.__CreateResultGraph(sorted_list)
        plt.show()

