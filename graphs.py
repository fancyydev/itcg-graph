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
    
    def get_graph_len(self):
        return len(self.graph_dict)
    
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
        if type_search != "Dijkstra" and type_search != "HillClimbing":
            node = node[0]
        
        for edge in self.graph_dict[node]:
            node2 = edge[0]
            weight = edge[1]
            #Dentro del costo acumulado del hijo
            #El coste acumulado va a ser igual a el peso en caso de que la busqueda sea HillClimbing
            if type_search == "HillClimbing":
                node2.set_a_cost(weight)
            else:
                #Ingresamos la suma del costo acumulado del padre y el peso hacia el nodo    
                node2.set_a_cost(node.get_a_cost()+weight)
            
            #Actualizamos el costo f
            if type_search == "BestFirst":
                node2.set_f_cost(node2.get_a_cost())    
            elif type_search == "ASearch":
                node2.set_f_cost(node2.get_a_cost() + node2.get_heuristic())
                #Agregamos a los hijos el arreglo
            
            if (type_search == "Dijkstra" or type_search == "HillClimbing"):
                sons.append([node2, node2.get_a_cost()])
            else:
                sons.append([node2, node2.get_f_cost(), node])
        
        return sons


    def treat_repited_sons(self, sons, open_state=None, closed_state=None, type_search = None):
        #Validamos que haya registros en sons
        elements_to_remove = []
        
        if (type_search == None):
            
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
                    #Se cambio el remove solo por la lista para evitar errores
                    elements_to_remove.append(son)

            for item in elements_to_remove:
                sons.remove(item)
                
        if type_search == "Dijkstra" and open_state is None:
            
            # Recopilamos elementos que se deben eliminar
            for son in sons:
                son_object = son[0]
                if son_object in closed_state:
                    elements_to_remove.append(son)

            # Eliminamos elementos después de la iteración
            for item in elements_to_remove:
                sons.remove(item)
                    
        elif(type_search == "Dijkstra" and open_state is not None):

            if len(sons) == 0:
                return open_state
            
            def find_index(arr, value):
                for idx, sublist in enumerate(arr):
                    if value in sublist:
                        return idx
                return -1
            
            
            #Eliminamos los hijos que tengan un mayor peso que en open_state
            for son in sons:
                son_object = son[0]
                son_weight = son[1]
                
                index_open = find_index(open_state,son_object)
                #Si el hijo se encuentra en open_state
                if index_open != -1:
                    #Y su peso es mayor en sons se elimina de sons
                    if son_weight > open_state[index_open][1]:
                        son_object.set_a_cost(open_state[index_open][1])
                    else:
                        #Si su peso en sons es menor que en open_state
                        #Se modifica el hijo de open
                        open_state[index_open] = son
                #Si no esta el hijo dentro de open_state que lo agrege
                else:
                    open_state.append(son)
            #Regresamos el open_state despues de las operaciones    
            return open_state
        
        elif(type_search == "HillClimbing"):
            for son in sons:
                son_object = son[0]
                if (son_object.get_used() == True):
                    elements_to_remove.append(son)
                    
            for item in elements_to_remove:
                sons.remove(item)
        
        return sons

    def update_ascending(self, state, type_search = None):
        #Ordenamos en base al peso temporal
        if type_search == "Dijkstra" or type_search == "HillClimbing":
            for i in range(len(state)):
                for j in range(len(state)-1-i):
                    if state[j][1] > state[j+1][1]:
                        aux = state[j+1]
                        state[j+1] = state[j]
                        state[j] = aux
        else:     
            for i in range(len(state)):
                for j in range(len(state)-1-i):
                    if state[j][0].get_f_cost() > state[j+1][0].get_f_cost():
                        aux = state[j+1]
                        state[j+1] = state[j]
                        state[j] = aux
            
        return state

    def get_next_son_level(self, current_level):
        level_nodes = []
        for node in self.graph_dict.keys():
            if node.get_level() == current_level and node.get_used() == False:
                level_nodes.append([node, node.get_a_cost()])
        
        if len(level_nodes) == 0:
            return None    
        level_nodes = self.update_ascending(level_nodes, "HillClimbing")
        return level_nodes[0][0]
    
    #Podria los algoritmos de busqueda ingresarlos dentro de otra clase para reescribir sus
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
    #Dijkstra
    def dijkstra(self, initial_node, end_node):
        final_weight = []
        temporal_weight = []
        temporal_weight.append([initial_node, 0])
        current = initial_node
        graph_len = self.get_graph_len()
        
        
        while(len(final_weight)<graph_len):    
            sons = self.get_search_sons(current, "Dijkstra")
            #Tratar repetidos buscando eliminar los hijos que ya esten en final weight 
            sons = self.treat_repited_sons(sons, closed_state=final_weight, type_search="Dijkstra")
            #Operamos con temporal weight verificando si ya existen que tengan un menor peso para cambiarlos y si no lo agregamos
            temporal_weight = self.treat_repited_sons(sons, open_state=temporal_weight, type_search="Dijkstra")
            #Ordenamos de manera ascendente
            temporal_weight = self.update_ascending(temporal_weight, "Dijkstra")
            
            for nodes in temporal_weight:
                nodes[0].set_a_cost(nodes[1])
                
            current.set_f_cost(temporal_weight[0][1])
            final_weight.append(current)
            del temporal_weight[0]
            if len(temporal_weight)>0:
                current = temporal_weight[0][0]
            
        
        for i in final_weight:
            #print(len(final_weight))
            print(i.get_name() + " " +str(i.get_f_cost()))
    
    def hill_climbing(self, initial_node, end_node):
        nodes_route = []
        current = initial_node
        current.set_level(0)
        current.set_used(True)
        nodes_route.append([current.get_name(),"Raiz"])
        
        current_level = 1
        level_asign = 1
        
        while current != end_node:
            #La estructura de sons es [son, weight=a_cost]
            sons = self.get_search_sons(current, type_search="HillClimbing")
            #Vamos a tratar como repetidos aquellos hijos que ya hayan sido usados
            sons = self.treat_repited_sons(sons=sons, type_search="HillClimbing")
            if (len(sons) != 0):
                for son in sons:
                    son_object = son[0]
                    son_object.set_father(current)
                    if  (son_object.get_level() == -1):
                        son_object.set_level(level_asign)
                level_asign += 1
                sons = self.update_ascending(sons, "HillClimbing")
                current = sons[0][0]
                current.set_used(True) 
            else:
                current = self.get_next_son_level(current_level)
                while (current == None):
                    current_level += 1 
                    current = self.get_next_son_level(current_level)
                current.set_used(True) 
            
            nodes_route.append([current.get_name(),current.get_father().get_name()])
        
        for i in nodes_route:
            print(i[0] + " <--- "+ i[1])
        
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
        
        #Atributos necesarios para hill climbing
        self.level = -1
        self.used = False
        self.father = None
    
    def get_level(self):
        return self.level
    def get_used(self):
        return self.used
    def get_father(self):
        return self.father
    
    def set_level(self, level):
        self.level = level
    def set_used(self, used):
        self.used = used
    def set_father(self, father):
        self.father = father
    
        
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
    # for n in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','p'):
    #     g.add_node(Node(n))

    # g.add_edge(Edge(g.get_node("a"), g.get_node("b"), 8))
    # g.add_edge(Edge(g.get_node("a"), g.get_node("e"), 4))
    # g.add_edge(Edge(g.get_node("a"), g.get_node("d"), 5))
    
    # g.add_edge(Edge(g.get_node("b"), g.get_node("c"), 3))
    # g.add_edge(Edge(g.get_node("b"), g.get_node("f"), 4))
    # g.add_edge(Edge(g.get_node("b"), g.get_node("e"), 12))
    
    # g.add_edge(Edge(g.get_node("c"), g.get_node("g"), 11))
    # g.add_edge(Edge(g.get_node("c"), g.get_node("f"), 9))
    
    # g.add_edge(Edge(g.get_node("d"), g.get_node("e"), 9))
    # g.add_edge(Edge(g.get_node("d"), g.get_node("h"), 6))
    
    # g.add_edge(Edge(g.get_node("e"), g.get_node("f"), 3))
    # g.add_edge(Edge(g.get_node("e"), g.get_node("i"), 8))
    # g.add_edge(Edge(g.get_node("e"), g.get_node("j"), 5))
    
    # g.add_edge(Edge(g.get_node("f"), g.get_node("g"), 1))
    # g.add_edge(Edge(g.get_node("f"), g.get_node("k"), 8))
    
    # g.add_edge(Edge(g.get_node("g"), g.get_node("k"), 8))
    # g.add_edge(Edge(g.get_node("g"), g.get_node("l"), 7))
    
    # g.add_edge(Edge(g.get_node("h"), g.get_node("i"), 2))
    # g.add_edge(Edge(g.get_node("h"), g.get_node("m"), 7))
    
    # g.add_edge(Edge(g.get_node("i"), g.get_node("j"), 10))
    # g.add_edge(Edge(g.get_node("i"), g.get_node("m"), 6))
    
    # g.add_edge(Edge(g.get_node("j"), g.get_node("k"), 6))
    # g.add_edge(Edge(g.get_node("j"), g.get_node("n"), 9))
    
    # g.add_edge(Edge(g.get_node("k"), g.get_node("l"), 5))
    # g.add_edge(Edge(g.get_node("k"), g.get_node("p"), 7))
    
    # g.add_edge(Edge(g.get_node("l"), g.get_node("p"), 6))
    
    # g.add_edge(Edge(g.get_node("m"), g.get_node("n"), 2))
    
    # g.add_edge(Edge(g.get_node("n"), g.get_node("p"), 12))
    
    
    #g.a_star_best_first_search(g.get_node("c"), g.get_node("h"), "BestFirst")
    
    #AJUSTAR PARA EN DIJKSTRA PONER EL TYPE DESDE AQUI
    #g.dijkstra(g.get_node("a"), g.get_node("p"))
    
    for n in ('a','b','c','d','e','f','g','h','i','j','k','l','m'):
        g.add_node(Node(n))
    
    g.add_edge(Edge(g.get_node("a"), g.get_node("b"), 3))
    g.add_edge(Edge(g.get_node("a"), g.get_node("f"), 5))
    g.add_edge(Edge(g.get_node("a"), g.get_node("c"), 8))
   
    g.add_edge(Edge(g.get_node("b"), g.get_node("e"), 1))
    
    g.add_edge(Edge(g.get_node("c"), g.get_node("g"), 9))
    g.add_edge(Edge(g.get_node("c"), g.get_node("d"), 10))
    
    g.add_edge(Edge(g.get_node("d"), g.get_node("k"), 6))
    
    g.add_edge(Edge(g.get_node("e"), g.get_node("h"), 4))
    g.add_edge(Edge(g.get_node("e"), g.get_node("i"), 3))
    
    g.add_edge(Edge(g.get_node("g"), g.get_node("j"), 7))
    g.add_edge(Edge(g.get_node("g"), g.get_node("k"), 8))
    
    g.add_edge(Edge(g.get_node("k"), g.get_node("m"), 5))
    g.add_edge(Edge(g.get_node("k"), g.get_node("l"), 3))
    
    g.hill_climbing(g.get_node("a"), g.get_node("m"))
    
    return g

G1 = build_graph(Undirected_graph)
