
from arithmetic import *


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
            new_user_input.append(item)
    return new_user_input

# #def validate_ints( num_ints_needed, lst):
#     if num_ints_needed ==1
#         if token[0] is not an int
#         throw error
#     elif num_ints_needed == 2
#         if token[0] not an int or if token[2[]]



# repeat forever:
while True:
    #     read input
    original_input = raw_input("> ")
    #print original_input
    #remove leading and trailing spaces
    original_input = original_input.strip()
    #print original_input 
    #     tokenize input
    split_list = original_input.split(" ")
    #print split_list
    #Remove first element from list, assign to new variable. 
    first_token = split_list.pop(0)
    #change token elements 1-n to integers
    tokens = convert_tokens_to_int(split_list)
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
