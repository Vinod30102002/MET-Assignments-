from fastapi import FastAPI
import os
import json
import sqlite3
 
def create_db():
    conn=sqlite3.connect("users.db")
    return conn
 
app = FastAPI()
 
create_db()
 
 
app = FastAPI()
 
 
users={}
 
 
def load_users():
    with open("db.json", 'r') as f:
        data = json.load(f)
        return data
   
def save_user(users):
    with open("db.json", 'w') as f:
        json.dump(users, f, indent=4)
 
@app.get("/users")
def read_users():
    users = load_users()
    return users
 
@app.post("/signup/{username}/{password}")
def signup(username,password):
    # users[username]=password
    users = load_users()
    users.append({'username': username, 'password': password })
    save_user(users)
    return "sucessful"
 
@app.post("/login/{username}/{password}")
def login(username,password):
    if username in users and users[username]==password:
        return "sucessful"
    else:
        return "unsuccessful"
 
@app.post("/update/{username}/{password}")
def update(username,password):
    users = load_users()
 
    for user in users:
        if username == user['username']:
            user['password'] = password
            break
 
    save_user(users)
    return "success"
 
   
@app.delete("/delete/{username}/{password}")
def delete(username,password):
    users = load_users()
    for user in users:
        if user["username"]==username and user["password"]==password:
            users.remove(user)
            save_user(users)
            return "deleted sucessfully"
 