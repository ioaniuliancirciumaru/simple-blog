import connection

def register(name, email, username, password):
    try:
        query = "INSERT INTO users(name, email, username, password) VALUES('{name}','{email}', '{username}', '{password}')".format(name=name,email=email, username=username,password=password)
        connection.execute_select(query)
    except:
        return True

def login(username):
    query = "SELECT * FROM users WHERE username = '{username}'".format(username=username)
    return connection.execute_select(query)
