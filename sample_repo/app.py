app_code = '''
from flask import Flask, request, jsonify
from auth import login

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login_api():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    result = login(username, password)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
'''

with open("sample_repo/app.py", "w") as f:
    f.write(app_code)
