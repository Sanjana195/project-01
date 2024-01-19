from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# For simplicity, using a hardcoded username and password
valid_username = "Admin"
valid_password = "admin123"

@app.route('/')
def index():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == valid_username and password == valid_password:
        return "Login successful!"
    else:
        return "Login failed. Please check your credentials."

if __name__ == '__main__':
    app.run(debug=True)
