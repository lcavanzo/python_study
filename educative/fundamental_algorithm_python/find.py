def find_index(lst, key):
    """
    This function takes a list of integers and a key to find in the list
    :param lst: A list of integers
    :param key: A key to find in the list
    :return: Index of element if exists otherwise -1
    """

    # loop through each element in the list
    for i in range(len(lst)):
        # check if this is the element you want to find
        if lst[i] == key:
            # if found return its index
            return i

    return -1  # element not found, return -1


# Driver code to test above
if __name__ == "__main__":

    number_to_search = 7
    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]

    print("Number", number_to_search, "is at index", find_index(nums, number_to_search))
