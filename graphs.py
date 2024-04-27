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
        weight = edge.get_weight()
        if n1 not in self.graph_dict:
            raise ValueError(f'Node {n1.get_name()} not in graph')
        if n2 not in self.graph_dict:
            raise ValueError(f'Node {n2.get_name()} not in graph')
        self.graph_dict[n1].append([n2, weight])
    
    def is_node_in(self, node):
        return node in self.graph_dict
    
    def get_node(self, node_name):
        #Optimizar para usar busqueda binaria dentro de los nodos
        for n in self.graph_dict:
            if node_name == n.get_name(): 
                return n
        print(f'Node {node_name} does not exist in the graph')
    
    def get_sons(self, node):
        #Acomodar para que me devuelva los hijos con la estructura de __str__
        return self.graph_dict[node]
    
    def get_search_sons(self, node, type_search):
        #Acomodar para que me devuelva los hijos con la estructura de __str__
        sons = []
        #Obtenemos el objeto nodo deseado
        node = node[0]


        for edge in self.graph_dict[node]:
            node2 = edge[0]
            weight = edge[1]
            #Dentro del costo acumulado del hijo
            #Ingresamos la suma del costo acumulado del padre y el peso hacia el nodo
            node2.set_a_cost(node.get_a_cost()+weight)
                #Actualizamos el costo f
            if type_search == "BestFirst":
                node2.set_f_cost(node2.get_a_cost())
            else:
                node2.set_f_cost(node2.get_a_cost() + node2.get_heuristic())
                #Agregamos a los hijos el arreglo
            sons.append([node2, node2.get_f_cost(), node])
        
        return sons


    def treat_repited_sons(self, sons, open_state, closed_state):
        #Validamos que haya registros en sons
        if len(sons) == 0:
            return None
        
        def find_index(arr, value):
            for idx, sublist in enumerate(arr):
                if value in sublist:
                    return idx
            return -1

        for son in sons:
            value = son[0]
            index_open = find_index(open_state,value)
            index_closed = find_index(closed_state,value)
            
            if index_open != -1 or index_closed != -1:
                sons.remove(son)

        return sons

    def update_ascending(self, state):
        
        for i in range(len(state)):
            for j in range(len(state)-1-i):
                if state[j][0].get_f_cost() > state[j+1][0].get_f_cost():
                    aux = state[j+1]
                    state[j+1] = state[j]
                    state[j] = aux
        
        return state

    def a_star_best_first_search(self, initial_node, end_node, type_search):
        open_state = []
        closed_state = []
        open_state.append([initial_node,0,initial_node])
        current = open_state[0]
        
        while len(open_state)>0  and current[0] != end_node:
            del open_state[0]
            closed_state.append(current)
            sons = self.get_search_sons(current, type_search)
            sons = self.treat_repited_sons(sons, open_state, closed_state)
            open_state.extend(sons)
            open_state = self.update_ascending(open_state)
            current = open_state[0]

        #Comprobacion si es final actual
        if current[0] == end_node:
            del open_state[0]
            closed_state.append(current)
            for i in closed_state:
                print(f"{i[0].get_name()} <-- {i[1]} -- {i[2].get_name()}")
        else:
            print("Solucion no encontrada")

    def __str__(self):
        all_edges = ''
        for n1 in self.graph_dict:
            for edge in self.graph_dict[n1]:
                n2 = edge[0]
                weight = edge[1]
                all_edges += n1.get_name() + ' -- ' + str(weight)  + ' --> ' + n2.get_name() + '\n'
        return all_edges

#Creamos una clase para manejar grafos de tipo no dirigido
class Undirected_graph(Directed_Graph):

    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(n1=edge.get_n2(), n2=edge.get_n1(), weight=edge.get_weight())
        Directed_Graph.add_edge(self, edge_back)



#Un edge esta compuesto por el nodo origen y el nodo destino
class Edge:
    def __init__(self, n1, n2, weight):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight
    def get_n1(self):
        return self.n1
    def get_n2(self):
        return self.n2
    def get_weight(self):
        return self.weight
    
    def __str__(self):
        return self.n1.get_name() +" -- "+ str(self.get_weight()) +" --> " + self.n2.get_name()

#Creamos la clase para manejar los nodos
class Node:
    #Aqui indicaremos los atributos necesarios para nuestro objeto nodo
    def __init__(self, name, h=None):
        self.name = name
        self.h = h
        self.a_cost = 0
        self.f_cost = 0
    def get_name(self):
        return self.name
    
    def get_heuristic(self):
        return self.h
    
    def get_a_cost(self):
        return self.a_cost
    
    def set_a_cost(self, a_cost):
        self.a_cost = a_cost
    
    def get_f_cost(self):
        return self.f_cost
    
    def set_f_cost(self, f_cost):
        self.f_cost = f_cost
    
    def __str__(self):
        return self.name
    
def build_graph(graph):
    g = graph()
    for n in ('a','b','c','d','e','f','g','h'):
        g.add_node(Node(n))

    g.add_edge(Edge(g.get_node("a"), g.get_node("b"), 1))
    g.add_edge(Edge(g.get_node("a"), g.get_node("c"), 2))

    g.add_edge(Edge(g.get_node("b"), g.get_node("d"), 3))
    
    g.add_edge(Edge(g.get_node("c"), g.get_node("d"), 4))
    g.add_edge(Edge(g.get_node("c"), g.get_node("e"), 2))
    g.add_edge(Edge(g.get_node("c"), g.get_node("g"), 1))

    g.add_edge(Edge(g.get_node("d"), g.get_node("f"), 5))
    g.add_edge(Edge(g.get_node("d"), g.get_node("g"), 3))

    g.add_edge(Edge(g.get_node("e"), g.get_node("g"), 2))

    g.add_edge(Edge(g.get_node("f"), g.get_node("g"), 2))
    g.add_edge(Edge(g.get_node("f"), g.get_node("h"), 1))

    g.add_edge(Edge(g.get_node("g"), g.get_node("h"), 2))
    
    g.a_star_best_first_search(g.get_node("c"), g.get_node("h"), "BestFirst")
    return g

G1 = build_graph(Undirected_graph)
