"""
Requirements
------------
Write depth-first and breadth-first graph searches.

Architecture
------------
Written in Python as functions. Run from the terminal.

System-level design
-------------------
As outlined in the architecture.

Module-level design
-------------------
One module for the functions. One module for unit testing.
"""


def dfs(graph, current_vertex, target_value, visited=None):
    """
    A depth-first graph search.

    Parameters
    ----------
    graph : dict
        - Key (str): A vertex's value.
        - Value (set of str): The set of neighbouring vertices.
    current_vertex : str
        The value of the current vertex.
    target_value : str
        The value of the target vertex.
    visited : set of str
        Previously visited vertices (defaults to None).

    Returns
    -------
    None
        If the target isn't found.
    List (of str)
        The path to the target. Each string is a vertex's value.
    """
    if visited is None:
        visited = []
    visited.append(current_vertex)
    if current_vertex == target_value:
        return visited
    for neighbour in graph[current_vertex]:
        if neighbour not in visited:
            path = dfs(graph, neighbour, target_value, visited)
            if path:
                return path
    return None


def bfs(graph, start_vertex, target_vertex):
    """
    A breadth-first graph search.

    Parameters
    ----------
    graph : dict
        - Key (str): A vertex's value.
        - Value (set of str): The set of neighbouring vertices.
    start_vertex : str
        The value of the starting vertex.
    target_value : str
        The value of the target vertex.

    Returns
    -------
    None
        If the target isn't found.
    List (of str)
        The path to the target. Each string is a vertex's value.
    """
    bfs_queue = [[start_vertex, [start_vertex]]]
    visited = set()
    while bfs_queue:
        vertex, path = bfs_queue.pop(0)
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if neighbour == target_vertex:
                    return path + [neighbour]
                else:
                    bfs_queue.append([neighbour, path + [neighbour]])
