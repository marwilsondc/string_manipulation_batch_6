#ask user to enter their full name with several spaces in the beginning, store in variable
user_string = input("Input your full name with several spaces before it: ")

#create a for loop that iterates through the user_string
for i in user_string:
    
    #create an if statement that evaluates whether iteration is a whitespace
    if i.isspace(): 

        #within if statement, replace whitespace into nothing or ""
        new_string = user_string.replace(i, "")

    #else, break the whole for loop
    else:
        break

print(new_string)