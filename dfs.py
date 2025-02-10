from tree import TreeNode


def dfs(root, value, path=()):
    """
    Depth-first search.

    A depth-first search using recursive calls.

    Parameters
    ----------
    root : TreeNode
        The root of the tree to search.
    value : object
        The node value to search for.
    path : a tuple of TreeNodes
        The path to this node's parent, with the root as the first item.
        Defaults to an empty tuple.
        
    Returns
    -------
    Tuple
        A tuple of TreeNodes, representing the path from root to value's node
    None
        If value isn't found. 
    """
    path = path + (root,)
    if root.value == value:
        return path
    for child in root.children:
        found_path = dfs(child, value, path)
        if found_path:
            return found_path
    return None
