import psycopg2, requests

conn = psycopg2.connect(
        host="xxxxxxx",
        database="xxxxxx",
        user="xxxxxxx",
        password="*****")
print("Connected", conn)

def fetchUser(username):
    cursor = conn.cursor()
    cursor.execute ('SELECT COUNT(*) FROM userProfiles WHERE username = %s' ,(username,))
    #query = ('''SELECT COUNT(*) FROM user_manage WHERE Name = %s''', (username,))
    #print(query)
    record = cursor.fetchone()
    print(record)
    print(record[0])
    if record[0] > 0:
        print("exists")
        cursor.execute('SELECT * FROM userProfiles WHERE username =  %s', (username,))
        result = cursor.fetchall()
        print(result)
        for row in result:
            Username = row[0]
            Password = row[1]
            UserEmail = row[2]
            CreatedDate = row[3]
        cursor.close()
        return {"Username": Username, "Password": Password, "Useremail": UserEmail, "CreatedDate": CreatedDate }
    else:
        cursor.close()
        return "User does not exist!"


#print(fetchUser("Deepa"))


def createUser(userObj):
   # try:
    cursor = conn.cursor()
    print(type(userObj))
    print(userObj)
    username = userObj['Username']
    password = userObj['Password']
    email = userObj['Useremail']
    print(username, password, email )
    cursor.execute ('SELECT COUNT(*) FROM userProfiles WHERE Username = %s' ,(username,))
    result = cursor.fetchone()
    #print(result)
    print(result[0])
    if result[0] > 0:
        #return "User - ", name + " already Exists"
        return f"User - {username} already Exists"
    else:
        cursor.execute('Insert into userProfiles (Username, Password, CreatedDate, Email) values (%s, %s, CURRENT_TIMESTAMP, %s)', (username, password, email,))
        conn.commit()
        return "User Registered!"
 #   except Exception as Error:
 #       print("Already exists")
        

#createUser({"UserID":"man4eeee","Useremail":"mannee3a@gmail","Username":"Manee3"})

def userAuth(username, password):
    cursor = conn.cursor()
    print(username, password)
    cursor.execute('Select count(*) from userProfiles where Username = %s',(username,))
    result = cursor.fetchone()
    print(result)
    print(result[0])
    if result[0] > 0:
        cursor.execute('Select count(*) from userProfiles where username = %s and password = %s',(username, password,))
        result = cursor.fetchone()
        print(result[0])
        if result[0] > 0:
            cursor.execute('update userProfiles set lastlogin = now() where username = %s', (username,))
            conn.commit()
            return "Login suceeded"
        else:
            return f"Incorrect Password for User - {username}"
    else:
        return f"User - {username} does not exist. Please register"

def updateUser(data):
    updateQuery1 = '''update userProfiles set '''
    updSetQuery = ' '
    updWhrQuery = ''
    username =''
    for key,value in data.items():
        print("key: {0} | value: {1}".format(key, value))
        if key == 'Username':
            username = value
            updWhrQuery = ' where ' + key + '=\'' + value + '\''
        else:
            updSetQuery = updSetQuery + key + ' = \'' +value + '\'' + ','
            
    finalQry =  updateQuery1 + updSetQuery[:-1] +  updWhrQuery
    print(finalQry)
    cursor = conn.cursor()
    cursor.execute(finalQry)
    conn.commit()
    return f"Updated user {username} successfully"


def delUser(username):
    cursor = conn.cursor()
    print(username)
    cursor.execute('Select count(*) from userProfiles where Username = %s',(username,))
    result = cursor.fetchone()
    print(result)
    print(result[0])
    if result[0] > 0:
        cursor.execute('delete from userProfiles where username = %s', (username,))
        conn.commit()
        return f"User - {username} deleted"
    else:
        return f"User - {username} does not exist"    