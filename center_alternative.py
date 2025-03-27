#define center_alt(str, len, char = " ")
#within function, initialize alternator = True, left_padding = "", and right_padding = ""
#then create a for loop iterating through range(len - len(str))
#then create an if statement, if alternator is True, add char to left_padding and set alternator to False
#if alternator is False, add char to right_padding and set alternator to True
#outside for loop, combine left_padding + str + right_padding, store in result
#return result
