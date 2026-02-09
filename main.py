import csv
from employee import Employee

FILE = "data.csv"

employees = []


def load_data():
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                employees.append(Employee(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        pass


def save_data():
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for emp in employees:
            writer.writerow(emp.to_list())


def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employees.append(Employee(emp_id, name, dept, salary))
    save_data()
    print("Employee added successfully!")


def view_employees():
    for emp in employees:
        print(emp.emp_id, emp.name, emp.department, emp.salary)


def search_employee():
    emp_id = input("Enter ID to search: ")
    for emp in employees:
        if emp.emp_id == emp_id:
            print(emp.emp_id, emp.name, emp.department, emp.salary)
            return
    print("Employee not found")


def update_employee():
    emp_id = input("Enter ID to update: ")
    for emp in employees:
        if emp.emp_id == emp_id:
            emp.name = input("New Name: ")
            emp.department = input("New Department: ")
            emp.salary = input("New Salary: ")
            save_data()
            print("Updated successfully")
            return
    print("Employee not found")


def delete_employee():
    emp_id = input("Enter ID to delete: ")
    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            save_data()
            print("Deleted successfully")
            return
    print("Employee not found")


def menu():
    print("\n1.Add Employee")
    print("2.View Employees")
    print("3.Search Employee")
    print("4.Update Employee")
    print("5.Delete Employee")
    print("6.Exit")


load_data()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
