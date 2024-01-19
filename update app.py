from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# For simplicity, using a hardcoded valid username and password
valid_username = "your_username" (EDIT USERNAME AND PASSWORD ACCORDINGLY)
valid_password = "your_password"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == valid_username and password == valid_password:
        return redirect(url_for('pim'))

    return render_template('login.html', error="Invalid credentials. Please try again.")

@app.route('/pim')
def pim():
    # Dummy data (replace with actual data from your database)
    employee_list = [
        {'id': 1, 'first_name': 'John', 'last_name': 'Doe'},
        {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith'},
        # Add more employee details as needed
    ]

    return render_template('pim.html', employee_list=employee_list)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    # Process the form data and add the employee (actual implementation would involve a database)
    employee_details = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        # Add other details as needed
    }

    # Assuming successful addition, show a success message
    return render_template('add_employee.html', success_message="Employee added successfully!")

if __name__ == '__main__':
    app.run(debug=True)

