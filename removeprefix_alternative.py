#ask user to input a string, contain in a variable
user_string = input("input a string: ")

#ask the user for the prefix that they want to remove, contain in a variable
user_prefix = input("what is the prefix you want removed?: ")

#initialize terminate_flag 
terminate_flag = True

#initialize index_count
index_count = 0 

#initialize compare_prefix
compare_prefix = ""

#create a for loop to iterate through user_string
for i in user_string: 

    #within for loop, create if statement to compare iteration and user_string index to user_prefix
    #Index Error
    if i and user_string[index_count] == user_prefix[index_count]:

        #if true, add the character to compare_prefix and add 1 to index_count
        compare_prefix += i
        index_count += 1

        #if compare_prefix equals user_prefix, replace compare_prefix with "" then print result
        if compare_prefix == user_prefix:
            user_string = user_prefix.replace(compare_prefix, "")
            print(user_prefix)

    #else, set terminate_flag to false and break
    else:
        terminate_flag = False
        break