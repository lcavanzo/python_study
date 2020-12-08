from datetime import datetime
import time
import random

odds = [number for number in range(1,60,2)]



for _ in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("this minute seems a little odd.")
    else:
        print("Not an odd minute.")
    time.sleep(random.randint(1,60))
