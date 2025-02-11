class HeapMap:
    """
    A heap map.
    """
    def __init__(self):
        self.heap_list = [None] # None is a sentinel element that simplifies other methods
        self.count = 0

    def parent_index(self, index):
        """
        Calculates the parent index of a child index.

        Parameters
        ----------
        index : int
            The child index.

        Returns
        -------
        int
            The parent index.
        """
        return index // 2
    
    def left_child_index(self, index):
        """
        Calculates the left child index of a parent index.

        Parameters
        ----------
        index : int
            The parent index.

        Returns
        -------
        int
            The left child index.
        """
        return index * 2
    
    def right_child_index(self, index):
        """
        Calculates the left child index of a parent index.

        Parameters
        ----------
        index : int
            The parent index.

        Returns
        -------
        int
            The left child index.
        """
        return index * 2 + 1
    
    def heapify_up(self):
        """
        Moves a newly added element up the heap until the max-heap rules are satisfied.

        Recursively swaps a child element with its parent if the child's value is greater than the parent's.
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

    def add(self, value):
        """
        Adds a value to the heap using max-heap rules.

        Parameters
        ----------
        value : int, float
        """
        self.heap_list.append(value)
        self.count += 1
        self.heapify_up()

