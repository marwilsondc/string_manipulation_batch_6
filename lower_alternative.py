#ask user to input a string, contain in user_string
user_string = input("input a string: ")

#create a for loop that iterates through user_string
for i in user_string:

    #within for loop, create if statement that evaluates whether a character is upper case
    if i.isupper():

        #if True, use replace() to convert character to lower along with swapcase()
        user_string = user_string.replace(i, i.swapcase())

    #else, continue iteration
    else:
        continue

#after iteration, print(user_string)
print(user_string)