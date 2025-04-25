from database import get_user_collection
import bcrypt

def add_user(jreq):
    collection = get_user_collection()
    hash_password = bcrypt.hashpw(jreq["password"].encode("utf-8"), bcrypt.gensalt())
    
    user_entry = {
        "username" : jreq["username"],
        "password" : hash_password,
        "token"    : 8,
        "text"     : "",
        "text2"    : ""
    }
    try: 
        collection.insert_one(user_entry)
        return(True, "successfull")
    
    except Exception as e:
        return(False, f"there was an error while creating entry ({ e })")


def remove_user():

    
    pass
