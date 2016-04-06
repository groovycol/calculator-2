
from arithmetic import *


def convert_tokens_to_int(user_input):
    """
    converts digits in list to integers

    leaves all other elements as strings; appends all elements to a new list.
    """
    new_user_input = []
    for word in user_input:
        if word.isdigit():
            word = int(word)
            new_user_input.append(word)
        else:
            new_user_input.append(word)
    return new_user_input



# repeat forever:
while True:
    #     read input
    input = raw_input("> ")
    #     tokenize input
    split_list = input.split(" ")
    #change token elements 1-n to integers
    tokens = convert_tokens_to_int(split_list)
    #     if the first token is 'q', quit
    if tokens[0] == 'q' or tokens[0] == 'Q':
        break
    #     otherwise decide which math function to call based on the tokens we read
    elif tokens[0] == '+':
        result = add(num1=tokens[1], num2=tokens[2])
        print result
    elif tokens[0] == '-':
        result = subtract(tokens[1], tokens[2])
        print result
    elif tokens[0] == '*':
        result = multiply(tokens[1], tokens[2])
        print result
    elif tokens[0] == '/':
        result = divide(tokens[1], tokens[2])
        print result
    elif tokens[0] == 'square':
        result = square(tokens[1])
        print result
    elif tokens[0] == 'cube':
        result = cube(tokens[1])
        print result
    elif tokens[0] == 'pow':
        result = pow(tokens[1], tokens[2])
        print result
    elif tokens[0] == 'mod':
        result = mod(tokens[1], tokens[2])
        print result
    else:
        print "error: do not understand input"
        break 
