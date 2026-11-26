
import csv
import os

FILE_NAME = "employees.csv"


def add_employee():
    employee = [
        input("Enter Employee ID: "),
        input("Enter Employee Name: "),
        input("Enter Department: "),
        input("Enter Salary: ")
    ]

    with open(FILE_NAME, "a", newline="") as file:
        csv.writer(file).writerow(employee)

    print("Employee record saved successfully!")


def display_employees():
    if not os.path.exists(FILE_NAME):
        print("No employee records available.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        records = list(csv.reader(file))

    if not records:
        print("Employee list is empty.")
        return

    print("\nEmployee Records:")
    for employee in records:
        print("ID:", employee[0])
        print("Name:", employee[1])
        print("Department:", employee[2])
        print("Salary:", employee[3])
        print("------------------------")


def update_employee():
    target_id = input("Enter Employee ID to modify: ")

    if not os.path.exists(FILE_NAME):
        print("Employee file not found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        records = list(csv.reader(file))

    updated = False

    for employee in records:
        if employee[0] == target_id:
            print("Existing Details:", employee)

            employee[1] = input("New Employee Name: ")
            employee[2] = input("New Department: ")
            employee[3] = input("New Salary: ")

            updated = True
            break

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(records)

    if updated:
        print("Employee details updated successfully!")
    else:
        print("Employee ID not found.")


def delete_employee():
    target_id = input("Enter Employee ID to remove: ")

    if not os.path.exists(FILE_NAME):
        print("Employee file not found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        records = list(csv.reader(file))

    remaining = [employee for employee in records if employee[0] != target_id]

    if len(remaining) == len(records):
        print("Employee ID not found.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(remaining)

    print("Employee removed successfully!")


def main():
    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            add_employee()

        elif option == "2":
            display_employees()

        elif option == "3":
            update_employee()

        elif option == "4":
            delete_employee()

        elif option == "5":
            print("See You Soon!")
            break

        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
