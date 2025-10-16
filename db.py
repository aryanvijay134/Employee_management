import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abhi@2003",  
        database="employees_management"  
    )

def get_employees():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def add_employee(emp_id, name, dept_id, doj, email, password, phone):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO employees (emp_id, name, dept_id, doj, email, password, phone)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (emp_id, name, dept_id, doj, email, password, phone)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    print("Employees added successfully.")

def update_employee(emp_id, name, dept_id, doj, email, password, phone):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """UPDATE employees SET name=%s, dept_id=%s, doj=%s, email=%s, password=%s, phone=%s WHERE emp_id=%s"""
    values = (name, dept_id, doj, email, password, phone, emp_id)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    print("Employees updated successfully.")

def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Employees deleted successfully.")

def get_departments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM department")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

if __name__ == "__main__":
    
    print(" Employee List:")
    for emp in get_employees():
        print(emp)

    print("\n Departments:")
    for dept in get_departments():
        print(dept)
