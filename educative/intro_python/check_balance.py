# strings to check
b1 = "[[[[][]]]]"
b2 = "[][][][]"
b3 = "[[]]]]][["
b4 = "]["


def check_balance(brackets):
    # Write your code her
    brackets = list(brackets)
    balanced = False
    flag = True
    while flag:
        if len(brackets) == 0:
            balanced = True
            break
        elif brackets[0] == "]":
            balanced = False
            flag = False

        if brackets[0] == "[":
            del brackets[0]
            for closed_bracket in range(len(brackets)):
                if brackets[closed_bracket] == "]":
                    del brackets[closed_bracket]
                    break
    print(balanced)


check_balance(b1)
check_balance(b2)
check_balance(b3)
check_balance(b4)


# INFO: code well written
# def check_balance(brackets):
#     check = 0
#     for bracket in brackets:
#         if bracket == "[":
#             check += 1
#
#         elif bracket == "]":
#             check -= 1
#
#         if check < 0:
#             break
#
#     return check == 0
#
#
# print(check_balance(b1))
# print(check_balance(b2))
# print(check_balance(b3))
# print(check_balance(b4))
