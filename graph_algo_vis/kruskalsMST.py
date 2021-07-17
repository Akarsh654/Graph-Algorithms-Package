import networkx as nx
import matplotlib.pyplot as plt
import sys

# References: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

class Kruskals():
	# A utility function that return the smallest unprocessed edge
	def __getMin(self, G, mstFlag):
		min = sys.maxsize  # initialize min to largest numeric value
		for i in [(u, v, edata['length']) for u, v, edata in G.edges( data = True) if 'length' in edata ]:
			if mstFlag[i] == False and i[2] < min:
				min = i[2]
				min_edge = i
		return min_edge

		

	# A utility function to find root or origin of the node i in MST
	def __findRoot(self, parent, i):
		if parent[i] == i:
			return i
		return self.__findRoot(parent, parent[i])



	# A function that does union of set x and y based on the rank
	def __union(self, parent, rank, x, y):
		xRoot = self.__findRoot(parent, x)
		yRoot = self.__findRoot(parent, y)

		# Attach smaller rank tree under root of high rank tree
		if rank[xRoot] < rank[yRoot]:
			parent[xRoot] = yRoot
		elif rank[xRoot] > rank[yRoot]:
			parent[yRoot] = xRoot
		# If ranks are same, then make any one as root and increment its rank by one
		else :
			parent[yRoot] = xRoot
			rank[xRoot] += 1



	# function that performs Kruskals algorithm on the graph G
	def __kruskals(self, G, pos):
		eLen = len(G.edges()) # eLen denotes the number of edges in G
		vLen = len(G.nodes()) # vLen denotes the number of vertices in G
		mst = [] # mst contains the MST edges
		mstFlag = {} # mstFlag[i] will hold true if the edge i has been processed for MST
		
		for i in [ (u, v, edata['length']) for u, v, edata in G.edges(data = True) if 'length' in edata ]:
			mstFlag[i] = False 

		parent = [None] * vLen # parent[i] will hold the vertex connected to i in the MST
		rank = [None] * vLen	# rank[i] will hold the rank of appearance of the node in the MST
		
		for v in range(vLen):
			parent[v] = v
			rank[v] = 0

		while len(mst) < vLen - 1 :
			curr_edge = self.__getMin(G, mstFlag) # pick the smallest egde from the set of edges
			mstFlag[curr_edge] = True # update the flag for the current edge
			y = self.__findRoot(parent, curr_edge[1])
			x = self.__findRoot(parent, curr_edge[0])
			# adds the edge to MST, if including it doesn't form a cycle
			if x != y:
				mst.append(curr_edge)
				self.__union(parent, rank, x, y)
			# Else discard the edge
		# marks the MST edges with red
		for X in mst:
			if (X[0], X[1]) in G.edges():
				nx.draw_networkx_edges(G, pos, edgelist = [(X[0], X[1])], width = 3.5, alpha = 0.6, edge_color = 'r')
		return



	# takes input from the file and creates a weighted graph
	def __CreateGraph(self, filename):
		G = nx.Graph()
		f = open(filename)
		n = int(f.readline())
		wtMatrix = []
		for i in range(n):
			list1 = map(int, (f.readline()).split())
			wtMatrix.append(list(list1))
		# Adds egdes along with their weights to the graph 
		for i in range(n) :
			for j in range(n)[i:] :
				if wtMatrix[i][j] > 0 :
						G.add_edge(i, j, length = wtMatrix[i][j]) 
		return G



	# draws the graph and displays the weights on the edges
	def __DrawGraph(self, G):
		pos = nx.spring_layout(G)
		options = {
				"node_color": "#A0CBE2",
				"edge_color": "#000000",
				"width": 3,
				"edge_cmap": plt.cm.Blues,
				"with_labels" : True,
				}
		nx.draw(G, pos, **options)  # with_labels=true is to show the node number in the output graph
		edge_labels = nx.get_edge_attributes(G, 'length')
		nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) #    prints weight on all the edges
		return pos


	def kruskals(self, filename):
		G = self.__CreateGraph(filename)
		pos = self.__DrawGraph(G)
		self.__kruskals(G, pos)
		plt.show()
