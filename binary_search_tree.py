class BinarySearchTree:
    """
    A binary search tree.
    """

    def __init__(self, value, depth=1):
        """
        Parameters
        ----------
        value : int
            This node's value
        depth : int
            The depth of this node in the tree.
            Defaults to 1.
        """        
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def depth_first_in_order_traversal(self):
        """
        Traverses the tree using depth-first in-order.

        Returns
        -------
        string
            A description of the depth and value of each node.
        """
        traversal_string = ""
        if self.left:
            traversal_string += self.left.depth_first_in_order_traversal()
        traversal_string += f"D={self.depth},V={self.value}\n"
        if self.right:
            traversal_string += self.right.depth_first_in_order_traversal()      
        return traversal_string

    def insert(self, value):
        """
        Inserts a value into the tree.

        Parameters
        ----------
        value : int, float
            The value to insert.
            Equal values are inserted on the right.
        """
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value, self.depth + 1)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value, self.depth + 1)

    def get_node_by_value(self, value):
        """
        Finds a node by its value.

        Parameters
        ----------
        value : int, float
            The value to search for.

        Returns
        -------
        BinarySearchTree
            A node from the tree with a matching value.
        None
            If value isn't found.
        """
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.get_node_by_value(value)
        elif value > self.value and self.right:
            return self.right.get_node_by_value(value)
        else:
            return None
        
