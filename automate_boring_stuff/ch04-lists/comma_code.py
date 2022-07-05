# write a function that takes a list value as argument and return a string 
## with al the items separated by comma and a space, with 'and' inserted before
## the last item

# Example
# [apples, bananas, tofu, cats] -> apples, bananas, tofu, and cats

def comma_separate(item_list):
    for index,item in enumerate(item_list):
        if item == item_list[-1]:
            print(f"and {item}")
        if item == item_list[-1]:
            continue
        print(f"{item}, ", end='')
    print()



items = [
    ['apples', 'bananas', 'tofu', 'cats'],
    ['linux', 'docker', 'bash', 'k8s', 'arch', 'python', 'go'], 
    ['messi', 'ronaldo', 'cristiano', 'xabi', 'iniesta', 'buffon', 'kante'],
]

for item in items:
    comma_separate(item)
