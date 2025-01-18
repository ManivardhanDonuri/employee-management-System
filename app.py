import sqlite3

con = sqlite3.connect("details.db")
curr = con.cursor()
curr.execute("""CREATE TABLE employee( ID INTEGER PRIMARY KEY,
             NAME TEXT NOT NULL,
             DESIGNATION TEXT NOT NULL,
             SALARY INTEGER) """)
con.commit()


def add_employee():
    ID = int(input("enter the id of the employee : "))
    NAME = str(input("enter the name of the employee : "))
    DESIGNATION = str(input("enter the designation of the employee : "))
    SALARY = int(input("enter the salary of the employee : "))
    curr.execute("""
                 INSERT INTO employee (ID,NAME,DESIGNATION,SALARY) VALUES(?,?,?,?)""",
                 (ID,NAME,DESIGNATION,SALARY))
    con.commit()


def view_list():
    curr.execute("SELECT * FROM employee")
    records = curr.fetchall()
    if records != None:
        for record in records:
            print(record)
    else:
        print("no records found please enter the records :)")
    con.commit()


def access_record():
    employee_id = int(input("enter the key id : "))
    curr.execute("SELECT * FROM employee WHERE id=?", (employee_id,))
    employee = curr.fetchone()
    if employee != None:
        print("_employee DETAILS")
        print(f"ID : {employee[0]}")
        print(f"NAME : {employee[1]}")
        print(f"DESIGNATION : {employee[2]}")
        print(f"SALARY : {employee[3]}")
    else:
        print("no employee found match with the key id")
    con.commit()


def update():
    employee_id = int(input("enter the id of the record you want to update : "))
    curr.execute("SELECT * FROM employee WHERE id=?", (employee_id,))
    current_employee = curr.fetchone()
    print("""what are the changes to be performed on records
            1.NAME
            2.DESIGNATION
            3.SALARY
            """)
    option = int(input("enter your choice : "))
    if current_employee != None:
        if option == 1:
            new_name = str(input("enter the updated name : "))
            curr.execute("UPDATE employee SET NAME=? WHERE id=?", (new_name or current_employee[1], employee_id))
        elif option == 2:
            new_designation = str(input("enter the updated designation : "))
            curr.execute("UPDATE employee SET DESIGNATION=? WHERE id=?", (new_designation or current_employee[2], employee_id))
        elif option == 3:
            new_salary = int(input("enter the updated salary : "))
            curr.execute("UPDATE employee SET SALARY=? WHERE id=?", (new_salary or current_employee[3], employee_id))
    else:
        print("no match record has been found with key :(")
    con.commit()


def delete_record():
    employee_id = int(input("enter the id of the record you want to delete : "))
    curr.execute("SELECT * FROM employee WHERE id=?", (employee_id,))
    target_employee = curr.fetchone()
    if target_employee != None:
        choice = int(input("""do you want to delete this record : 
                         1.YES
                         2.NO"""))
        if choice == 1:
            curr.execute("DELETE FROM employee WHERE id=?", (employee_id,))
            con.commit()
        else:
            print("deletion of the record has been cancelled :)")
    else:
        print("please enter an existing record id :(")

print("------------------------------employee MANAGEMENT SYSTEM--------------------------------")
print()
print()
while True:
    print(""" ***********LIST OF THE OPERATIONS ************
          1. INSERTING AN employee RECORD INTO DATABASE
          2. VIEWING THE LIST OF employee RECORDS IN THE DATABASE
          3. ACCESSING A PARTICULAR RECORD FROM THE DATABASE
          4. UPDATE A PARTICULAR RECORD IN DATABASE
          5. DELETING A PARTICULAR RECORD IN DATABASE
          6. EXIT""")
          
    choice = int(input("Please enter your choice: "))
    
    if choice == 1:
        add_employee()
    elif choice == 2:
        view_list()
    elif choice == 3:
        access_record()
    elif choice == 4:
        update()
    elif choice == 5:
        delete_record()
