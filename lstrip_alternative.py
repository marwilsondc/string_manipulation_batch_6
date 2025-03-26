#ask user to enter their full name with several spaces in the beginning, store in variable
user_string = input("Input your full name with several spaces before it: ")

#initialize alpha_flag
alpha_flag = True

#create a for loop that iterates through the user_string
for i in user_string:
    
    #create an if statement that evaluates whether iteration is a whitespace
    if i.isspace() and alpha_flag: 

        #within if statement, replace whitespace into nothing or ""
        user_string = user_string.replace(i, "", 1)

    #else, break the whole for loop
    else:
        alpha_flag = False
        break

print(user_string)