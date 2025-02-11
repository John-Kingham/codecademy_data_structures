class MaxHeap:
    """
    A max-heap.
    """

    ROOT_INDEX = 1

    def __init__(self):
        self.heap_list = [
            None
        ]  # None is a sentinel element that simplifies other methods
        self.count = 0

    def parent_index(self, child_index):
        """
        Gets the parent index of a child index.

        Parameters
        ----------
        child_index : int
            The child index.

        Returns
        -------
        int
            The parent index.
        """
        return child_index // 2

    def left_child_index(self, parent_index):
        """
        Gets the left child index of a parent index.

        Parameters
        ----------
        parent_index : int
            The parent index.

        Returns
        -------
        int
            The left child index.
        """
        return parent_index * 2

    def right_child_index(self, parent_index):
        """
        Gets the left child index of a parent index.

        Parameters
        ----------
        parent_index : int
            The parent index.

        Returns
        -------
        int
            The left child index.
        """
        return parent_index * 2 + 1

    def parent_has_child(self, parent_index):
        """
        Does a parent node have any child nodes?

        Parameters
        ----------
        parent_index : int
            The index of the parent node.

        Returns
        -------
        bool
            Whether the parent has any children. 
        """
        return self.left_child_index(parent_index) <= self.count

    def largest_child_index(self, parent_index):
        """
        Returns the index of the largest child.

        Parameters
        ----------
        parent_index : int
            The index of the parent node.

        Returns
        -------
        int
            The index of the child node with the highest value
        """
        right_child_index = self.right_child_index(parent_index)
        if right_child_index > self.count:
            return self.left_child_index(parent_index)
        right_child = self.heap_list[right_child_index]
        left_child_index = self.left_child_index(parent_index)
        left_child = self.heap_list[left_child_index]
        if right_child >= left_child:
            return right_child_index
        else:
            return left_child_index

    def heapify_up(self):
        """
        Moves a newly added node up the heap until the max-heap rules are satisfied.

        Recursively swaps a child node with its parent if the child is greater than the parent.
        """
        current_index = self.count
        parent_exists = True
        while parent_exists:
            parent_index = self.parent_index(current_index)
            if parent_index == 0:
                parent_exists = False
                continue
            current_value = self.heap_list[current_index]
            parent_value = self.heap_list[parent_index]
            if current_value <= parent_value:
                break
            self.heap_list[parent_index] = current_value
            self.heap_list[current_index] = parent_value
            current_index = parent_index

    def heapify_down(self):
        """
        Moves a newly added root node down the heap until the max-heap rules are satisfied.

        Starting from the root, recursively swaps a parent node with its highest-value child if the parent has a lower value.
        """
        if self.count <= 1:
            return
        parent_index = MaxHeap.ROOT_INDEX
        parent = self.heap_list[parent_index]
        larger_child_exists = True
        while larger_child_exists:
            if not self.parent_has_child(parent_index):
                larger_child_exists = False
                continue
            largest_child_index = self.largest_child_index(parent_index)
            largest_child = self.heap_list[largest_child_index]
            if parent >= largest_child:
                larger_child_exists = False
                continue
            self.heap_list[parent_index] = largest_child
            self.heap_list[largest_child_index] = parent
            parent_index = largest_child_index

    def add(self, node):
        """
        Adds a node to the heap using max-heap rules.

        Parameters
        ----------
        node : A comparable object
        """
        self.heap_list.append(node)
        self.count += 1
        self.heapify_up()

    def extract_max(self):
        """
        Pops the maximum (root) node from the heap and reheapifies.

        Returns
        -------
        object
            The maximum (root) node
        None
            If there are no nodes in the heap.
        """
        if self.count == 0:
            return None
        old_root = self.heap_list[MaxHeap.ROOT_INDEX]
        self.heap_list[MaxHeap.ROOT_INDEX] = self.heap_list[self.count]
        self.heap_list[self.count] = old_root
        self.heap_list.pop()
        self.count -= 1
        self.heapify_down()
        return old_root
