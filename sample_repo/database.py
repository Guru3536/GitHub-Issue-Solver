database_code = '''
users = {

    "john": {
        "password": "123456"
    },

    "alice": {
        "password": "alice123"
    }

}

def get_user(username):

    return users.get(
        username,
        {
            "password": ""
        }
    )
'''

with open("sample_repo/database.py", "w") as f:
    f.write(database_code)
