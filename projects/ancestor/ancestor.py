from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # instatiate graph
    gr = Graph()
    # loop through ancestors to populate graph
    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        # add vertex for parent
        gr.add_vertex(parent)
        # add vertex for child
        gr.add_vertex(child)
        # add edges from child to parent
        gr.add_edge(child, parent)
    # get the ancestor for the given starting_node
    return gr.get_ancestor(starting_node)
