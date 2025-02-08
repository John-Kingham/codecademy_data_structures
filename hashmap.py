class HashMap:
    """
    A hashmap.

    Stores values that are accessible with a key. For example, the
    key of "Joe Blogs" might be mapped to the value "42".
    """

    def __init__(self, size):
        """
        Parameters
        ----------
        size: int
            The maximum number of key-value pairs the hashmap can store.
        """
        self.__size = size
        self.__array = [None for i in range(size)]

    def __get_hash(self, key, collisions):
        hash_code = sum(key.encode()) + collisions
        return hash_code % self.__size

    def assign(self, key, value):
        """
        Adds or updates a key-value pair.

        Parameters
        ----------
        key: String
            A key that can be used to update and retrieve value.
        value: Object
            An object associated with the key.

        Returns
        -------
        None
            If the value is added or updated.
        int
            Returns 1 if the value couldn't be stored because the hashmap was full.
        """
        num_collisions = 0
        while num_collisions < self.__size:
            index = self.__get_hash(key, num_collisions)
            if self.__array[index] is None or self.__array[index][0] == key:
                self.__array[index] = [key, value]
                return
            num_collisions += 1
        return 1

    def retrieve(self, key):
        """
        Retrieves the value associated with key.

        Parameters
        ----------
        key: String
            The key associated with the value.

        Returns
        -------
        None
            If the key wasn't found.
        Object
            The value associated with key, if the key was found.
        """
        num_collisions = 0
        while num_collisions < self.__size:
            index = self.__get_hash(key, num_collisions)
            if self.__array[index] is None:
                return None
            if self.__array[index][0] == key:
                return self.__array[index][1]
            num_collisions += 1
        return None
