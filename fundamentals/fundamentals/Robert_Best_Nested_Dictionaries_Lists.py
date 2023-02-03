

# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]['first_name'] = 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y'] = 30
print(z)

#2

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},0
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# what do i need to do? loop trough each dictonary, and print each key and the associated value, 

def iterateDictonary(list):
    for index in range(0, len(list)):
        for key, val in list[index].items():
            print(key, "-", val)
            

iterateDictonary(students) 


# The soultion page has the output function it it, i dont konw why or anything, i saw that the only thing i was missing was the students[index] i had it at students [0] and of course it was just repeating the 0 function,  over and over again, reached out to chris m and to camron, both busy, so i went with the solutions page to see what was wrong, and i was iterating at 0 every single time. beaucase i had for key, val in students[0].items(): so oviously it would be after looking at it. 

#3 Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

        # is key a reserved word????? is val a reserved word???? do i need key and val because i am accessing them both?? is the key named key name to create distinction between the name in the function?? why dosent it mess up when their the same name?  can it only access the value because value is in the for loop??? 
    #So i had the key == key and it printed the first and last name on both, so im guessing key is a reserved word.

def iterateDictonary2(key_name, list):
    for index in range(0, len(list)):
        for key, val in list[index].items():
            if key == key_name:
                print(val)

iterateDictonary2('first_name', students)
iterateDictonary2('last_name', students)  





