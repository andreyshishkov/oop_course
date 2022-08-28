class Vertex:

    def __init__(self):
        self._links = []  # List[Link]
        self.min_weight = float('+inf')

    @property
    def links(self):
        return self._links

    def __hash__(self):
        return hash(id(self))


class Link:

    def __init__(self, v1: Vertex, v2: Vertex):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def __eq__(self, other):
        return (self.v1, self.v2) == (other.v1, other.v2) or (self.v2, self.v1) == (other.v1, other.v2)


class LinkedGraph:

    def __init__(self):
        self._links = []  # list of links
        self._vertex = []  # list of vertexes

    def add_vertex(self, v: Vertex) -> None:
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link) -> None:
        t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2)) or
                                   (id(x.v2) == id(link.v1) and id(x.v1) == id(link.v2)),
                         self._links)
                  )
        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def find_path(self, start_v: Vertex, stop_v: Vertex):
        self.__clear_weight()
        start_v.min_weight = 0
        used_vertex = {start_v}
        processed_vertex = [start_v]
        while len(used_vertex) != len(self._vertex):
            curr_vertex = processed_vertex.pop(0)
            processed_links = curr_vertex.links
            for link in processed_links:
                end_vertex = link.v1 if link.v1 != curr_vertex else link.v2
                if end_vertex in used_vertex:
                    continue
                end_vertex.min_weight = min(end_vertex.min_weight, curr_vertex.min_weight + link.dist)
                if end_vertex not in processed_vertex:
                    processed_vertex.append(end_vertex)
                    processed_vertex.sort(key=lambda x: x.min_weight)
            used_vertex.add(curr_vertex)
            if curr_vertex is stop_v:
                break

        return self.__get_vertex_and_links(start_v, stop_v)

    @staticmethod
    def __get_vertex_and_links(start_v, stop_v):
        curr_vertex = stop_v
        min_path_vertex = [stop_v]
        min_path_links = []
        while curr_vertex != start_v:
            processed_links = curr_vertex.links
            for link in processed_links:
                end_v = link.v1 if link.v1 != curr_vertex else link.v2
                if curr_vertex.min_weight - link.dist == end_v.min_weight:
                    min_path_vertex.append(end_v)
                    min_path_links.append(link)
                    curr_vertex = end_v
                    break
        return min_path_vertex[::-1], min_path_links[::-1]

    def __clear_weight(self):
        for vertex in self._vertex:
            vertex.min_weight = float("+inf")


class Station(Vertex):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):

    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist
