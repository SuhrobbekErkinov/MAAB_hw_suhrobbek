import os.path


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
            open(self.FILE_NAME, 'w').close()

    def get_employee(self, employee_id):
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                parts = line.strip().split(", ")
                if parts[0] == employee_id:
                    return Employee(*parts)
        return None

    def add_employee(self, employee):
        if self.get_employee(employee.employee_id):
            print("Employee ID is used previously. Employee with this ID already exists.")
            return
        with open(self.FILE_NAME, 'a') as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        with open(self.FILE_NAME, 'r') as file:
            records = file.readlines()
        if not records:
            print("No records found.")
        else:
            print("Employees Records:")
            for record in records:
                print(record.strip())

    def update_employee(self, employee_id):
        if not self.get_employee(employee_id):
            print("Employee not found.")
        employees = []
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                if line.startswith(employee_id + ", "):
                    name = input("Enter a new name for employee: ")
                    position = input("Enter a new position for employee: ")
                    salary = input("Enter a new salary for employee: ")
                    employees.append(f"{employee_id}, {name}, {position}, {salary}")
                else:
                    employees.append(line)
        with open(self.FILE_NAME, 'w') as file:
            file.writelines(employees)
        print("Employee updated successfully!.")

    def delete_employee(self, employee_id):
        if not self.get_employee(employee_id):
            print("Employee not found.")
        employees = []
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                if line.startswith(employee_id + ", "):
                    continue
                else:
                    employees.append(line)
        with open(self.FILE_NAME, "w") as file:
            file.writelines(employees)
        print("Employee deleted successfully.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(Employee(employee_id, name, position, salary))
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                employee = self.get_employee(employee_id)
                print("Employee Found:\n" + str(employee) if employee else "Employee not found.")
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                self.update_employee(employee_id)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()