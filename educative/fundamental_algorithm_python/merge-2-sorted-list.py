# Merge 2 sorted list
"""
Merge Two Sorted Lists

Try to solve the Merge Two Sorted Lists problem.
Statement

Given two integer lists, nums1 and nums2, of size mm and nn, respectively, sorted in nondecreasing order. Merge nums1 and nums2 into a single list sorted in nondecreasing order.
"""


def merged_list(n1, n2):
    new_list = []
    p1 = 0
    p2 = 0
    p3 = 0
    while True:
        print(f"p1:{p1}, p2:{p2}, p3:{p3}")
        print(f"new_List: {new_list}\n")
        if n1[p1] < n2[p2]:
            new_list.insert(p3, n1[p1])
            p1 += 1
        elif n1[p1] > n2[p2]:
            new_list.insert(p3, n2[p2])
            p2 += 1
        else:
            break
        p3 += 1


nums1 = [1, 3, 4, 5]
nums2 = [2, 6, 7, 8]

print(merged_list(nums1, nums2))
