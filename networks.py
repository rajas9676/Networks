# Implementation of python class for graphs covering basic functions.

class graph(object):
    # Initialize the graph object with dictionary input provided. If no dictionary
    # is provided or None is given, then an empty dictionary will be used.
    def __init__(self,graph_dict=None):
        if(graph_dict == None):
            graph_dict = {}
        self.__graph_dict = graph_dict

    # return vertices of nodes of the graph
    def nodes(self):
        return list(self.__graph_dict.keys())

    # return edges of the graph
    def edges(self):
        return self.__generate_edges()

    # function to generate edges of the graph
    def __generate_edges(self):
        edges = []
        for node in self.__graph_dict:
            for neighbor in self.__graph_dict[node]["Adjacent"]:
                if {node, neighbor} not in edges:
                    edges.append({node, neighbor})
        return edges

    # add nodes of the graph
    def add_node(self,node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    # add edges of the graph
    def add_edge(self,edge):
        edge = set(edge)
        (node1,node2) = tuple(edge)
        if node1 in self.__graph_dict:
            self.__graph_dict[node1].append(node2)
        else:
            self.__graph_dict[node1] = [node2]

    # print the resulting nodes and edges from graph input
    def __str__(self):
        res = "Nodes: "
        for node in self.__graph_dict:
            res = res + str(node) + " "
        res = res + "\nedges: "
        for edge in self.__generate_edges():
            res = res + str(edge) + " "
        return res


