from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db="users_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
# going to use a class method to invoke a method for instances
# now we use class methods to query our database
# crud method: read
    @classmethod
    def get_all_users(cls):
        query = """ 
            SELECT * FROM users;
        """
        # make sure to call the connectToMySQL function with the 
        # schema you are targeting
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of the class user
        all_users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            # need to pass in a dict to fill out info for data
            all_users.append(cls(user))
        return all_users
   
# the get_one method will be used when we need to retrieve just one specific row of the table.
# just added this...now have to implement it with the following code... and add update class 
# and delete class for the rest of the CRUD method but this is apart of the crud method: read
    @classmethod
    def get_one(cls, user_id):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        data = {'id':user_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
# crud method: create
    @classmethod
    def save_user(cls,data):
        query = """
            INSERT INTO users
            (first_name, last_name, email)
            VALUES(%(first_name)s, %(last_name)s, %(email)s)
        """
        
        # instead of results = connectToMySQL(cls.db).query_db(query)
        # we can use (saves us one line of code ;) )
        return connectToMySQL(cls.db).query_db(query, data)
