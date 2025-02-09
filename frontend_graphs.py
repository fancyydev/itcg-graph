import networkx as nx
import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt
from graphs import Undirected_graph, Node, Edge

class CustomAlgorithmButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_500
        self.color = ft.colors.WHITE
        self.text = text 
        self.on_click = on_click
        
def create_graph_logic(graph):
    g = graph()
    for n in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
        g.add_node(Node(n))
    
    g.add_edge(Edge(g.get_node("a"), g.get_node("b"), 1.5))
    g.add_edge(Edge(g.get_node("a"), g.get_node("c"), 2.1))
    
    g.add_edge(Edge(g.get_node("b"), g.get_node("c"), 1))
    g.add_edge(Edge(g.get_node("b"), g.get_node("d"), 2.2))
    
    g.add_edge(Edge(g.get_node("c"), g.get_node("d"), 1.7))
    g.add_edge(Edge(g.get_node("c"), g.get_node("f"), 2.3))
    
    g.add_edge(Edge(g.get_node("d"), g.get_node("e"), 1.8))
    
    g.add_edge(Edge(g.get_node("e"), g.get_node("f"), 2))
    g.add_edge(Edge(g.get_node("e"), g.get_node("g"), 1.2))
    
    g.add_edge(Edge(g.get_node("f"), g.get_node("g"), 1.1))
    g.add_edge(Edge(g.get_node("f"), g.get_node("i"), 2.6))
    
    g.add_edge(Edge(g.get_node("g"), g.get_node("h"), 1.9))
    g.add_edge(Edge(g.get_node("g"), g.get_node("i"), 1.5))
    
    g.add_edge(Edge(g.get_node("h"), g.get_node("k"), 2.2))
    g.add_edge(Edge(g.get_node("h"), g.get_node("l"), 1.8))
    
    g.add_edge(Edge(g.get_node("i"), g.get_node("j"), 1.7))
    g.add_edge(Edge(g.get_node("i"), g.get_node("l"), 2.4))
    
    g.add_edge(Edge(g.get_node("j"), g.get_node("l"), 1.3))
    g.add_edge(Edge(g.get_node("j"), g.get_node("p"), 2.5))
    
    g.add_edge(Edge(g.get_node("k"), g.get_node("l"), 1.4))
    g.add_edge(Edge(g.get_node("k"), g.get_node("m"), 2.6))
    
    g.add_edge(Edge(g.get_node("l"), g.get_node("m"), 1.1))
    g.add_edge(Edge(g.get_node("l"), g.get_node("ñ"), 2.0))
    
    g.add_edge(Edge(g.get_node("m"), g.get_node("n"), 1.8))
    
    g.add_edge(Edge(g.get_node("n"), g.get_node("o"), 1.2))
    g.add_edge(Edge(g.get_node("n"), g.get_node("u"), 2.9))
    
    g.add_edge(Edge(g.get_node("ñ"), g.get_node("o"), 1.3))
    g.add_edge(Edge(g.get_node("ñ"), g.get_node("p"), 1.5))
    g.add_edge(Edge(g.get_node("ñ"), g.get_node("q"), 2.1))
    
    g.add_edge(Edge(g.get_node("o"), g.get_node("u"), 1.7))
    
    g.add_edge(Edge(g.get_node("p"), g.get_node("r"), 1.8))
    g.add_edge(Edge(g.get_node("p"), g.get_node("s"), 2.4))
    
    g.add_edge(Edge(g.get_node("q"), g.get_node("r"), 1.6))
    g.add_edge(Edge(g.get_node("q"), g.get_node("u"), 2.8))
    
    g.add_edge(Edge(g.get_node("r"), g.get_node("s"), 1.2))
    g.add_edge(Edge(g.get_node("r"), g.get_node("t"), 2.2))
    g.add_edge(Edge(g.get_node("r"), g.get_node("u"), 1.5))
    
    g.add_edge(Edge(g.get_node("s"), g.get_node("v"), 2.7))
    
    g.add_edge(Edge(g.get_node("t"), g.get_node("w"), 1.8))
    
    g.add_edge(Edge(g.get_node("u"), g.get_node("y"), 1.9))
    g.add_edge(Edge(g.get_node("u"), g.get_node("w"), 2.5))
    
    g.add_edge(Edge(g.get_node("v"), g.get_node("w"), 1.7))
    g.add_edge(Edge(g.get_node("v"), g.get_node("x"), 2.4))
    
    g.add_edge(Edge(g.get_node("w"), g.get_node("x"), 1.1))
    g.add_edge(Edge(g.get_node("w"), g.get_node("y"), 2.3))
    
    g.add_edge(Edge(g.get_node("x"), g.get_node("y"), 1.8))
    g.add_edge(Edge(g.get_node("x"), g.get_node("z"), 2.7))
    
    g.add_edge(Edge(g.get_node("y"), g.get_node("z"), 1.4))
    
    return g


