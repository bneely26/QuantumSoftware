"""Provide the primary functions."""


import networkx as nx

def build_1d_graph(N, verbose=0):
    if verbose > 0: print(" Building 1D with %i sites"%N)
    Jval = 1.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval
    return G

def build_graph1(verbose=0):
    if verbose > 0: print(" Building Graph 1 with 10 sites")

    G = nx.Graph()
    G.add_nodes_from([i for i in range(10)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(10)])
    G.add_edge(2,5)
    G.add_edge(4,8)
    G.add_edge(4,0)
    for e in G.edges:
        G.edges[e]['weight'] = 1.0

    return G
    
def build_graph2(verbose=0):
    if verbose > 0: print(" Building Graph 2 with 6 sites")
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval
    return G

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    pass
