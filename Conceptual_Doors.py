#to access the door to a list, you use an index, even more spesific, you use a list and an index, wrapped in brackets,

fruits = ["orange", "apple"]
print(fruits[1])


#to access the door to a dictonary, you use an index, even more spesific, you use a list and a key, wrapped in brackets,
fruits = {"color":"red","name":"apple"} 
print(fruits["name"])

class Fruit:
    def __init__(self,data):
        self.color = data['color']
        self.name = data['name']


apple = Fruit(fruits)

print(apple.name)