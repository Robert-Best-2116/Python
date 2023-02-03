from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


# ! where i stoped and what i did, i added password to my main user_schema, added password to all of my methods and on my routes as well as my templates, used the password type to conceal what was written, feeling good about everything that ive done

# ! todays victories! got all of my routing done with help from TA Peter and Ta Samuel, i used session to carry over the information on the dojo route to the ninja delete route, used an fstring on the users update information to reroute me back to the proper dojo upon updating the information, added session to keep my users information inside of the create user route as well as session.clear() to insure that i kept my users information there when i showed them what i needed to fix! its pretty cool, today had great flow, also i was given this really cool plug in for my comments to give me some more color diffrentation on my updates/comments for myself. good work self! feeling really great about todays progress. 
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

# model the class after the friend table from our database

    # ... other class methods
    # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = """
        INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s)
        ;"""
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users').query_db( query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;"
        print("data", data)
        result= connectToMySQL('users').query_db( query, data)
        return result

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users').query_db( query, data)
        return result

    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        # ! this is called a guard clause, it returns because we do not want the user to continue any further in the function if they do not pass the test/criteria.
        if len(user['fname']) == 0 or len(user['lname']) == 0 or len(user['email']) == 0 or len(user['password']) == 0:
            flash('All Fields Must Be Filled Out')
            return False
        if len(user['fname']) < 2:
            flash("First Name Must Be at least 2 Characters.")
            is_valid = False
        if len(user['lname']) < 2:
            flash("Last Name Must Be at Least 2 Characaters")
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        # logic is not perfect for the else statment, but it make sence because we are first checking to see if the email is valid prior to executing the else statment and querying our database. 
        else:
            query = 'SELECT * FROM users WHERE email = %(email)s;'
            print("query", query)
            # ! if I am usuing the database, i can pass in the database name instead of data, and it will selct the information from it provided that it is there. 
            result = connectToMySQL('users').query_db( query, user)
            print("result", result)
            if len(result) > 0:
                flash("Email already in use")
                is_valid = False
        if len(user['password']) < 2:
            flash('Password must be longer than 2 characters')
            is_valid = False
        return is_valid