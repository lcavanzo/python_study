# multiplication_quiz-no-lib.py - A simple multiplication quiz
"""
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project
on your own without importing it.
This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9.
You’ll need to implement the following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves
on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the
next question.
Eight seconds after first displaying the question, the question is marked as incorrect even
if the user enters the correct answer after the 8-second limit.
"""

import random
import re
import time


# define Python user-defined exceptions
class TimeoutException(Exception):
    "Raised when the user waits more than 5 secs to put a value"


class RetryLimitExceptions(Exception):
    "Raised when the user fails more than 3 times"


number_of_questions = 10
correct_answers = 0


for question in range(number_of_questions):
    # Generate random values for the questions
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    # get the result
    answer = num1 * num2
    # Create regex to catch only numbers
    regex = r"^[0-9]+$"

    tries = 0
    flag = True

    try:
        # While the answer is incorrect, it keeps asking for the input 3 times
        while flag:
            # watch the init time
            start = time.time()
            response = input(f"\n#{question+1}: {num1} X {num2} >>> ")

            # validating answer to only numbers
            if re.match(regex, response):
                response = int(response)
            else:
                print("Input is not a valid number.")

            # watch the finish time
            end = time.time()
            total_time = end - start
            # if the response is correct, then we break the loop
            if response == answer:
                flag = False
            # raising exceptions
            if total_time > 10:
                raise TimeoutException
            if response != answer:
                tries += 1
            if tries == 3:
                raise RetryLimitExceptions

    except TimeoutException:
        print("Exception occurred: Out of time ")
    except RetryLimitExceptions:
        print("Exception occurred: Out of tries")
    else:
        print("Correct")
        correct_answers += 1
    print(f"Score {correct_answers/number_of_questions}")
