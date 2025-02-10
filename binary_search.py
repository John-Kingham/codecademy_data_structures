def binary_search_recursive(sorted_list, left_pointer, right_pointer, target):
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
        return binary_search_recursive(sorted_list, left_pointer, mid_index, target)
    else:
        return binary_search_recursive(sorted_list, mid_index + 1, right_pointer, target)


def binary_search_iterative(sorted_list, target):
    """
    An iterative binary search.

    Parameters
    ----------
    sorted_list : list
        A sorted list to search.
    target : int
        The number to search for.

    Returns
    -------
    int
        The index of target.
    None
        If target isn't found.
    """
    left_pointer = 0
    right_pointer = len(sorted_list)
    while left_pointer < right_pointer:
        mid_index = (left_pointer + right_pointer) // 2
        mid_value = sorted_list[mid_index]
        if mid_value == target:
            return mid_index
        if target < mid_value:
            right_pointer = mid_index
        if target > mid_value:
            left_pointer = mid_index + 1
    return None
