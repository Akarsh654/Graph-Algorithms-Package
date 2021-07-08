import networkx as nx
import matplotlib.pyplot as plt
 

class DFS():
	#utility fucntion used by DFS which does recursive depth first search 
	def __DFSUtil(self, G, v, visited, sl): 
		visited[v] = True
		sl.append(v) 
		for i in G[v]:
			if not visited[i]:
				self.__DFSUtil(G, i, visited, sl)
		return sl
	


	#DFS traversal 
	def __dfs(self, G, source): 
		visited = [False]*(len(G.nodes()))
		sl = []		#a list that stores dfs forest starting with source node
		stack = [] #A nested list that stores all the DFS Forest's
		stack.append(self.__DFSUtil(G, source, visited, sl))
		for i in range(len(G.nodes())):
			if not visited[i]:
				sl = []
				stack.append(self.__DFSUtil(G, i, visited, sl))
		return stack
				


	#takes input from the file and creates a weighted graph
	def __CreateGraph(self, filename):
		G = nx.DiGraph()
		f = open(filename)
		n = int(f.readline())
		wtMatrix = []
		for i in range(n):
			list1 = map(int,(f.readline()).split())
			wtMatrix.append(list(list1))
		source = int(f.readline()) #source vertex from where DFS has to start
		#Adds egdes along with their weights to the graph 
		for i in range(n):
			for j in range(n):
				if wtMatrix[i][j] > 0:
						G.add_edge(i, j, length = wtMatrix[i][j]) 
		return G,source



	#marks all edges traversed through DFS with red
	def __DrawDFSPath(self, G, stack):
		pos = nx.spring_layout(G)
		options = {
		"node_color": "#A0CBE2",
		"edge_color": "#000000",
		"width": 3,
		"edge_cmap": plt.cm.Blues,
		"with_labels" : True,
		}
		nx.draw(G, pos, **options)  #with_labels=true is to show the node number in the output graph
		edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])
		nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
		for i in stack:
			#if there is more than one node in the dfs-forest, then print the corresponding edges
			if len(i) > 1:
				for j in i[ :(len(i)-1)]:
					if i[i.index(j)+1] in G[j]:
						nx.draw_networkx_edges(G, pos, edgelist = [(j,i[i.index(j)+1])], width = 3.5, alpha = 0.6, edge_color = 'r')
					else:
						#if in case the path was reversed because all the possible neighbours were visited, we need to find the adj node to it.
						for k in i[1::-1]: 
							if k in G[j]:
								nx.draw_networkx_edges(G, pos, edgelist = [(j,k)], width = 3.5, alpha = 0.6, edge_color = 'r')
								break
	
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
		edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])
		nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
		return pos

	def draw_graph(self, filename):
		G,source = self.__CreateGraph(filename)
		self.__DrawGraph(G)
		plt.show()							

	
	def depth_first_search(self, filename):
		G, source = self.__CreateGraph(filename)
		stack = self.__dfs(G, source)
		self.__DrawDFSPath(G, stack)
		plt.show()





