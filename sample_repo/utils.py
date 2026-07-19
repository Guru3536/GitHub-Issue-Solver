utils_code = '''
def validate_username(username):

    return len(username) >= 3


def validate_password(password):

    return len(password) >= 6
'''

with open("sample_repo/utils.py", "w") as f:
    f.write(utils_code)
