def bsr(sorted_list, left_pointer, right_pointer, target):
    """
    A recursive binary search.

    Parameters
    ----------
    sorted_list : list
        A sorted list of zero or more items
    left_pointer : int
        The leftmost index of the portion of the list to search.
    right_pointer : int
        The rightmost index of the portion of the list to search.
    target : object
        The list item being searched for.

    Returns
    -------
    int
        The index of the target object.
    None
        If the target object isn't in the list. 
    """
    list_empty = left_pointer >= right_pointer
    if list_empty:
        return None
    mid_index = (left_pointer + right_pointer) // 2
    mid_item = sorted_list[mid_index]
    if mid_item == target:
        return mid_index
    elif mid_item > target:
        return bsr(sorted_list, left_pointer, mid_index, target)
    else:
        return bsr(sorted_list, mid_index + 1, right_pointer, target)
