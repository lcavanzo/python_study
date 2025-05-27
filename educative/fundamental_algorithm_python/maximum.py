def maximum_index(lst):
    """
    function finds the maximum element’s index in the list
    :param lst: A list of integers
    :return: Index of maximum element if exists otherwise -1
    """

    # initialize index to 0
    max_index = -1

    # set max value to least number
    max_val = -99999  # INT_MIN

    # loop through each element in list
    for i in range(len(lst)):
        if max_val < lst[i]:
            max_val = lst[i]
            max_index = i

    return max_index


# Driver code to test above
if __name__ == "__main__":

    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]

    max = maximum_index(nums)
    print("Maximum number in the list is", nums[max], "at index ", max)
