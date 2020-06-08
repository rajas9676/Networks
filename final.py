from networks import graph
import networkx as nx
import matplotlib.pyplot as plot

# following section need to be formatted to accept data from csv/json files rather than hard coded values
g = {"Z0": ["Z4","Z5","Z1"],
         "Z1": ["Z0","Z5","Z2"],
         "Z2": ["Z1","Z6","Z3"],
         "Z3": ["Z2","Z6","Z7"],
         "Z4": ["Z8","Z5","Z0"],
         "Z5": ["Z1","Z0","Z4","Z8"],
         "Z6": ["Z2","Z3","Z11","Z10","Z9"],
         "Z7": ["Z3","Z11"],
         "Z8": ["Z12","Z13","Z9","Z5","Z4"],
         "Z9": ["Z8","Z10","Z6"],
         "Z10": ["Z14","Z13","Z9","Z6"],
         "Z11": ["Z7", "Z6", "Z15"],
         "Z12": ["Z13", "Z8"],
         "Z13": ["Z10","Z8","Z12"],
         "Z14": ["Z15","Z10"],
         "Z15": ["Z11", "Z14"]}

original = {"Z1":{"IP_range": "10.1.1.0/24",
                  "Adjacent": ["Z4","Z5","Z6"],
                  "Firewall-rules": [{"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":80,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":3389,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":90,"action":"ALLOW"}]
                  },
            "Z2":{"IP_range": "10.1.2.0/24",
                  "Adjacent": ["Z3"],
                  "Firewall-rules": [{"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":80,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":3389,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":90,"action":"ALLOW"}]
                },
            "Z3":{"IP_range": "10.1.3.0/24",
                  "Adjacent": ["Z2","Z4"],
                  "Firewall-rules": [{"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":80,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":3389,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":90,"action":"ALLOW"}]
                },
            "Z4":{"IP_range": "10.1.3.0/24",
                  "Adjacent": ["Z2"],
                  "Firewall-rules": [{"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":80,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":3389,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":90,"action":"ALLOW"}]
                },
            "Z5":{"IP_range": "10.1.3.0/24",
                  "Adjacent": ["Z6","Z2"],
                  "Firewall-rules": [{"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":80,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":3389,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":90,"action":"ALLOW"}]
                },
            "Z6":{"IP_range": "10.1.3.0/24",
                  "Adjacent": ["Z2"],
                  "Firewall-rules": [{"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":80,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":3389,"action":"ALLOW"},
                                     {"src_net":"10.1.2.1","dst_net":"10.1.2.2","src_port":any,"dst_port":90,"action":"ALLOW"}]
            }}

graph = graph(original)
print(graph.edges())
# Add nodes and edges using NetworkX module
G = nx.Graph()
G.add_nodes_from(graph.nodes())
G.add_edges_from(graph.edges())
nx.draw(G, with_labels=True, node_size=600)
plot.show()
