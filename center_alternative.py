#define center_alt(str, length, char = " ")
def center_alt(str, length, char = " "):

    #within function, initialize alternator = True, left_padding = "", and right_padding = ""
    alternator = True
    left_padding = ""
    right_padding = ""

    #subtract len(str) from len, store in pad_range
    pad_range = length - len(str)

    #then create a for loop iterating through range(len - len(str))
    for i in range(pad_range):

        #then create an if statement, if alternator is True, add char to left_padding and set alternator to False
        if alternator:
            left_padding += char
            alternator = False
            continue

        #if alternator is False, add char to right_padding and set alternator to True
        if alternator == False:
            right_padding += char
            alternator = True
            continue

    #outside for loop, combine left_padding + str + right_padding, store in result
    result = left_padding + str + right_padding

    #return result
    return result

#tester
user_string = input("input a string: ")
other_text = "whitespace ends here."

print(center_alt(user_string, 19, "0") + other_text)
print(center_alt(user_string, 19) + other_text)