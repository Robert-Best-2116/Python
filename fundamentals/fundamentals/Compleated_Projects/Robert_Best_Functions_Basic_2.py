# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
num= 5
list = []
def countdown(num):
    while num >= 0:
        list.append(num)
        num = num -1
        print(list)
    else:
        print(list)
        return(list)
        

countdown(num)  
#Example: countdown(5) should return [5,4,3,2,1,0]

#Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

values = [1, 2]

def print_recieve(values):
    for i in values:
        print(values[0])
        return(values[1])
#ensuring that the value is printed
print_recieve(values)
#ensuring that the second value is stored via the return
print(print_recieve(values))

#Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

numbas= [1, 2, 3, 4, 5]

def one_plus_length(numbas):
    x = numbas[0] + len(numbas)
    print(x)
    return(x)

one_plus_length(numbas)



#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

#first list
biggins = [21, 16, 45, 91]

def large(biggins):
    bigger_biggins = []
    for i in biggins:
        if i > biggins[1]:
            #print(i) used to see if code was properly appending to new list.
            bigger_biggins.append(i)
    print(len(bigger_biggins))
    #If the list has less than 2 elements, have the function return False figured returning true shows that its working. 
    if len(bigger_biggins) >= 3:
            print("true")
    elif len(bigger_biggins) <= 2:
            print("false")
    #print(bigger_biggins) used to be sure that the array was there.
    return(bigger_biggins)


    


large(biggins)

# this was a long one, only figure it out after i told myself to walk away and actually did it. deff rewarding to figure it out after all this time. 

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

#what is it i need to do? wright a function that accepts two intergers as paramaters, paramaters would be size, and value, so i need to create a function that looks like this def length_and_value(length, value):
#after that i need to create a for loop that creates a list, so ill need to add in a list to the function, named l_and_v that adds the value to the list a number of times equal to the length. this may need to be a while loop instead of a for loop. not sure the while loop would look something like this, while x is >= length append value to list, print list, and after that loop exits, return list. 


def length_and_value(length, value):
    l_and_v = []
    x = 0
    #print(l_and_v)
    #print(x)
    while x < length:
        #print(x)
        l_and_v.append(value)
        x = x+1
        #print(l_and_v)
    print(l_and_v)
    return l_and_v



length_and_value(7,6) 
length_and_value(21, 16)