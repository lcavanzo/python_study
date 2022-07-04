import time, sys
indent = 0 # How many spaces to indent
indent_increasing = True # Wheter the intdentatino is increasing or not

try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indent_increasing:
            # INcreaase the number of spaces:
            indent = indent + 1
            if indent == 30:
                # Change direction:
                indent_increasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # change direction
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
