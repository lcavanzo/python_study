def minimum_index(lst):
    """
    This function finds the minimum element index in the list
    :param lst: A list of integers
    :return: Index of minimum element if it exists otherwise -1
    """

    # initialize index to 0
    min_index = -1

    # set min value to the large number
    min_val = 9999

    # loop through each element in list
    for i in range(len(lst)):
        if min_val > lst[i]:
            min_val = lst[i]
            min_index = i

    return min_index


# Driver code to test above
if __name__ == "__main__":

    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
    min = minimum_index(nums)

    print("Minimum number in the list is", nums[min], "at index ", min)
