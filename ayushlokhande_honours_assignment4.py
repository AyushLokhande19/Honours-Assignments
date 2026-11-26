
import pandas as pd
import os


class EmployeeManager:

    def __init__(self, filename="employees.csv"):
        self.filename = filename
        columns = ["ID", "Name", "Salary"]

        if os.path.exists(self.filename):
            self.data = pd.read_csv(self.filename, dtype={"ID": str})
        else:
            self.data = pd.DataFrame(columns=columns)

    def save_data(self):
        self.data.to_csv(self.filename, index=False)

    def add_employee(self, emp_id, name, salary):
        if emp_id in self.data["ID"].astype(str).values:
            print("Employee ID already exists.")
            return

        new_record = {
            "ID": emp_id,
            "Name": name,
            "Salary": salary
        }

        self.data.loc[len(self.data)] = new_record
        self.save_data()

        print("Employee record added successfully.")

    def display_employees(self):
        if self.data.empty:
            print("No employee records available.")
        else:
            print("\nEmployee Details:")
            print(self.data.to_string(index=False))

    def update_employee(self, emp_id, name, salary):
        condition = self.data["ID"].astype(str) == emp_id

        if condition.any():
            self.data.loc[condition, ["Name", "Salary"]] = [name, salary]
            self.save_data()
            print("Employee information updated.")
        else:
            print("Employee ID not found.")

    def delete_employee(self, emp_id):
        condition = self.data["ID"].astype(str) != emp_id

        if condition.any() == False:
            print("Employee ID not found.")
            return

        self.data = self.data[condition].reset_index(drop=True)
        self.save_data()

        print("Employee record deleted.")


def main():

    employee = EmployeeManager()

    while True:
        print("\n===== EMPLOYEE MANAGEMENT =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            salary = input("Enter Salary: ")

            employee.add_employee(emp_id, name, salary)

        elif choice == "2":
            employee.display_employees()

        elif choice == "3":
            emp_id = input("Enter ID to update: ")
            name = input("Enter New Name: ")
            salary = input("Enter New Salary: ")

            employee.update_employee(emp_id, name, salary)

        elif choice == "4":
            emp_id = input("Enter ID to delete: ")
            employee.delete_employee(emp_id)

        elif choice == "5":
            print("See You Soon!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
