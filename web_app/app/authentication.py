from database import get_user_collection
import bcrypt

collection = get_user_collection()

def authenticate(jreq) ->int : # returns status code
    if not(["password", "username"].issubset(jreq.keys())):
        return 305
    else:
        username_inp = jreq["username"]
        password_inp = jreq["password"]
        password_hash = collection.find_one[{
            "username" : username_inp
            }]["password"]
        # Checking the password     
        if (bcrypt.hashpw(password_inp.encode("utf-8"), password_hash) == password_hash):
            return 200
        else:
            return 302        
        
def checkExists(jreq) -> int :
    if not(["password", "username"].issubset(jreq.keys())):
        return 305
    else:
        username_inp = jreq["username"]
        password_inp = jreq["password"]
        document = collection.find_one[{
            "username" : username_inp
            }]
        # Checking the password     
        if document:
            return 200
        else:
            return 303 
        
        return 