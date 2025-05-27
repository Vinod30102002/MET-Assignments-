from fastapi import FastAPI, Request
import sqlite3
 
 
def connect_db():
    conn = sqlite3.connect("user1.db")
    return conn
 
app = FastAPI()

@app.get("/users")
def read_users():
    #1. get conn object
    conn = connect_db()
 
    #2. use cursor menthod
    cursor = conn.cursor()
 
    #3. use execute() and pass SQL as argument
    cursor.execute("SELECT * FROM users1")
 
    #4. use fetchall() to get all records
    data = cursor.fetchall()
 
    conn.close()
 
    output = []
 
    for entry in data:
        output.append({
            "username": entry[1],
            "password": entry[2]
        })
    return data
 
       


@app.post("/users/logout")

def logout(username,password):
 
     conn=connect_db()
 
     cursor=conn.cursor()
 
     cursor.execute("SELECT * FROM users1 WHERE username=? AND password=?",(username, password))

     data = cursor.fetchall()

     for entry in data:

         if username == entry[1] and password == entry[2]:

             cursor.execute("UPDATE users1 SET is_login =0 WHERE username =?",(username, ))

     # else:

     #     return "logout failed"

     conn.commit()

     conn.close()

     return "logout successfull"






@app.post("/users/login")
def login(username,password):

    conn=connect_db()

    cursor=conn.cursor()

    cursor.execute("SELECT * FROM users1 WHERE username=? AND password=?",(username,password))

    data=cursor.fetchall()

    for entry in data:

        if username == entry[1] and password == entry[2]:

            cursor.execute("UPDATE users1 SET is_login =1 WHERE username =?",(username, ))


        #else:
        # return "login failed"

        conn.commit()

        conn.close()

        return "login successfull"