import networkx as nx
import matplotlib.pyplot as plt
import sys
# References: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

class Prims():
	#utility function that returns the minimum egde weight node
	def __minkeyance(self, key, mstSet, V):
		min = sys.maxsize # initialize min to largest numeric value 
		for v in range(V):
			if mstSet[v] == False and key[v] < min:
				min = key[v]
				min_index = v
		return min_index



	#function that performs prims algorithm on the graph G
	def __prims(self, G, pos):
		V = len(G.nodes()) # V denotes the number of vertices in G
		key = [sys.maxsize]*V # key[i] will hold the minimum weight edge value of node i in the constructed MST
		parent = [None]*V # parent[i] will hold the vertex connected to i, in the MST edge
		mstSet = [False]*V # mstSet[i] will hold true if vertex i is included in the MST 


		key[0] = 0 # Make key 0 so that this vertex is picked as first vertex
		parent[0]= -1 # starting vertex is itself the root, and hence has no parent
		for count in range(V-1):
			u = self.__minkeyance(key, mstSet, V) #pick the minimum distance vertex
			mstSet[u] = True
			# Update key value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and
			# the vertex in not in the shotest path tree
			for v in range(V):
				if (u, v) in G.edges():
    					# if u and v are adjacent vertices and v is not yet added to MST set and weight of <u,v> is 
						# less than current key of v then update key
					if mstSet[v] == False and G[u][v]['length'] < key[v]:
						key[v] = G[u][v]['length']
						parent[v] = u
						
		for X in range(V):
			if parent[X] != -1: #ignore the parent of the starting node
				if (parent[X], X) in G.edges():
					nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 3.5, alpha = 0.6, edge_color = 'r')
		return



	#takes input from the file and creates a weighted graph
	def __CreateGraph(self, filename):
		G = nx.Graph()
		f = open(filename)
		n = int(f.readline())
		wtMatrix = []
		for i in range(n):
			list1 = map(int, (f.readline()).split())
			wtMatrix.append(list(list1))
		#Adds egdes along with their weights to the graph 
		for i in range(n) :
			for j in range(n)[i:] :
				if wtMatrix[i][j] > 0 :
						G.add_edge(i, j, length = wtMatrix[i][j]) 
		return G



	#draws the graph and displays the weights on the edges
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
		edge_labels = nx.get_edge_attributes(G,'length')
		nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) #prints weight on all the edges
		return pos

	def prims(self, filename):
		G = self.__CreateGraph(filename)
		pos = self.__DrawGraph(G)
		self.__prims(G, pos)
		plt.show()	

