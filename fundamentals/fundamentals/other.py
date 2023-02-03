
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictonary2(key_name, list):
    for index in range(0, len(list)):
        # is key a reserved word????? is val a reserved word???? do i need key and val because i am accessing them both?? is the key named key name to create distinction between the name in the function?? why dosent it mess up when their the same name?  can it only access the value because value is in the for loop??? 
        for key, val in list[index].items():
            if key == key_name:
                print(val)

iterateDictonary2('first_name', students)
#only prints the first name, idk why, even if i comment out the first name so idfk why it dosent work. 
iterateDictonary2('last_name', students) 
