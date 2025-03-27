#define ljust_alt(str, val)
def ljust_alt(str, val):

    #create while loop that runs until the length of str reaches val
    while len(str) < val:

        #within while loop, add " " or whitespace to str
        str += " "

    #outside while loop, return str
    return str

#tester
user_string = input("input a string = ")
other_text = "whitespace ends before this text."

print(ljust_alt(user_string, 20) + other_text)