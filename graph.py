class Graph:
    def __init__(self):
        # Using adjacency list: {location: set(connected_locations)}
        self.adj_list = {}

    def add_location(self, location):
        if location not in self.adj_list:
            self.adj_list[location] = set()

    def remove_location(self, location):
        if location in self.adj_list:
            self.adj_list.pop(location)
            for loc in self.adj_list:
                self.adj_list[loc].discard(location)

    def add_road(self, loc1, loc2):
        if loc1 in self.adj_list and loc2 in self.adj_list:
            self.adj_list[loc1].add(loc2)
            self.adj_list[loc2].add(loc1)

    def remove_road(self, loc1, loc2):
        if loc1 in self.adj_list and loc2 in self.adj_list:
            self.adj_list[loc1].discard(loc2)
            self.adj_list[loc2].discard(loc1)

    def display_connections(self):
        for loc in self.adj_list:
            print(f"{loc}: {', '.join(self.adj_list[loc])}")

    def get_locations(self):
        return list(self.adj_list.keys())