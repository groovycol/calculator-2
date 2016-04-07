
from arithmetic import *


def convert_tokens_to_int(user_input):
    """
    converts digits in list to integers

    leaves all other elements as strings; appends all elements to a new list.
    """
    new_user_input = []
    for word in user_input:
        if word == '':
            pass
        #elif word[0] !=
        elif word.isdigit():
            word = int(word)
            new_user_input.append(word)
        else:
            new_user_input.append(word)
    return new_user_input

# #def validate_ints( num_ints_needed, lst):
#     if num_ints_needed ==1
#         if token[1] is not an int
#         throw error
#     elif num_ints_needed == 2
#         if token[1] not an int or if token[2[]]



# repeat forever:
while True:
    #     read input
    original_input = raw_input("> ")
    print original_input
    #remove leading and trailing spaces
    original_input = original_input.strip()
    print original_input 
    #     tokenize input
    split_list = original_input.split(" ")
    print split_list
    #change token elements 1-n to integers
    tokens = convert_tokens_to_int(split_list)
    print tokens
    #     if the first token is 'q', quit
    if tokens[0] == 'q' or tokens[0] == 'Q':
        break
    #     otherwise decide which math function to call based on the tokens we read
    elif tokens[0] == '+':
        #validate_ints(2, tokens)
        print add(num1=tokens[1], num2=tokens[2])
    elif tokens[0] == '-':
        print subtract(num1=tokens[1], num2=tokens[2])
    elif tokens[0] == '*':
        print multiply(num1=tokens[1], num2=tokens[2])
    elif tokens[0] == '/':
        print divide(num1=tokens[1], num2=tokens[2])
    elif tokens[0] == 'square':
        print square(num1=tokens[1])
    elif tokens[0] == 'cube':
        #validate_ints(1, tokens)
        print cube(num1=tokens[1])
    elif tokens[0] == 'pow':
        print pow(num1=tokens[1], num2=tokens[2])
    elif tokens[0] == 'mod':
        print mod(num1=tokens[1], num2=tokens[2])
    else:
        print "error: do not understand input"
        continue 
