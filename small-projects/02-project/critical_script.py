import os
def do_something_important():
    print('Performing critical operation...')
    # Simulate a critical operation
    with open('operation_log.txt', 'a') as log_f:
        log_f.write('Critical operation performed.\n')
if __name__ == '__main__':
    do_something_important()

# Added a comment later