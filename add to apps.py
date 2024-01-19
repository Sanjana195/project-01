@app.route('/delete_employee/<employee_id>')
    def delete_employee(employee_id):
        # Simulate deleting an employee (actual implementation would involve a database)
        # Here, we remove the employee from the dummy 'employees' list
        for employee in employees:
            if employee['id'] == int(employee_id):
                employees.remove(employee)
                return render_template('pim.html', employee_list=employees, success_message="Employee deleted successfully!")
    
        # If employee not found, show an error message
        return render_template('pim.html', employee_list=employees, error_message="Employee not found.")
