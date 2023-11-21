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
def create_table(dbname, name):
    try:
        # connect to the database server
        mydb = MySQLdb.connect(host='localhost', user='root',
                               passwd="root", db=f'{dbName}')
        cur = mydb.cursor()
        command = cur.execute(
            f"CREATE TABLE {name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
        for x in cur:
            print(x)

    except:
        print("Internal Server Error")

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
    print("\n5. Insert Record")
    print("\n6. Update Record")
    print("\n7. Delete Record")
    print("\n8. Search Record")
    print("\n9. Display Record")

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
                       for i in range(int(input("\nEnter Number of Columns: ")))]
        dataTypes = [str(input(f"\nColumn {column}: Enter DataType (INT/VARCHAR/DATE): ")) for
                     column in columnCount]
        # primaryKey = str(input("\nPrimary Key? (yes/no): ")).lower().strip()
        foreignKeys = []

        nameColumns = [
            str(input(f"\nColumn {column}: Enter Name : ")) for
            column in columnCount]

        foreignKeys.append(nameColumns)
        foreignKeys.append(dataTypes)
        print(foreignKeys)


main()
