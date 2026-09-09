from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()

def check_username(username):
    response=supabase.table("users").select("username").eq("username",username).execute() #Returns empty list if not exists
    
    return len(response.data)>0 

def register_user(name,username,password):
    if check_username(username):
        return False,"Username already taken"
    
    data={"name":name,"username":username,"password":hash_pass(password)}
    
    supabase.table("users").insert(data).execute()
    
    return True,"Account created successfully"

def user_login(username,password):
    response=supabase.table("users").select("*").eq("username",username).execute()
    
    if response.data:
        user=response.data[0]
        if check_pass(password,user["password"]):
            return user
    
    return None

def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(),hashed.encode())