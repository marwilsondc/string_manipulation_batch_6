#define capitalize_alt(str)
def capitalize_alt(str):

    #within function, initialize final_result, index_count
    final_result = ""
    index_count = 0

    #below initialization, create if statement that evaluates whether first iteration is part of the alphabet
    if str[0].isalpha():

        #within if statement, create for loop to iterate through string
        for i in str:

            #within for loop, create another if statement that evaluates whether index_count is 0
            if index_count == 0:

                #if above statement is True, add the iteration to final_result in uppercase and add 1 to index_count
                final_result += i.upper()
                index_count += 1

            #else, another if statement, evaluate whether iteration is alpha
            else:
                if i.isalpha():

                    #if true, add iteration to final_result in lowercase 
                    final_result += i.lower()

                #else, add iteration to final_result
                else:
                    final_result += i

        return final_result

    #else, return string itself
    else:
        return str
    
#tester
user_string = input("input a string: ")
print(capitalize_alt(user_string))