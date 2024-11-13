class Person:
    def __init__(self):
        self.name = input("Enter the employee's name: ")
        self.employee_id = int(input("Enter the employee's ID number: "))
        
class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        self.department = input("Enter the department: ")
        self.position = input("Enter the position: ")

    def print_info2(self):
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        
class Salary:
    def __init__(self):
        self.wage_per_hour = float(input("Enter the wage per hour: "))
        self.hours_of_work_per_day = int(input("Enter the hours of work per day: "))
        self.total_days_in_a_month = int(input("Enter the total days in a month: "))

    def calculate_total_salary(self):
        return self.wage_per_hour * self.hours_of_work_per_day * self.total_days_in_a_month
    
    def validate_inputs(wage, hours, days):
     while True:
        if wage < 0:
            print("Invalid wage per hour. Please enter a non-negative value.")
            wage = float(input("Enter the wage per hour: "))
        elif hours < 0 or hours > 24:
            print("Invalid hours of work per day. Please enter a value between 0 and 24.")
            hours = int(input("Enter the hours of work per day: "))
        elif days < 1 or days > 31:
            print("Invalid total days in a month. Please enter a value between 1 and 31.")
            days = int(input("Enter the total days in a month: "))
        else:
            break
     return wage, hours, days
 
    def display_salary_info(total_salary):
      print(f"Total Salary: ${total_salary:.2f}")
  
class Employee1(Employee, Salary):
    def __init__(self):
        Employee.__init__(self)
        Salary.__init__(self)

    def display_info(self):
        super().print_info2()
        super().display_salary_info()
        

employee = Employee1()
employee.display_info()
    
