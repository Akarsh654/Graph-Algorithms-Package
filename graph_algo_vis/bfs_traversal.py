import networkx as nx
import matplotlib.pyplot as plt
 

class BFS():

	#BFS traversal 
	def __bfs(self, G, source, pos): 
		visited = [False]*(len(G.nodes()))
		level = [False]*(len(G.nodes()))
		queue = []		#a queue for BFS traversal
		queue.append(source)
		visited[source] = True
		level[source] = 0
		while queue:
			curr_node = queue.pop(0)
			for i in G[curr_node]:  #iterates through all the possible vertices adjacent to the curr_node
				if not visited[i]:
					queue.append(i)
					visited[i] = True
					level[i] = level[curr_node] + 1
					nx.draw_networkx_edges(G, pos, edgelist = [(curr_node,i)], width = 3.5, alpha = 0.6, edge_color = 'r')
		
		return



	#takes input from the file and creates a weighted graph
	def __CreateGraph(self, filename):
		G = nx.DiGraph()
		f = open(filename)
		n = int(f.readline())
		wtMatrix = []
		for i in range(n):
			list1 = map(int, (f.readline()).split())
			wtMatrix.append(list(list1))
		
		source = int(f.readline()) #source vertex from where BFS has to start
		#Adds egdes along with their weights to the graph 
		for i in range(n):
			for j in range(n):	
				if wtMatrix[i][j] > 0:
					G.add_edge(i, j, length = wtMatrix[i][j]) 
		return G, source



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

	
	def breadth_first_search(self, filename):
		G,source = self.__CreateGraph(filename)
		pos = self.__DrawGraph(G)
		self.__bfs(G, source, pos)
		plt.show()


