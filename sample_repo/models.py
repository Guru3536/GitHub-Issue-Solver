models_code = '''
class User:

    def __init__(self, username, password):

        self.username = username
        self.password = password
'''

with open("sample_repo/models.py", "w") as f:
    f.write(models_code)
