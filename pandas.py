import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define global variables
student_fields = ['roll', 'name', 'marks', 'age', 'email', 'phone']
student_database = 'students.csv'


# menu
def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


# add student
def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    # input("Press any key to continue")
    return


# display student
def view_students():
    global student_fields
    global student_database
    marks = []
    names = []
    ids = []
    data = []
    cor = np.array(ids)
    hei = 0

    print("--- Student Records ---")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='    |')
        print("\n-----------------------------------------------------------------")

        # for graphs
        for row in reader:
            if len(row) > 0:
                if row[0] == row[0]:
                    hei += 1
                    ids.append(hei)
                    marks.append(int(row[2]))
                    names.append(row[1])

            # for print all students
            print("\n")
            ps = pd.series(marks)
            print("ps", ps)
            for item in row:
                print(item, end=" |")

            # bar graph
            data = np.array(marks)
            left_coordinates = ids
            heights = data
            bar_labels = names
            plt.bar(left_coordinates, heights, tick_label=bar_labels,
                    width=0.6, color=['black', 'blue'])
            plt.xlabel('Students')
            plt.ylabel('Marks')
            plt.title(" Marks Analysis")
            plt.show()


# search student
def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("marks: ", row[3])
                    print("Email: ", row[4])
                    print("Phone: ", row[5])
                    break
        else:
            print("Roll No. not found in our database")
    # input("Press any key to continue")


# update student
def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ", index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    # input("Press any key to continue")


# delete student
def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    # input("Press any key to continue")


while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break
