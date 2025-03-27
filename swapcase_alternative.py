#ask user to input a string to use swapcase on, store in user_string
user_string = input("input a string: ")

#initialize index_count
index_count = 0

final_result = ""
#create a for loop to iterate through user_string
for i in user_string:

    #elif, evaluate if iteration is lowercase, if true, convert user_string[index_count] to uppercase and add 1 to index_count
    if i.islower():
        final_result += user_string[index_count].upper()
        index_count += 1
        continue

    #elif, evaluate if iteration is uppercase, if true, convert user_string[index_count] to lowercase and add 1 to index_count
    elif i.isupper():
        final_result += user_string[index_count].lower()
        index_count += 1
        continue
    
    else:
        index_count += 1
        final_result += i
        continue

#print user_string
print(final_result)