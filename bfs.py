from collections import deque
from tree import TreeNode

def bfs(root_node, search_value):
    """
    A breadth-first search function.

    Uses the breadth-first process to search a tree for a given value.

    Parameters
    ----------
    root_node : TreeNode
        The root of the tree to search
    search_value : Object
        The value to search for

    Returns
    -------
    list
        The path from root to the node containing the value.
        The root is at index 0 and the target node is at index -1.
    None
        If the value isn't in the tree.
    """
    paths_to_search = deque()
    root_path = [root_node]
    paths_to_search.appendleft(root_path)
    while len(paths_to_search) > 0:
        path = paths_to_search.pop()
        node = path[-1]
        print(f"Searching node with value: {node.value}")
        if node.value == search_value:
            return path
        for child in node.children:
            child_path = path[:]
            child_path.append(child)
            paths_to_search.appendleft(child_path)
    NOT_FOUND = None
    return NOT_FOUND