import MySQLdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def dataanalysis(choice):
    # data anlysis
    try:
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root", db='products')
        cur = mydb.cursor()

        # for sales
        command = cur.execute('SELECT sales FROM allproducts')
        results = cur.fetchall()
        arr = []
        arr2 = []
        arr3 = []
        hei = 0
        for i in results:
            arr.append(i[0])
            # print(i[0])
        data = np.array(arr)

        # for heights
        command = cur.execute('SELECT Id FROM allproducts')
        results = cur.fetchall()
        for i in results:
            hei += 1
            arr2.append(hei)
            # print(i[0])
        ids = np.array(arr2)

        # for names
        command = cur.execute('SELECT name FROM allproducts')
        results = cur.fetchall()
        for i in results:
            arr3.append(i[0])
        names = np.array(arr3)
        if choice == 1:
            # bar graph
            left_coordinates = ids
            heights = data
            bar_labels = names
            plt.bar(left_coordinates, heights, tick_label=bar_labels,
                    width=0.6, color=['red', 'black'])
            plt.xlabel('Products')
            plt.ylabel('No. Of sales')
            plt.title("Sales graph")

            # show plot
            plt.show()
        if choice == 2:
            # pie chart
            # fig = plt.figure(figsize=(10, 7))
            plt.pie(data, labels=names)

            # show plot
            plt.show()

    except error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# add new employee
def add_product(product_name, category, price, quantity, sales):
    try:
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root", db='products')
        cur = mydb.cursor()
        sql = (
            f"INSERT INTO allproducts (name, category, price, quantity, sales) values('{product_name}', '{category}', {price},{quantity}, {sales})")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "was inserted.")

    except error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# Update employee
def update_employee(product_name, sales):
    try:
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root", db='products')
        cur = mydb.cursor()
        sql = f"Update allproducts set sales = {sales} where name = '{product_name}'"
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "was Updated.")
        print(f"Employee {product_name} has Updated ")

    except Error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# Delete employee
def delete_employee(product_name):
    try:
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root", db='products')
        cur = mydb.cursor()
        sql = f"Delete from allproducts where name = '{product_name}'"
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "was Deleted.")
        print(f"Employee {product_name} has Deleted ")

    except Error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# Display employee
def display_employees():
    try:
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root", db='products')
        cur = mydb.cursor()
        command = cur.execute('SELECT * FROM allproducts')
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
        print("\n1. Add Product")
        print("\n2. Update employee")
        print("\n3. Delete employee")
        print("\n4. Display employee")
        print("\n5. Display Analysis")
        print("\n6. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            product_name = input("\nEnter Product name: ")
            category = input("\nEnter Category: ")
            price = int(input("\nEnter price: "))
            quantity = int(input("\nEnter quantity: "))
            sales = int(input("\nEnter sale of products: "))

            add_product(product_name, category, price, quantity, sales)

        elif choice == 2:
            product_name = input("\nEnter Product name: ")
            sales = int(input("\nEnter sales: "))
            update_employee(product_name, sales)

        elif choice == 3:
            product_name = input("\nEnter Product name: ")
            delete_employee(product_name)

        elif choice == 4:
            display_employees()

        elif choice == 5:
            try:
                choice = input("\nEnter \n1.Bar Graph\n2.Pie Chart\n")
                if choice == '1':
                    dataanalysis(1)
                else:
                    dataanalysis(2)
            except Error as error:
                print(error)


        elif choice == 6:
            break

        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()
