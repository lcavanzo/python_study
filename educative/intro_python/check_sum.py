def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num + 1, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False


s1 = [10, -14, 26, 5, -3, 13, -5]
s2 = [10, -14, 26, 5, -2]
s3 = [5, 10, -14, 26, 5, -3, 13, -5, 5]
print(check_sum(s1))
print(check_sum(s2))
print(check_sum(s3))
