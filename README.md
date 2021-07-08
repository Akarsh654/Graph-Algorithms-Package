# Visualisation of Graph Algorithms

### Description ###

The package aims to create visual outputs for popular graph algorithms.   
Currently: BFS and DFS   
I plan to implement more algorithms:  Prim's and Kruskal's Algorithms etc   

It is not just limited to getting a visual output, but the algorithms will be optimised by using heuristics for non-polynomial time algorithms. This project aims to create a better understanding of the working of graph algorithms, improve the computation time and optimising the algorithms. It could be used by analysts as well as students and teachers, as a teaching aid.

To run the package: pip install graph-algo-vis

### Sample Code to run the package ###

### BFS and DFS ###
Import:   
from graph_algo_vis import dfs_traversal

Instantiation:   
g = dfs_traversal.DFS()

Visualize the input graph:   
g.draw_graph("input.txt")  

Visualize the result of DFS:   
g.depth_first_search("input.txt")

### Topological Sort ###  
Import:   
from graph_algo_vis import topological_sort   

Instantiation:   
g = topological_sort.Top_Sort()   

Visualize the input graph and result:   
g.topological_sort("input.txt")   

### Pre requisites ###

To run this package run you must have matplotlib and networkx libraries installed.

### INPUT ###

Input is taken from the file 
#### input.txt ####

Sample input for BFS and DFS
```
4
0 5 10 5
0 0 5 0
0 10 0 0
0 0 10 0
0

```
First line contains the number of nodes,say n.(Nodes are numbered as 0,1,2,...(n-1) )
Followed by n*n weighted matrix. Disconnected egdes are represented by negative weight.
Last line contains the source node.(i.e, the node from which the BFS or DFS should begin)

Sample input for Topological Sort:
```
6
1 2
1 3
2 3
2 4
3 4
3 5

```   
First line contains the number of edges.  
Followed by the edges eg 1 2 represents an edge from 1 to 2  


### Draw Graph ###


Graph is first drawn from the weighted matrix input from the user with weights shown. Edges are marked with black.  

![1](https://i.ibb.co/bK1Y8D4/Graph.png)


### BFS Traversal ###

Iterative BFS is performed, using a queue. Each time an edge is encountered, 
it is marked with red on the graph.

### DFS traversal ###

Recursive DFS is performed, resulting DFS forests are stored in a stack.    

![2](https://i.ibb.co/mXPTWQK/DFS-Result.png)

### Topological Sort ###   

Topological Sort is performed using Depth First Search (DFS).  

PS: Topological Sorting for a graph is not possible if the graph is not a Directed Acyclic Graph (DAG).  
Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.  

Green node - denotes the starting node.                                        
Red node - denotes the final node.   

![3](https://i.ibb.co/Rz4qPMv/Graph-after-Topological-Sort.png)  

### Time Complexity ###

0(m+n)                                                                                                        
where m - number of edges                                                                                
      n - number of nodes 


