"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if not self.vertices.get(vertex_id):
            # add vertex to vertices as an empty set if it doesn't exist alread
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph if both currently exist in verticies.
        """
        if v1 in self.vertices and v2 in self.vertices:
            # add edge if both vertices exist
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Not Found')

    def get_ancestor(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # check if starting vertex exists
        if self.vertices.get(starting_vertex) == set():
            # return -1 if not
            return -1
        # instantiate stack
        s = Stack()
        # instantiate visited
        already = set()
        # add starting_vertex to stack
        s.push(starting_vertex)
        # track current vertex
        current = starting_vertex
        # loop through stack
        while s.size():
            # pop from stack
            now = s.pop()
            # check if popped vertex has been visited
            if now not in already:
                if s.size() and self.vertices.get(now) == set():
                    # pop another off of the stack if not empty and popped vertex is empty
                    now2 = s.pop()
                    if now2 < now:
                        # use the smaller of the popped vertices
                        now = now2
                # add popped vertex to visted
                already.add(now)
                # change current vertex to popped vertex
                current = now
            # loop through edges of popped vertex
            for v in self.vertices[now]:
                # add each edge to stack if not visited already
                if v not in already:
                    s.push(v)
        # return current vertex
        return current
