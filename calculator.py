
from arithmetic import *

def format_input():
    """ Collects user's raw input and returns it as a list."""

    original_input = raw_input("> ")
    original_input = original_input.strip()
    formatted_input = original_input.split(" ")
    return formatted_input



def convert_tokens_to_int(user_input):
    """Converts digits in list to integers; appends all elements to a new list.

    Returns None if user input is invalid."""

    new_user_input = []
    for item in user_input:
        if item == '':
            continue
        elif item.isdigit():
            item = int(item)
            new_user_input.append(item)
        else:
            print "Your input is invalid. Please try again."
            return None
    if len(new_user_input) > 2:
        print "You entered too many numbers. Please try again"
        return None
    return new_user_input



 
def calculator():
    """ Takes user input, calculates arithmetic functions."""

    while True:
        split_list = format_input() 
        first_token = split_list.pop(0)
        tokens = convert_tokens_to_int(split_list)
        if tokens == None:
            continue
        # If user enters 'q', quit program.
        if first_token == 'q' or first_token == 'Q':
            break
        # Otherwise calculate user input. 
        elif first_token == '+':
            print add(num1=tokens[0], num2=tokens[1])
        elif first_token == '-':
            print subtract(num1=tokens[0], num2=tokens[1])
        elif first_token == '*':
            print multiply(num1=tokens[0], num2=tokens[1])
        elif first_token == '/':
            print divide(num1=tokens[0], num2=tokens[1])
        elif first_token == 'square':
            print square(num1=tokens[0])
        elif first_token == 'cube':
            print cube(num1=tokens[0])
        elif first_token == 'pow':
            print pow(num1=tokens[0], num2=tokens[1])
        elif first_token == 'mod':
            print mod(num1=tokens[0], num2=tokens[1])
        else:
            print "error: do not understand input"
            continue 


calculator()
