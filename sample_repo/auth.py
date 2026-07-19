auth_code = '''
from database import get_user

def login(username, password):

    user = get_user(username)

    # Intentional Bug
    if password.strip() == "":
        raise Exception("Password Error")

    if user["password"] != password:
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    return {
        "success": True,
        "message": "Login Successful"
    }
'''

with open("sample_repo/auth.py", "w") as f:
    f.write(auth_code)
