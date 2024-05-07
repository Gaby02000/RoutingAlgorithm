import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


def set_place_for_name(string):
    place = string
    x = ox.graph_from_place(place,network_type="drive")
    
    #set_nodes2(x)
    n= (input("Enter the starting latitude and longitude.\n"))
    val=n.split(', ')
    starting_latitude=float(val[0])
    print(starting_latitude)
    starting_longitude=float(val[1])
   

    n=(input("Enter the destination latitude and longitude.\n"))
    val=n.split(', ')
    destination_latitude = float(val[0])
    destination_longitude = float(val[1])
    set_nodes(x,starting_latitude,starting_longitude,destination_latitude,destination_longitude)


def set_place_for_x_y(latitude,longitude,radius):
    x= ox.graph_from_point((latitude,longitude), radius, network_type="drive")
    n= (input("Enter the starting latitude and longitude.\n"))
    val=n.split(', ')
    starting_latitude=float(val[0])
    starting_longitude=float(val[1])
   

    n=(input("Enter the destination latitude and longitude.\n"))
    val=n.split(', ')
    destination_latitude = float(val[0])
    destination_longitude = float(val[1])
    set_nodes(x,starting_latitude,starting_longitude,destination_latitude,destination_longitude)

"""
def set_nodes2(x):
    #starting = list(x.nodes())[0]  
    #destination = list(x.nodes())[99]
    starting=6291226777
    destination=5892299693
    
    shortest_route = nx.shortest_path(x, starting, destination, weight='length')
    print_map(x,shortest_route)
"""

def set_nodes(x,lat_i,long_i,lat_d,long_d):
    starting = ox.nearest_nodes(x, long_i, lat_i)  
    destination = ox.nearest_nodes(x, long_d, lat_d)

    shortest_route = nx.shortest_path(x, starting, destination, weight='length')
    print_map(x,shortest_route)

def print_map(x,shortest_route):
    #fig, ax =ox.plot_graph(x, node_color="blue", node_size=10, edge_color="gray", edge_linewidth=0.5, figsize=(10, 10))
    fig, ax = ox.plot_graph(x, node_size=1, node_color="white", show=False)
    print_nodes(ax,fig,shortest_route,x)
   
def print_nodes(ax,fig,shortest_route,x):

    for i in range(len(shortest_route)):
        actual_node = shortest_route[i]
        ax.scatter(x.nodes[actual_node]['x'], x.nodes[actual_node]['y'], color='red', s=50, zorder=5)
        
        #ax.text(x.nodes[actual_node]['x'], x.nodes[actual_node]['y'], str(actual_node), fontsize=8, ha='right', color='white')

        plt.draw()
        plt.pause(0.5) 
        if i < len(shortest_route) - 1:
            ax.scatter(x.nodes[actual_node]['x'], x.nodes[actual_node]['y'], color='blue', s=50, zorder=5)
    plt.show()


def main():
    
    val=input("Enter 1 to load location by name or 2 to load by latitude and longitude.\n")
    if(val=='1'):
        val=input("Enter a location. \nExample: Paris, France.\n")
        if not isinstance(val, str):
            print("The entered value is not a string.")    
        else:
            set_place_for_name(val)
    elif (val=='2'):
        n=(input("Enter the latitude and longitude of the location.\n"))
        y=n.split(', ')
        latitude=float(y[0])
        longitude=float(y[1])
        radius=float(input("Enter a radius.\n"))
        set_place_for_x_y(latitude, longitude, radius)
    else:
        print("Incorrect input value.\n")


if __name__ == "__main__":
    main()
