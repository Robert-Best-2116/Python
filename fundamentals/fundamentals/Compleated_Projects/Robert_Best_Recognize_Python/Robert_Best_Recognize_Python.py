num1 = 42 # number
num2 = 2.3 # number
boolean = True # boolean
string = 'Hello World' # string, 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictonary
fruit = ('blueberry', 'strawberry', 'banana') #list
print(type(fruit)) # type check, log statment
print(pizza_toppings[1]) # accessing the value of a list, log statment
pizza_toppings.append('Mushrooms') # adding the value to the list
print(person['name']) # accessing the dictonary vairable name , log statment
person['name'] = 'George' # updating the value name in the dictonary to a new name., vairable declaration
person['eye_color'] = 'blue' # updating the value eye_color to blue in the dictonary. vairable declaration. 
print(fruit[2]) #accessing the value of list. log statment

if num1 > 45: # conditional, if statment
    print("It's greater")  # log statment
else: # else statment
    print("It's lower") #log statment

if len(string) < 5: # conditional, if, length check
    print("It's a short word!") # string, Log statment
elif len(string) > 15: # conditoinal, elif, length check
    print("It's a long word!") # string, Log statment
else: # conditional, else
    print("Just right!") # string, log statment

for x in range(5): # for loop, number, argument
    print(x) # log statment
for x in range(2,5): # for loop, number, argument
    print(x) # log statment
for x in range(2,10,3): # for loop, number, argument
    print(x) # log statment
x = 0 # number, variable decleration, 
while(x < 5): # while loop, string, number? argument
    print(x) # log statment
    x += 1 # continue, 

pizza_toppings.pop() # deleate value any
pizza_toppings.pop(1) # deleate value in position 1

print(person) # log statment 
person.pop('eye_color') #dictonary delete  value from dictonary eye color 
print(person) # log statment, 

for topping in pizza_toppings:# for loop, 
    if topping == 'Pepperoni': # for loop, conditional, 
        continue # for loop continue 
    print('After 1st if statement') # log statment, 
    if topping == 'Olives': # for loop, conditional 
        break # for loop break, 

def print_hello_ten_times(): # function 
    for num in range(10): # for loop, argument 
        print('Hello') # log statment 

print_hello_ten_times() # log statment, function 

def print_hello_x_times(x): # function, paramater, 
    for num in range(x): # for loop, 
        print('Hello') # log statment, string 

print_hello_x_times(4) # log statment, 

def print_hello_x_or_ten_times(x = 10): # function, variable declaration 
    for num in range(x): # for loop, 
        print('Hello') # log statment, string, 

print_hello_x_or_ten_times() # log statment, 
print_hello_x_or_ten_times(4) # log statment, paramaters


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)