from configparser import ConfigParser
from pymongo import MongoClient

# Read configuration
config = ConfigParser()
config.read("config.ini")

# Establish MongoDB connection
try:
    client = MongoClient(config['DATABASE']['CONNECTIONSTRING'])
    db = client[config['DATABASE']['DB']]
    users_collection = db[config['DATABASE']['COLLECTIONUSERS']]
    queries_collection = db[config['DATABASE']['COLLECTIONQUERIES']]
except Exception as e:
    print("Data Base Connection Error!!!")

def create_user(new_name, new_email, new_date, new_password) -> int:
    """
    Creates a new user in the database.

    Args:
        new_name (str): The name of the new user.
        new_email (str): The email of the new user.
        new_date (str): The date of birth of the new user.
        new_password (str): The password for the new user.

    Returns:
        int: Returns 0 if the user already exists, 1 if the user is created successfully.
    """
    if users_collection.find_one({"_id": new_email}):
        return 0
    user = {"_id": new_email, "name": new_name, "DOB": new_date, "password": new_password}
    users_collection.insert_one(user)
    return 1

def authenticate_user(email, password):
    """
    Authenticates a user based on email and password.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        bool: Returns True if authentication is successful, False otherwise.
    """
    user = users_collection.find_one({"_id": email, "password": password})
    if user:
        return True
    return False

def get_user_queries(email):
    """
    Retrieves the queries of a user from the database.

    Args:
        email (str): The email of the user.

    Returns:
        dict: A dictionary of user queries with sanitized keys.
    """
    user_queries = queries_collection.find_one({"_id": email})
    if user_queries:
        return {k.replace("__dot__", "."): v for k, v in user_queries.items() if k != '_id'}
    return {}

def update_user_queries(username, queries):
    """
    Updates the queries of a user in the database.

    Args:
        username (str): The username (email) of the user.
        queries (dict): A dictionary of queries to update.

    Returns:
        None
    """
    sanitized_queries = {k.replace(".", "__dot__"): v for k, v in queries.items()}
    queries_collection.update_one({"_id": username}, {"$set": sanitized_queries}, upsert=True)

def update_user(new_email, new_date, new_password) -> int:
    """
    Updates the password of a user in the database.

    Args:
        new_email (str): The email of the user.
        new_date (str): The date of birth of the user.
        new_password (str): The new password for the user.

    Returns:
        int: Returns 0 if the user does not exist, 1 if the credentials are invalid, 
             and 2 if the password is updated successfully.
    """
    if not users_collection.find_one({"_id": new_email}):
        return 0
    elif not users_collection.find_one({"_id": new_email, "DOB": new_date}):
        return 1
    else:
        users_collection.update_one({"_id": new_email}, {"$set": {"password": new_password}})
        return 2

def getname(email):
    """
    Retrieves the name of a user from the database.

    Args:
        email (str): The email of the user.

    Returns:
        str: The name of the user.
    """
    user = users_collection.find_one({"_id": email})
    return user['name']

def clear_chats(email):
    """
    Clears the chat history of a user from the database.

    Args:
        email (str): The email of the user.

    Returns:
        None
    """
    queries_collection.delete_one({"_id": email})

def delete_acc(email, password):
    """
    Deletes a user account from the database.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        int: Returns 1 if the account is deleted successfully, 0 if the credentials are invalid.
    """
    if users_collection.find_one({"_id": email, "password": password}):
        users_collection.delete_one({"_id": email, "password": password})
        queries_collection.delete_one({"_id": email})
        return 1
    else:
        return 0
