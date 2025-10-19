from graph import Graph

class LocationManager:
    def __init__(self, graph):
        self.graph = graph

    def add_location(self, location):
        self.graph.add_location(location)

    def remove_location(self, location):
        self.graph.remove_location(location)

    def add_road(self, loc1, loc2):
        self.graph.add_road(loc1, loc2)

    def remove_road(self, loc1, loc2):
        self.graph.remove_road(loc1, loc2)