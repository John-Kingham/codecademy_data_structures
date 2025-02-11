from max_heap import MaxHeap


def heapsort(unsorted_list):
    """
    Sorts a list with the help of a max-heap.

    Parameters
    ----------
    unsorted_list : A list of comparable objects.

    Returns
    -------
    list
        A new sorted list.
    """
    sorted_list = []
    max_heap = MaxHeap()
    for item in unsorted_list:
        max_heap.add(item)
    while max_heap.count > 0:
        sorted_list.insert(0, max_heap.extract_max())
    return sorted_list
