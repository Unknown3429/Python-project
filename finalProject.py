import mysql.connector
import pandas as pd
import numpy as np


# add new employee
def add_employee(phone, employee_name, salary, designation, address, email, branch):
    try:
        mydb = mysql.connector.connect(host='localhost', user='root',
                               passwd="root", db='employees')
        cur = mydb.cursor()
        sql = (
            f"INSERT INTO emloyees (name, salary, designation, phone, email, address, branch) values('{employee_name}', {salary}, '{designation}',{phone}, '{address}', '{email}', '{branch}')")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "was inserted.")

    except Error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# Update employee
def update_employee(employee_name, salary):
    try:
        mydb = mysql.connector.connect(host='localhost', user='root',
                               passwd="root", db='employees')
        cur = mydb.cursor()
        sql = f"Update employees set Salary = {salary} where name = '{employee_name}'"
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "was Updated.")
        print(f"Employee {employee_name} has Updated ")

    except Error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# Delete employee
def delete_employee(employee_name):
    try:
        mydb = mysql.connector.connect(host='localhost', user='root',
                               passwd="root", db='employees')
        cur = mydb.cursor()
        sql = f"Delete from employees where name = '{employee_name}'"
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "was Deleted.")
        print(f"Employee {employee_name} has Deleted ")

    except Error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# Display employee
def display_employees():
    try:
        mydb = mysql.connector.connect(host='localhost', user='root',
                               passwd="root", db='employees')
        cur = mydb.cursor()
        command = cur.execute('SELECT * FROM employees')
        results = cur.fetchall()
        for i in results:
            print(i)

    except Error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# Main Function
def main():
    print(("\nEmployee mangement system\n").center(50))
    while True:
        print("\n1. Add employee")
        print("\n2. Update employee")
        print("\n3. Delete employee")
        print("\n4. Display employee")
        print("\n5. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            phone = int(input("\nEnter phone: "))
            employee_name = input("\nEnter employee name: ")
            salary = int(input("\nEnter employee salary: "))
            designation = input("\nEnter Designation: ")
            address = input("\nEnter Address: ")
            email = input("\nEnter email: ")
            branch = input("\nEnter Branch: ")
            add_employee(phone, employee_name, salary,
                         designation, address, email, branch)

        elif choice == 2:
            employee_name = input("\nEnter employee name: ")
            salary = int(input("\nEnter employee salary: "))
            update_employee(employee_name, salary)

        elif choice == 3:
            employee_name = input("\nEnter employee name: ")
            delete_employee(employee_name)

        elif choice == 4:
            display_employees()

        elif choice == 5:
            break

        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()
