from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user_info;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users


    @classmethod
    def save(cls, data ):
        query = """
        INSERT INTO user_info (first_name, last_name, email, password) 
        VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s)
        ;"""
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('login').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM user_info WHERE id = %(id)s;"
        result = connectToMySQL('login').query_db( query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user_info WHERE email = %(email)s;"
        print("query", query)
        result = connectToMySQL("login").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM user_info WHERE id = %(id)s;"
        results = connectToMySQL("login").query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_user( user ):
        is_valid = True
        if len(user['fname']) == 0 or len(user['lname']) == 0 or len(user['email']) == 0 or len(user['password']) == 0:
            flash('All Fields Must Be Filled Out', 'register')
            return False
        if len(user['fname']) < 2:
            flash("First Name Must Be at least 2 Characters.", 'register')
            is_valid = False
        if len(user['lname']) < 2:
            flash("Last Name Must Be at Least 2 Characaters", 'register')
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'register')
            is_valid = False
        else:
            query = 'SELECT * FROM user_info WHERE email = %(email)s;'
            print("query", query)
            result = connectToMySQL('login').query_db( query, user)
            print("result", result)
            if len(result) >= 1:
                flash("Email already in use", 'register')
                is_valid = False
        if len(user['password']) < 2:
            flash('Password must be longer than 2 characters', 'register')
            is_valid = False
        if user['password'] != user['confirm']:
            flash('Passwords must match', 'register')
        return is_valid