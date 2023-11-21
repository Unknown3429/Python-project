import MySQLdb


# create DataBase
def create_database(name):
    try:
        # connect to the database server
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root")
        cur = mydb.cursor()

        command = cur.execute(f"CREATE DATABASE {name}")
        print(command, " Database created")

    except:
        print("Internal Server Error")

    finally:
        cur.close()
        mydb.close()


# Show DataBase
def show_databases():
    try:
        # connect to the database server
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root")
        cur = mydb.cursor()
        command = cur.execute(f"SHOW DATABASES")
        for x in cur:
            print(x)

    except:
        print("Internal Server Error")

    finally:
        cur.close()
        mydb.close()


# Create Table
def create_table(dbName, name, column, count):
    # connect to the database server
    mydb = MySQLdb.connect(host='localhost', user='root',
                           passwd="root", db=f"{dbName}")
    cur = mydb.cursor()
    try:
        value = "(30)"
        if len(count) == 2:
            columnsf = f'{column[0][0]} {column[1][0]+value if column[1][0] == "VARCHAR" else column[1][0]}, {column[0][1]} {column[1][1]+value if column[1][0] == "VARCHAR" else column[1][1]}'

            command = cur.execute(f"CREATE TABLE {name} ({columnsf})")
            print(f"table {name} created")

        elif len(count) == 3:
            columnsf = f'{column[0][0]} {column[1][0]+value if column[1][0] == "VARCHAR" else column[1][0]}, {column[0][1]} {column[1][1]+value if column[1][0] == "VARCHAR" else column[1][1]}, {column[0][2]} {column[1][2]+value if column[1][0] == "VARCHAR" else column[1][2]}'

            command = cur.execute(f"CREATE TABLE {name} ({columnsf})")
            print(f"table {name} created")

        elif len(count) == 4:
            columnsf = f'{column[0][0]} {column[1][0]+value if column[1][0] == "VARCHAR" else column[1][0]}, {column[0][1]} {column[1][1]+value if column[1][0] == "VARCHAR" else column[1][1]}, {column[0][2]} {column[1][2]+value if column[1][0] == "VARCHAR" else column[1][2]}, {column[0][3]} {column[1][3]+value if column[1][0] == "VARCHAR" else column[1][3]}'

            command = cur.execute(f"CREATE TABLE {name} ({columnsf})")
            print(f"table {name} created")

        else:
            print("Choose Column Count B/W 2-4")

    except:
        print("Internal Server Error")

    finally:
        cur.close()
        mydb.close()


# show tables
def show_tables(dbName):
    # connect to the database server
    mydb = MySQLdb.connect(host='localhost', user='root',
                           passwd="root", db=f"{dbName}")
    cur = mydb.cursor()

    try:
        command = cur.execute("show tables")
        for i in cur:
            print(i)

    except:
        print("Internal Server Error")

    finally:
        cur.close()
        mydb.close()


# delete table
def delTable(dbName, table):
    # connect to the database server
    mydb = MySQLdb.connect(host='localhost', user='root',
                           passwd="root", db=f"{dbName}")
    cur = mydb.cursor()

    try:
        command = cur.execute(f"DROP TABLE {table}")
        print(f"table {table} deleted")

    except:
        print("Internal Server Error")

    finally:
        cur.close()
        mydb.close()


# table desc
def table_desc(dbName, tableName):
    # connect to the database server
    mydb = MySQLdb.connect(host='localhost', user='root',
                           passwd="root", db=f"{dbName}")
    cur = mydb.cursor()

    try:
        r = []
        command = cur.execute(f"DESC {tableName}")
        for i in cur:
            print(i)
            r.append(i)
        return r
    except:
        print("Internal Server Error")

    finally:
        cur.close()
        mydb.close()

# add data


def insertData(dbName, tableName, ):
    print("--------------------------------------")
    print(f"Add data into {tableName}")
    print("---------------------------------------")
    row = table_desc(dbName, tableName)
    frow = []
    for i in row:
        r = list(i)
        for x in range(4):
            r.pop()
        frow.append(r)

    # print(frow)
    mydb = MySQLdb.connect(host='localhost', user='root',
                           passwd="root", db=f'{dbName}')
    cur = mydb.cursor()
    title = []

    for i in frow:
        title.append(i[0])

    values = [str(input(f"\nEnter {i[0]}: ")) for
              column, i in enumerate(frow)]
    print(title)
    sql = (
        f"INSERT INTO {tableName} ({title[0]}, {title[1]}, {title[2]}) values('{values[0]}', {values[1]}, {values[2]})")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "was inserted.")


# display data
def display_data(dbName, tableName):
    try:
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root", db=f'{dbName}')
        cur = mydb.cursor()
        command = cur.execute(f'SELECT * FROM {tableName}')
        results = cur.fetchall()

        row = table_desc(dbName, tableName)
        print("-----------------------------------------------------------------")
        print("Students Information")
        print("\n-----------------------------------------------------------------")

        frow = []
        for i in row:
            r = list(i)
            for x in range(4):
                r.pop()
            frow.append(r)

        for x in frow:
            print(x[0], end='    |')
        print("\n-----------------------------------------------------------------")
        for i in cur:
            print("\n")
            for x in i:
                print(x, end='    |')
    except Error as error:
        print(error)

    finally:
        cur.close()
        mydb.close()


# main
def main():
    # Menu
    print("Menu")
    print("\n1. Create DataBase")
    print("\n2. Show DataBases")
    print("\n3. Create Table")
    print("\n4. Show Tables")
    print("\n11. Delete Table")
    print("\n12. Table Desc")
    print("\n5. Insert Record")
    print("\n6. Display Record")
    print("\n7. Delete Record")
    print("\n8. Search Record")
    print("\n9. Update Record")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        dbName = input("\nEnter Database Name: ")
        create_database(dbName)

    elif choice == 2:
        show_databases()

    elif choice == 3:
        dbName = input("\nEnter db Name: ")
        tableName = input("\nEnter Table Name: ")
        columnCount = [str(i+1)
                       for i in range(int(input("\nEnter Number of Columns, count is b/w 2-4: ")))]
        dataTypes = [str(input(f"\nColumn {column}: Enter DataType (INT/VARCHAR/DATE): ")).upper() for
                     column in columnCount]
        # primaryKey = str(input("\nPrimary Key? (yes/no): ")).lower().strip()
        foreignKeys = []

        nameColumns = [
            str(input(f"\nColumn {column}: Enter Name : ")) for
            column in columnCount]

        foreignKeys.append(nameColumns)
        foreignKeys.append(dataTypes)
        create_table(dbName, tableName, foreignKeys, columnCount)

    elif choice == 4:
        dbName = input("\nEnter db Name: ")
        show_tables(dbName)

    elif choice == 11:
        dbName = input("\nEnter db Name: ")
        tableName = input("\nEnter Table Name: ")
        delTable(dbName, tableName)

    elif choice == 12:
        dbName = input("\nEnter db Name: ")
        tableName = input("\nEnter Table Name: ")
        table_desc(dbName, tableName)

    elif choice == 5:
        dbName = input("\nEnter db Name: ")
        tableName = input("\nEnter Table Name: ")
        insertData(dbName, tableName)

    elif choice == 6:
        dbName = input("\nEnter db Name: ")
        tableName = input("\nEnter Table Name: ")
        display_data(dbName, tableName)


main()
