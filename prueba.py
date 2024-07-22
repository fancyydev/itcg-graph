import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

# Función para visualizar el grafo
def visualizar_grafo(camino_numeros=None):
    # Crear un grafo vacío
    G = nx.Graph()

    # Agregar nodos al grafo
    for i in range(27):
        G.add_node(i)

    # Agregar aristas al grafo con pesos (distancias)
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

    # Definir las posiciones de los nodos manualmente
    posiciones_personalizadas = {
        0: (11, 6.3), 1: (11, 7.8), 2: (8.7, 5.0), 3: (9.5, 8.0), 4: (7.8, 8.2),
        5: (7.5, 5.0), 6: (7.252, 7.1), 7: (6.5, 8.0), 8: (6.45, 4.9), 9: (5.65, 4.5),
        10: (5.75, 8.9), 11: (5.5, 6.5), 12: (5.1, 8.0), 13: (4.3, 8.2), 14: (4.2, 5.0),
        15: (3.9, 6.5), 16: (4.0, 4.0), 17: (2.8, 6.0), 18: (2.0, 5.5), 19: (1.8, 4.5),
        20: (1.3, 5.5), 21: (1.6, 6.5), 22: (1.0, 4.7), 23: (0, 6.0), 24: (-1.5, 4.7),
        25: (0, 7.0), 26: (-1.0, 8.0),
    }

    # Crear un diccionario para mapear los nombres de los nodos
    nombres_nodos = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
        10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
        19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }
    nodos_nombres = {v: k for k, v in nombres_nodos.items()}

    # Ajustar el tamaño de la figura
    fig.clear()
    ax = fig.add_subplot(111)

    if camino_numeros:
        # Verificar si el camino elegido es válido
        camino_valido = True
        for i in range(len(camino_numeros) - 1):
            if not G.has_edge(camino_numeros[i], camino_numeros[i + 1]):
                camino_valido = False
                break

        if camino_valido:
            mensaje_estado.config(text=f"El camino ingresado es válido.")
            # Función para visualizar el camino y resaltar las aristas en rojo
            path_edges = list(zip(camino_numeros, camino_numeros[1:]))
            nx.draw(G, pos=posiciones_personalizadas, labels=nombres_nodos, with_labels=True, node_color='skyblue', ax=ax)
            nx.draw_networkx_nodes(G, pos=posiciones_personalizadas, nodelist=camino_numeros, node_color='r', ax=ax)
            nx.draw_networkx_edges(G, pos=posiciones_personalizadas, edgelist=path_edges, edge_color='r', width=2, ax=ax)
        else:
            mensaje_estado.config(text="El camino ingresado no es válido.")
            nx.draw(G, pos=posiciones_personalizadas, labels=nombres_nodos, with_labels=True, node_color='skyblue', ax=ax)
    else:
        # Visualizar el grafo sin rutas al inicio
        nx.draw(G, pos=posiciones_personalizadas, labels=nombres_nodos, with_labels=True, node_color='skyblue', ax=ax)

    # Añadir etiquetas con los pesos de las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=posiciones_personalizadas, edge_labels=labels)

    canvas.draw()

# Crear una aplicación de Tkinter
app = tk.Tk()
app.title("BUSQUEDAS")
app.geometry('1400x420')
app.configure(background='black')

# Crear un contenedor para la interfaz de usuario
frame_interfaz = ttk.Frame(app)
frame_interfaz.pack(side=tk.LEFT, padx=10, pady=10)

# Instrucciones
instrucciones_texto = "Ingrese los nombres de los nodos del camino separados por comas (por ejemplo, a,b,d,e):"
instrucciones = ttk.Label(frame_interfaz, text=instrucciones_texto, font=("Arial", 10, "bold"))
instrucciones.grid(row=0, column=0, columnspan=2, pady=5)

# Entrada de texto para ingresar el camino
entrada_camino = ttk.Entry(frame_interfaz, width=50)
entrada_camino.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Botón para iniciar la búsqueda y visualización
def buscar_y_visualizar():
    camino_nombres = entrada_camino.get().split(',')
    nodos_nombres = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
        10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
        19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }
    nodos_nombres = {v: k for k, v in nodos_nombres.items()}
    camino_numeros = [nodos_nombres[nodo_nombre] for nodo_nombre in camino_nombres]
    visualizar_grafo(camino_numeros)

# Botones
boton_Aserch = ttk.Button(frame_interfaz, text="A search", command=buscar_y_visualizar)
boton_Aserch.grid(row=2, column=0, columnspan=2, padx=7, pady=10)
boton_Aserch.config(width=20)

boton_best = ttk.Button(frame_interfaz, text="Best First", command=buscar_y_visualizar)
boton_best.grid(row=3, column=0, columnspan=2, padx=7, pady=10)
boton_best.config(width=20)

boton_hill = ttk.Button(frame_interfaz, text="Hill Climbing", command=buscar_y_visualizar)
boton_hill.grid(row=4, column=0, columnspan=2, padx=7, pady=10)
boton_hill.config(width=20)

boton_dij = ttk.Button(frame_interfaz, text="Dijkstra", command=buscar_y_visualizar)
boton_dij.grid(row=5, column=0, columnspan=2, padx=7, pady=10)
boton_dij.config(width=20)

# Etiqueta para mostrar el estado del camino
mensaje_estado = ttk.Label(frame_interfaz, text="")
mensaje_estado.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Crear un contenedor 
frame_grafo = ttk.Frame(app)
frame_grafo.pack(side=tk.RIGHT, padx=15, pady=10)

# Crear la figura 
fig, ax = plt.subplots(figsize=(15, 6))  # Ajustar el tamaño de la figura aquí
canvas = FigureCanvasTkAgg(fig, master=frame_grafo)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Visualizar el grafo inicial
visualizar_grafo()

# Función para manejar el evento de cierre de la ventana
def on_closing():
    app.quit()  # Detiene el bucle principal de Tkinter
    app.destroy()  # Destruye la ventana

app.protocol("WM_DELETE_WINDOW", on_closing)  # Llama a on_closing cuando se cierra la ventana

# Ejecutar la aplicación
app.mainloop()
