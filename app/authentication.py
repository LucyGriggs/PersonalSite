import re
import hashlib

#user database
users = {}

def login(username, password):
    #user login
    if username in users and users[username] == hash_password(password):
        return True
    return False

def logout(username):
    #user logout
    pass

def register(username, password):
    #new user
    if not is_valid_username(username):
        return "invalid username format"
    if username in users:
        return "username already exists"
    users[username] = hash_password(password)
    return "registration successful"

def is_valid_username(username):
    #protect against SQL injection etc.
    pattern = re.compile(r'^[\wäöüßÄÖÜ]+$')
    return bool(pattern.match(username))

def hash_password(password):
    #hash function
    return hashlib.sha256(password.encode()).hexdigest()