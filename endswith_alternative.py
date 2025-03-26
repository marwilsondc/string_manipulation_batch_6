#ask user to input a string to be evaluated, contain in user_string
user_string = input("input a string to be evaluated: ")

#ask user to input the condition to evaluate string with, contain in endswith_eval
endswith_eval = input("input string to evaluate string with: ")

#initialize return_bool 
return_bool = True

#initialize comparator_string
comparator_string = ""

#create a for loop to iterate through user_string
for i in user_string:

    #within for loop, create if statement to evaluate whether iterations match endswith_eval
    if i in endswith_eval:

        #if True, add iteration to comparator_string
        comparator_string += i

        #within initial if statement, create another if statement that compares comparator_string with endswith_eval
        if comparator_string == endswith_eval:

            #if True, set return_bool to True
            return_bool = True

    #outside initial if statement, continue else statement
    else: 

        #if True, clear comparator_string and set return_bool to False
        comparator_string = ""
        return_bool = False

#outside for loop, print return_bool
print(return_bool)