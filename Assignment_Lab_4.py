class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.id}, {self.name}, {self.age}, {self.salary})"


def search_employee(employees, search_parameter, value):
    if search_parameter == 1:
        filtered_employees = [employee for employee in employees if employee.age == value]
    elif search_parameter == 2:
        filtered_employees = [employee for employee in employees if employee.name == value]
    elif search_parameter == 3:
        filtered_employees = [employee for employee in employees if employee.salary >= value]
        if value < 0:
            filtered_employees = [employee for employee in employees if employee.salary <= value]
    else:
        raise ValueError("Invalid search parameter")

    return filtered_employees


def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Select the search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    search_parameter = int(input("Enter your choice: "))

    print("Enter the value to search:")
    value = input()

    filtered_employees = search_employee(employees, search_parameter, value)

    if not filtered_employees:
        print("No employee found")
    else:
        for employee in filtered_employees:
            print(employee)


if __name__ == "__main__":
    main()
