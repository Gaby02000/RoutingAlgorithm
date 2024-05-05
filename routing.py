import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


def set_place_for_name(string):
    lugar = string
    x = ox.graph_from_place(lugar,network_type="drive")
    
    #set_nodes2(x)
    latitud_inicio=float(input("Ingrese la latitud de inicio.\n"))
    longitud_inicio=float(input("Ingrese la longitud de inicio.\n"))

    latitud_destino=float(input("Ingrese la latitud de destino.\n"))
    longitud_destino=float(input("Ingrese la longitud de destino.\n"))
    set_nodes(x,latitud_inicio,longitud_inicio,latitud_destino,longitud_destino)


def set_place_for_x_y(latitud,longitud,radio):
    x= ox.graph_from_point((latitud,longitud), radio, network_type="drive")
    latitud_inicio=float(input("Ingrese la latitud de inicio.\n"))
    longitud_inicio=float(input("Ingrese la longitud de inicio.\n"))

    latitud_destino=float(input("Ingrese la latitud de destino.\n"))
    longitud_destino=float(input("Ingrese la longitud de destino.\n"))
    set_nodes(x,latitud_inicio,longitud_inicio,latitud_destino,longitud_destino)


def set_nodes2(x):
    inicio = list(x.nodes())[0]  
    final = list(x.nodes())[99]
    ruta_mas_corta = nx.shortest_path(x, inicio, final, weight='length')
    print_map(x,ruta_mas_corta)


def set_nodes(x,lat_i,long_i,lat_d,long_d):
    inicio = ox.nearest_nodes(x, (lat_i, long_i))  
    final = ox.nearest_nodes(x, (lat_d, long_d))
    
    #inicio = list(x.nodes())[0]  
    #final = list(x.nodes())[99]
    ruta_mas_corta = nx.shortest_path(x, inicio, final, weight='distance')
    print_map(x,ruta_mas_corta)

def print_map(x,ruta_mas_corta):
    #fig, ax =ox.plot_graph(x, node_color="blue", node_size=10, edge_color="gray", edge_linewidth=0.5, figsize=(10, 10))
    fig, ax = ox.plot_graph(x, node_size=1, node_color="white", show=False)
    

    
    """
    for nodo in x.nodes:
        latitud = x.nodes[nodo]['y']
        longitud = x.nodes[nodo]['x']    
        Latitud: -43.3000
        Longitud: -65.1000   
    """
    print_nodes(ax,fig,ruta_mas_corta,x)
   
def print_nodes(ax,fig,ruta_mas_corta,x):
     
    for i in range(len(ruta_mas_corta)):
        nodo_actual = ruta_mas_corta[i]
        ax.scatter(x.nodes[nodo_actual]['x'], x.nodes[nodo_actual]['y'], color='red', s=50, zorder=5)
        
        #latitud = x.nodes[nodo_actual]['y']
       # longitud = x.nodes[nodo_actual]['x']
        #plt.text(x.nodes[nodo_actual]['x'], x.nodes[nodo_actual]['y'], f"({latitud}, {longitud})", fontsize=8, ha='right',color="white")
        

        plt.draw()
        plt.pause(0.5) 
        if i < len(ruta_mas_corta) - 1:
            ax.scatter(x.nodes[nodo_actual]['x'], x.nodes[nodo_actual]['y'], color='blue', s=50, zorder=5)
    plt.show()


def main():
    
    val=input("Ingresa 1 para cargar localidad por nombre o 2 para cargar por latitud y longitud.\n")
    if(val=='1'):
        val=input("Ingresa una localidad\nEj:Paris, Francia.\n")
        if not isinstance(val, str):
            print("El valor ingresado no es una cadena.")    
        else:
            set_place_for_name(val)
    elif (val=='2'):
        latitud=float(input("Ingresa la latitud.\n"))
        longitud=float(input("Ingresa la longitud.\n"))
        radio=float(input("Ingresa un radio.\n"))
        set_place_for_x_y(latitud,longitud,radio)
    else:
        print("Valor ingreado incorrecto.\n")
  

if __name__ == "__main__":
    main()
#ox.plot_graph(x, node_size=1, node_color="green")
#ox.plot_graph_route(x, ruta_mas_corta, route_linewidth=4, node_size=0, edge_color='white', route_color='red')