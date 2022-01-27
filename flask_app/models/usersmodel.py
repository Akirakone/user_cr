from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'users_cr'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        query_results = connectToMySQL(cls.db_name).query_db(query)
        
        users = []
        for each_row in query_results:
            new_user = cls(each_row)
            users.append(new_user)

        return users

        #for user_data in results:
            #users.append( cls(user_data) )

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = (%(id)s)"
        query_results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(query_results[0])

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = (%(id)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = (%(id)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)