def create_graph_figure(camino_numeros=None):
    # Crear el grafo
    G = nx.Graph()
    
    for i in range(27):
        G.add_node(i)

    # Agregar nodos y aristas con pesos
    aristas_con_pesos = [
        (0, 1, 1.5), (0, 2, 2.1), (1, 2, 1.0), (1, 3, 2.2), (2, 3, 1.7),
        (2, 5, 2.3), (3, 4, 1.8), (4, 6, 1.2), (4, 5, 2.0), (5, 8, 2.6),
        (5, 6, 1.1), (6, 7, 1.9), (6, 8, 1.5), (7, 10, 2.2), (7, 11, 1.8),
        (8, 11, 2.4), (8, 9, 1.7), (9, 11, 1.3), (9, 16, 2.5), (10, 11, 1.4),
        (10, 12, 2.6), (11, 12, 1.1), (11, 14, 2.0), (12, 13, 1.8), (13, 15, 1.2),
        (13, 21, 2.9), (14, 16, 1.5), (14, 15, 1.3), (14, 17, 2.1), (15, 21, 1.7),
        (16, 18, 1.8), (16, 19, 2.4), (17, 18, 1.6), (17, 21, 2.8), (18, 21, 1.5),
        (18, 20, 2.2), (18, 19, 1.2), (19, 22, 2.7), (20, 23, 1.8), (21, 23, 2.5),
        (21, 25, 1.9), (22, 23, 1.7), (22, 24, 2.4), (23, 24, 1.1), (23, 25, 2.3),
        (24, 25, 1.8), (24, 26, 2.7), (25, 26, 1.4)
    ]
    G.add_weighted_edges_from(aristas_con_pesos)

    # Posiciones personalizadas para los nodos
    posiciones_personalizadas = {
        0: (11, 6.3), 1: (11, 7.8), 2: (8.7, 5.0), 3: (9.5, 8.0), 4: (7.8, 8.2),
        5: (7.5, 5.0), 6: (7.252, 7.1), 7: (6.5, 8.0), 8: (6.45, 4.9), 9: (5.65, 4.5),
        10: (5.75, 8.9), 11: (5.5, 6.5), 12: (5.1, 8.0), 13: (4.3, 8.2), 14: (4.2, 5.0),
        15: (3.9, 6.5), 16: (4.0, 4.0), 17: (2.8, 6.0), 18: (2.0, 5.5), 19: (1.8, 4.5),
        20: (1.3, 5.5), 21: (1.6, 6.5), 22: (1.0, 4.7), 23: (0, 6.0), 24: (-1.5, 4.7),
        25: (0, 7.0), 26: (-1.0, 8.0),
    }
    
    etiquetas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Crear la figura
    fig, ax = plt.subplots(figsize=(14, 8))

    # Dibujar nodos y etiquetas
    nx.draw_networkx_nodes(G, posiciones_personalizadas, node_size=700, ax=ax, node_color='skyblue')
    nx.draw_networkx_labels(G, posiciones_personalizadas, labels={n: etiquetas[n] for n in G.nodes()}, font_size=10, ax=ax)

    # Dibujar aristas
    nx.draw_networkx_edges(G, posiciones_personalizadas, edgelist=G.edges, width=2, edge_color='gray', ax=ax)

    # Resaltar camino si se proporciona
    if camino_numeros:
        camino_aristas = list(zip(camino_numeros, camino_numeros[1:]))
        nx.draw_networkx_edges(G, posiciones_personalizadas, edgelist=camino_aristas, width=4, edge_color='red', ax=ax)

    # Dibujar etiquetas de peso
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, posiciones_personalizadas, edge_labels=edge_labels, font_size=9, ax=ax)

    ax.axis("off")
    plt.tight_layout()
    return fig
        
