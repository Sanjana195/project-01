@app.route('/edit_employee/<employee_id>', methods=['GET', 'POST'])
    def edit_employee(employee_id):
        # Simulate fetching existing employee details from a database
        existing_employee_details = {
            'first_name': 'John',
            'last_name': 'Doe',
            # Add other details as needed
        }
    
        if request.method == 'POST':
            # Process the form data and update the employee (actual implementation would involve a database)
            updated_employee_details = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                # Add other details as needed
            }
    
            # Assuming successful update, show a success message
            return render_template('edit_employee.html', success_message="Employee details updated successfully!")
    
        return render_template('edit_employee.html', employee_id=employee_id, employee_details=existing_employee_details)
