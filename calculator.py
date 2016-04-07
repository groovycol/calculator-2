
from arithmetic import *

def format_input():
    """
    Converts user's raw input to a list of strings.

    """
    original_input = raw_input("> ")
    original_input = original_input.strip()
    formatted_input = original_input.split(" ")
    return formatted_input



def convert_tokens_to_int(user_input):
    """
    converts digits in list to integers

    leaves all other elements as strings; appends all elements to a new list.
    """
    new_user_input = []
    for item in user_input:
        if item == '':
            pass
        elif item.isdigit():
            item = int(item)
            new_user_input.append(item)
        else:
            print "Your input is invalid. Please try again."
            return None
    return new_user_input





# repeat forever:
while True:
    split_list = format_input() 
    first_token = split_list.pop(0)
    #change token elements 1-n to integers
    tokens = convert_tokens_to_int(split_list)
    if tokens == None:
        continue
    elif len(tokens) > 2:
        print "You entered too many numbers. Please try again"
        continue
    #print tokens
    #     if the first token is 'q', quit
    if first_token == 'q' or first_token == 'Q':
        break
    #     otherwise decide which math function to call based on the tokens we read
    elif first_token == '+':
        #validate_ints(2, tokens)
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
        #validate_ints(1, tokens)
        print cube(num1=tokens[0])
    elif first_token == 'pow':
        print pow(num1=tokens[0], num2=tokens[1])
    elif first_token == 'mod':
        print mod(num1=tokens[0], num2=tokens[1])
    else:
        print "error: do not understand input"
        continue 
