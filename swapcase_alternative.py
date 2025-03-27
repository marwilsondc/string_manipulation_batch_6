#ask user to input a string to use swapcase on, store in user_string
user_string = input("input a string: ")

#initialize index_count
index_count = 0

#create a for loop to iterate through user_string
for i in user_string:

    #within for loop, create if statement to evaluate if iteration is a space. If True, continue iteration
    if i.isspace():
        continue

    #elif, evaluate if iteration is lowercase, if true, convert user_string[index_count] to uppercase and add 1 to index_count
    elif i.islower():
        user_string = user_string[index_count].upper()
        index_count += 1

    #elif, evaluate if iteration is uppercase, if true, convert user_string[index_count] to lowercase and add 1 to index_count
    elif i.isupper():
        user_string = user_string[index_count].lower()
        index_count += 1

#print user_string
print(user_string)