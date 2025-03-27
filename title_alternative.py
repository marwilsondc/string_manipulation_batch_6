#define title_alt(str)
def title_alt(str):

    #within function, initialize is_separated = True and final_result
    is_separated = True
    final_result = ""

    #create for loop to iterate through str
    for i in str:

        #within for loop, create if statement that evaluates whether iteration is alpha
        if i.isalpha():

            #within if statement, create another if statement that evaluates whether is_separated is True
            if is_separated:

                #if above statement is True, add iteration to final_result in uppercase and set is_separated to False
                final_result += i.upper()
                is_separated = False

            #within if statement, continue to else statement for when is_separated is False
            else: 

                #if above statemnt is True, add iteration to final_result in lowercase
                final_result += i.lower()

        #else is for characters outside alpha, including numbers, whitespaces, and symbols
        else:

            #if above statement is True, set is_separated to True
            is_separated = True