def main(page: ft.Page):
    fig = create_graph_figure()  # Crear la figura inicial
    
    # Container de MatplotlibChart que muestra la figura
    chart = MatplotlibChart(figure=fig, expand=True)

    
    
    def search(search_type):
        nonlocal fig  # Se usa 'nonlocal' para modificar la variable fig
        nonlocal page
        
        empty_alert = ft.AlertDialog(
            title=ft.Text("Please complete all fields"),
            icon = ft.Icon(name=ft.icons.ERROR, color=ft.colors.RED, size=50),
        )
        
        first_node = txt_initial_node.value
        last_node = txt_end_node.value
        
        if (len(first_node) == 0 or len(last_node) == 0):
            if (len(first_node) == 0 and len(last_node) == 0):
                msg = ft.Text("Please enter the starting node and the end node")
            elif (len(first_node) == 0 ):
                msg = ft.Text("Please enter the starting node")
            else:
                msg = ft.Text("Please enter the end node")
            
            empty_alert.content = msg
            
            # Puedo agregar igual un focus al que falte
            
            page.open(empty_alert)
        
        else:
            G1 = create_graph_logic(Undirected_graph)
            initial_node = G1.get_node(first_node)
            end_node = G1.get_node(last_node)
            
            if (initial_node is not None and end_node is not None):
                if search_type == 'ASearch':
                    camino_nombres, total_cost = G1.a_star_best_first_search(initial_node, end_node, "ASearch")
                elif search_type == 'BestFirst':
                    camino_nombres, total_cost = G1.a_star_best_first_search(initial_node, end_node, "BestFirst")
                elif search_type == 'Dijkstra':
                    camino_nombres, total_cost = G1.dijkstra(initial_node=initial_node, end_node=end_node)
                elif search_type == 'HillClimbing':
                    camino_nombres, total_cost = G1.hill_climbing(initial_node, end_node)
               
                nodos_nombres = {
                    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
                    10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
                    19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
                }
                nodos_nombres = {v: k for k, v in nodos_nombres.items()}
                camino_numeros = [nodos_nombres[nodo_nombre] for nodo_nombre in camino_nombres]
                
                # Actualizar la figura con el nuevo camino
                fig = create_graph_figure(camino_numeros)
                chart.figure = fig  # Actualizar el gráfico con la nueva figura
                page.update()  # Actualizar la interfaz de usuario
                
            #else:
                
    # Configuración de la página
    page.title = "Search Algorithms"
    page.window.height = 700
    page.window.width = 800
    page.window.top = 100
    page.window.left = 500
    page.window.resizable = False

    # Campos de texto configurados
    txt_initial_node = ft.TextField(
        width=50,
        height=50,
        text_align="center",
        content_padding=ft.Padding(10, 10, 10, 10),
        max_length=1,
        input_filter=ft.TextOnlyInputFilter()
    )
    txt_end_node = ft.TextField(
        width=50,
        height=50,
        text_align="center",
        content_padding=ft.Padding(10, 10, 10, 10),
        max_length=1,
        input_filter=ft.TextOnlyInputFilter()
    )
    
    
    dlg = ft.AlertDialog(
        title=ft.Text("No se permiten nulos"),
        content=ft.Text(""),
        icon=ft.Icon(name=ft.icons.ERROR, color=ft.colors.RED, size=50),
        on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
    )

    cost_text = ft.Text("Costo total: 0")
    
    # Diseño organizado con columnas y espacio entre elementos
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Initial Node:"),
                        txt_initial_node,
                    ],
                    alignment=ft.alignment.center,
                ),
                ft.Column(
                    [
                        ft.Text("End Node:"),
                        txt_end_node,
                    ],
                    alignment=ft.alignment.center,
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        ft.Row(
            [
                CustomAlgorithmButton(text="A Search", on_click=lambda e: search("ASearch")),
                CustomAlgorithmButton(text="Best First", on_click=lambda e: search("BestFirst")),
                CustomAlgorithmButton(text="Hill Climbing", on_click=lambda e: search("HillClimbing")),
                CustomAlgorithmButton(text="Dijkstra", on_click=lambda e: search("Dijkstra")),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
    
        ft.Container(
            content=chart,  # Aquí usamos el container para mostrar el gráfico
            height=400,
            expand=True
        ),
        ft.Row(
            [cost_text],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Ejecutar la aplicación
ft.app(main)
