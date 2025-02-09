from collections import deque


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
        self.children = []

    def add_child(self, child):
        """
        Add a child node.

        Parameters
        ----------
        child : TreeNode
            A child node to add to this parent node.
        """
        self.children.append(child)

    def remove_child(self, child):
        """
        Removes the child node, if it exists.

        Parameters
        ----------
        child : TreeNode
            The child node to be removed.
        """
        self.children = [c for c in self.children if c.value != child.value]

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
            nodes_to_traverse += current_node.children
        return values_string[:-3]

    def __str__(self):
        """
        Returns a graphical representation of the tree from this node down.

        Returns
        -------
        string
            A graphical representation of the tree from this node down.

        Examples
        --------
        Home
        |-Documents
        | |-WishList.txt
        | |-TodoList.txt
        |-Photos
        | |-Fluffy.jpg
        """
        stack = deque()
        stack.append([self, 0])
        level_str = "\n"
        while len(stack) > 0:
            node, level = stack.pop()
            if level > 0:
                level_str += "| " * (level - 1) + "|-"
            level_str += str(node.value) + "\n"
            level += 1
            for child in reversed(node.children):
                stack.append([child, level])
        return level_str

alice = TreeNode("Alice")
bob = TreeNode("Bob")
colin = TreeNode("Colin")
alice.add_child(bob)
alice.add_child(colin)
print(alice)