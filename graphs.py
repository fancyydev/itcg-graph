#Creamos la clase para manejar los grafos de tipo dirigido
class Directed_Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, node):
        if node in self.graph_dict:
            return "Node alredy in graph"
        # Esto nos permite agregar el nodo como key
        # dentro del diccionario
        self.graph_dict[node] = []
    
    def add_edge(self, edge):
        n1 = edge.get_n1()
        n2 = edge.get_n2()
        if n1 not in self.graph_dict:
            raise ValueError(f'Node {n1.get_name()} not in graph')
        if n2 not in self.graph_dict:
            raise ValueError(f'Node {n2.get_name()} not in graph')
        self.graph_dict[n1].append(n2)
    
    def is_node_in(self, node):
        return node in self.graph_dict
    
    def get_node(self, node_name):
        #Optimizar para usar busqueda binaria dentro de los nodos
        for n in self.graph_dict:
            if node_name == n.get_name(): 
                return n
        print(f'Node {node_name} does not exist in the graph')
    
    def get_children(self, node):
        return self.graph_dict[node]

    def __str__(self):
        all_edges = ''
        for n1 in self.graph_dict:
            for n2 in self.graph_dict[n1]:
                all_edges += n1.get_name() + ' ---> ' + n2.get_name() + '\n'
        return all_edges

#Creamos una clase para manejar grafos de tipo no dirigido
class Undirected_graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(n1=edge.get_n2(), n2=edge.get_n1())
        Directed_Graph.add_edge(self, edge_back)



#Un edge esta compuesto por el nodo origen y el nodo destino
class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def get_n1(self):
        return self.n1
    def get_n2(self):
        return self.n2
    def __str__(self):
        return self.n1.get_name() + " ---> " + self.n1.get_name()

#Creamos la clase para manejar los nodos
class Node:
    #Aqui indicaremos los atributos necesarios para nuestro objeto nodo
    def __init__(self, name):
        self.name = name
        self.h = 1
    def get_name(self):
        return self.name
    def get_heuristic(self):
        return str(self.h)
    def __str__(self):
        return self.name
    
def build_graph(graph):
    g = graph()
    for n in ('a','b','c','d','e','f','g','h','i','j'):
        g.add_node(Node(n))

    g.add_edge(Edge(g.get_node("a"), g.get_node("b")))
    
    a = g.get_node("a")
    print(a.get_name()+a.get_heuristic())

    return g

G1 = build_graph(Directed_Graph)

print(type(G1))
print(G1)