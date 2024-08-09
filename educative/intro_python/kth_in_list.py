"""
Exercise: Kth Maximum Integer in a List

Given a list of integers and a number k, find the kth largest integer in the list.
The integer will be stored in the kth_max variable.

For example, with a list of 7 integers, if k = 2, then kth_max will be equal to the
second-largest integer in the list.
If k = 6, kth_max will equal the 6th largest integer.

[40, 35, 82, 14, 22, 66, 53]
k =2 -> kth_max = 66
k =6 -> kth_max = 22
"""

test_list = [40, 35, 82, 14, 22, 66, 53]
k = 2
# test_list and variable k are already given
# Write your code here

def k_integer(kth, k_list):
    ordered_list = sorted(k_list)
    kth_max = ordered_list[-kth]
    return kth_max


print(k_integer(k, test_list))
