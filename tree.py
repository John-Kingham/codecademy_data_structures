class TreeNode:
    """
    A tree node.

    A tree node has a value and is linked to zero or more child nodes.
    """

    def __init__(self, value):
        """
        Parameters
        ----------
        value : string
            The node's value as a string.
        """
        self.value = value
        self.__children = []

    def add_child(self, child):
        """
        Add a child node.

        Parameters
        ----------
        child : TreeNode
            A child node to add to this parent node.
        """
        self.__children.append(child)

    def remove_child(self, child):
        """
        Removes the child node, if it exists.

        Parameters
        ----------
        child : TreeNode
            The child node to be removed.
        """
        self.__children = [c for c in self.__children if c.value != child.value]

    def traverse(self):
        """
        Traverses the tree from this node down and returns a string of every node's value.

        Returns
        -------
        String
            The value of this node and all its descendent nodes recursively.
        """
        values_string = ""
        nodes_to_traverse = [self]
        while len(nodes_to_traverse) > 0:
            current_node = nodes_to_traverse.pop()
            values_string += current_node.value + " : "
            nodes_to_traverse += current_node.__children
        return values_string[:-3]