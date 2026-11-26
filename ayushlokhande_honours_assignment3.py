
import sqlite3


class EmployeeDatabase:

    def __init__(self):
        self.connection = sqlite3.connect("employee.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                department TEXT
            )
        """)

        self.connection.commit()

    def insert_employee(self, name, age, department):
        query = "INSERT INTO employees (name, age, department) VALUES (?, ?, ?)"
        values = (name, age, department)

        self.cursor.execute(query, values)
        self.connection.commit()

        print("New employee record inserted.")

    def display_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        employees = self.cursor.fetchall()

        if len(employees) == 0:
            print("Database contains no employee records.")
        else:
            for employee in employees:
                print(employee)

    def modify_employee(self, emp_id, name, age, department):
        query = """
            UPDATE employees
            SET name = ?, age = ?, department = ?
            WHERE id = ?
        """

        self.cursor.execute(query, (name, age, department, emp_id))
        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("Employee information modified.")
        else:
            print("Employee ID does not exist.")

    def remove_employee(self, emp_id):
        self.cursor.execute(
            "DELETE FROM employees WHERE id = ?",
            (emp_id,)
        )

        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("Employee record removed.")
        else:
            print("Employee ID not found.")

    def close_database(self):
        self.connection.close()


def main():
    database = EmployeeDatabase()

    while True:
        print("\n===== EMPLOYEE DATABASE =====")
        print("1. Insert Employee")
        print("2. Display Employees")
        print("3. Modify Employee")
        print("4. Remove Employee")
        print("5. Exit")

        choice = input("Enter your selection: ")

        try:
            if choice == "1":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                department = input("Enter Department: ")

                database.insert_employee(name, age, department)

            elif choice == "2":
                database.display_employees()

            elif choice == "3":
                emp_id = int(input("Enter Employee ID: "))
                name = input("Enter Updated Name: ")
                age = int(input("Enter Updated Age: "))
                department = input("Enter Updated Department: ")

                database.modify_employee(emp_id, name, age, department)

            elif choice == "4":
                emp_id = int(input("Enter Employee ID to delete: "))
                database.remove_employee(emp_id)

            elif choice == "5":
                print("See You Soon!")
                break

            else:
                print("Invalid selection. Try again.")

        except ValueError:
            print("Please enter valid numeric values for ID and age.")

    database.close_database()


if __name__ == "__main__":
    main()
