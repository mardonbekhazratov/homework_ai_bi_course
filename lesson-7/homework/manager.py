import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w'):
                pass

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        if self.find_employee_by_id(employee_id):
            print("Employee ID already exists. Please use a unique ID.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        employee = Employee(employee_id, name, position, salary)
        with open(self.FILE_NAME, 'a') as file:
            file.write(str(employee) + '\n')
        print("-------------------------------")

    def view_all_employees(self):
        with open(self.FILE_NAME, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No employee records found.")
            else:
                print("Employee Records:")
                for line in lines:
                    print(line.strip())

    def find_employee_by_id(self, employee_id):
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    return line.strip()
        return None

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")
        result = self.find_employee_by_id(employee_id)
        if result:
            print("Employee Found:")
            print(result)
        else:
            print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        records = []
        updated = False

        with open(self.FILE_NAME, 'r') as file:
            records = file.readlines()

        with open(self.FILE_NAME, 'w') as file:
            for line in records:
                if line.startswith(employee_id + ","):
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    updated_record = f"{employee_id}, {name}, {position}, {salary}\n"
                    file.write(updated_record)
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Employee record updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        records = []
        deleted = False

        with open(self.FILE_NAME, 'r') as file:
            records = file.readlines()

        with open(self.FILE_NAME, 'w') as file:
            for line in records:
                if line.startswith(employee_id + ","):
                    deleted = True
                else:
                    file.write(line)

        if deleted:
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

manager = EmployeeManager()
manager.menu()
