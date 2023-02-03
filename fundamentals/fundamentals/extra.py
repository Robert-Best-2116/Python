students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# what do i need to do? loop trough each dictonary, and print each key and the associated value, 

def iterateDictonary(list):
    for index in range(0, len(list)):
        for x, y in list[index].items():
            #print(key, "-", val)
            print(x, y)

iterateDictonary(students)
name = list[range(5)]
print(name) 