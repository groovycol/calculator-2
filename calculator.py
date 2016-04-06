"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def convert_tokens_to_int(user_input):
    """
    converts user input 1-n elements to integers

    leaves the 0th element as a str
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
    new_list = input.split(" ")
    #change token elements 1-n to integers
    token = convert_tokens_to_int(new_list)
    #     if the first token is 'q', quit
    if token[0] == 'q' or token[0] == 'Q':
        break
    #     otherwise decide which math function to call based on the tokens we read
    elif token[0] == '+':
        result = add(num1=token[1], num2=token[2])
        print result
    elif token[0] == '-':
        result = subtract(token[1], token[2])
        print result
    elif token[0] == '*':
        result = multiply(token[1], token[2])
        print result
    elif token[0] == '/':
        result = divide(token[1], token[2])
        print result
    elif token[0] == 'square':
        result = square(token[1])
        print result
    elif token[0] == 'cube':
        result = cube(token[1])
        print result
    elif token[0] == 'pow':
        result = pow(token[1], token[2])
        print result
    elif token[0] == 'mod':
        result = mod(token[1], token[2])
        print result
    else:
        print "error: do not understand input"
        break 
