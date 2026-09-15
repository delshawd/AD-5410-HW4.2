from Graph import *
import math


def calculate_distance(orig, dest):
    dlon = dest[1] - orig[1]
    dlat = dest[0] - orig[0]

    a = (math.sin(math.radians(dlat / 2)))**2 + \
        math.cos(math.radians(orig[0])) * \
        math.cos(math.radians(dest[0])) * \
        (math.sin(math.radians(dlon / 2)))**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 3961
    d = R * c

    return d


def load_graph(g):
    gilroy = [37.0065078, -121.5631723]
    cheyenne = [41.139981, -104.820246]
    fargo = [46.877229, -96.789821]
    zanesville = [39.9401426, -82.005019]
    worcester = [42.2625621, -71.8018877]
    tupelo = [34.2576067, -88.7033859]
    lubbock = [33.5855677, -101.8470215]

    g.add_vertex('Gilroy')
    g.add_vertex('Cheyenne')
    g.add_vertex('Fargo')
    g.add_vertex('Zanesville')
    g.add_vertex('Worcester')
    g.add_vertex('Tupelo')
    g.add_vertex('Lubbock')

    g.add_edge('Lubbock', 'Gilroy',
               calculate_distance(lubbock, gilroy), True)

    g.add_edge('Lubbock', 'Fargo',
               calculate_distance(lubbock, fargo), True)

    g.add_edge('Lubbock', 'Zanesville',
               calculate_distance(lubbock, zanesville), True)

    g.add_edge('Gilroy', 'Cheyenne',
               calculate_distance(gilroy, cheyenne), True)

    g.add_edge('Cheyenne', 'Fargo',
               calculate_distance(cheyenne, fargo), True)

    g.add_edge('Cheyenne', 'Lubbock',
               calculate_distance(cheyenne, lubbock), True)

    g.add_edge('Fargo', 'Zanesville',
               calculate_distance(fargo, zanesville), True)

    g.add_edge('Tupelo', 'Lubbock',
               calculate_distance(tupelo, lubbock), True)

    g.add_edge('Tupelo', 'Zanesville',
               calculate_distance(tupelo, zanesville), True)

    g.add_edge('Zanesville', 'Worcester',
               calculate_distance(zanesville, worcester), True)

    g.add_edge('Worcester', 'Tupelo',
               calculate_distance(worcester, tupelo), True)

# end def load_graph(g):


def path_to_target(start, goal, g):
    dijkstra(g, g.get_vertex(start), g.get_vertex(goal))

    target = g.get_vertex(goal)
    path = [target.get_id()]
    shortest(target, path)

    return path[::-1], target.get_distance()

# end def path_to_target(start, goal, g):


def main():
    graph = Graph()
    load_graph(graph)
    path, distance = path_to_target('Gilroy', 'Lubbock', graph)
    print('Gilroy to Lubbock:', path, distance)

    graph = Graph()
    load_graph(graph)
    path, distance = path_to_target('Gilroy', 'Zanesville', graph)
    print('Gilroy to Zanesville:', path, distance)

    graph = Graph()
    load_graph(graph)
    path, distance = path_to_target('Tupelo', 'Fargo', graph)
    print('Tupelo to Fargo:', path, distance)

    graph = Graph()
    load_graph(graph)
    path, distance = path_to_target('Worcester', 'Gilroy', graph)
    print('Worcester to Gilroy:', path, distance)

# end def main():


if __name__ == "__main__":
    main()