#ask user to input a string to be evaluated, contain in user_string
user_string = input("input a string to evaluate: ")

#initialize return_bool
return_bool = True

#create a for loop to iterate through user_string 
for i in user_string:

    #within for loop, create if statement of return_bool
    if return_bool:

        #within initial if statement, create if statement to evaluate whether iteration is uppercase 
        if i == i.upper():

            #if True, continue iteration
            continue

        #else, set return_bool to False and print return_bool and break
        else:
            return_bool = False
            print(return_bool)
            break

#if for loop iterates throughout user_string, print return_bool (display True)
if return_bool:
    print(return_bool)

