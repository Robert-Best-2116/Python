from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__ ( self, data ):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#create class method to query our dojo database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        #getting all of the information from the table dojos
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        #targeting the dojos_and_ninjas Schema
        dojos = []
        #created an empty list to append our instances of dojos from our results 
        for dojo in results:
            dojos.append( cls(dojo))
        return dojos
        #for loop to go through the database results and create instances of dojos with the class. 

    #creating a class method for making new dojos
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        #query for inserting the only value that is supplied by the user which is the name, everything else is auto created
        print(query)
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        #forgot to pass in the data
        print(results)
        return results

    #get one class method for just showing one dojos information
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(results[0])
        #what i did here was create a select all statment for the dojo id, note that this does not have the ninja information in it, i think that is all on the ninja page. once i get there

    
    #now comes the join, lets see if i can pull this off
    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        #now we collect the information?
        dojo = cls(results[0])
        for ninja in results:

            ninja_info = {
                "id" : ninja["ninjas.id"],
                "first_name" : ninja["first_name"],
                "last_name" : ninja["last_name"],
                "age" : ninja["age"],
                "created_at" : ninja['ninjas.created_at'],
                "updated_at" : ninja["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja_info)

        return dojo
        #had alot of things wrong with this one but got it working eventually