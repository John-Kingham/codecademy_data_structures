from linked_list import Node, LinkedList


class Hashmap:
    """
    A hashmap that uses separate chaining to manage collisions.
    """
    
    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The size of the hashmap's array.
        """
        self.__size = size
        self.__array = [LinkedList() for i in range(size)]

    def __compressed_hash(self, key):
        """
        Returns a has compressed to fit within the hashmap's array.

        Parameters
        ----------
        key : string
            The key to be hashed

        Returns
        -------
        Int
            The compressed hash
        """
        return sum(key.encode()) % self.__size
    
    def assign(self, key, value):
        """
        Adds or updates the key-value pair.

        If the key is found, the related value is updated. If the key isn't found, the key-value pair are added to the array.

        Parameters
        ----------
        key : string
            A key that can be used to update and retrieve the value
        value : object
            The value  
        """
        linked_list = self.__array[self.__compressed_hash(key)]
        for key_value in linked_list:
            if key_value is not None and key_value[0] == key:
                key_value[1] = value
                return
        linked_list.insert_beginning([key, value])

    def retrieve(self, key):
        """
        Tries to retrieve the value associated with a key.

        Parameters
        ----------
        key : string
            The key whose associated value you want to retrieve.

        Returns
        -------
        Object
            If the key is found, the associated value is returned
        None
            If the key isn't found
        """
        linked_list = self.__array[self.__compressed_hash(key)]
        for key_value in linked_list:
            if key_value is not None and key_value[0] == key:
                return key_value[1]
        return None