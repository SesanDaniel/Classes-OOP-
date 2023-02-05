class Employee:  # Class-name
    tax = 1.05  # A class attribute
    num_of_employees = 0

    def __init__(self, name, salary):
        """ This is the init method, which runs the instance of a class
         everytime the class is instantiated. The __init__ takes "self"
         as first argument followed by any other argument we intend to
         use in class. The self argument refers to each instance of the class. """
        self.name = name  # Instance Variable
        self.salary = salary  # Instance Variable
        Employee.num_of_employees += 1

    def greetings_to_employee(self):
        """ This is a "REGULAR" method (A method is a function in a class).
         A REGULAR method takes in the instance as it's first argument, using
         "self" by convention """
        return f"Hi {self.name}, welcome to work!!!"

    def emp_salary(self):  # This is also a "REGULAR" method
        return int(self.salary)

    def salary_after_monthly_tax(self):
        return self.salary / self.tax


employee_1 = Employee("Daniel", 3550)  # First instance (Object) of class Employee
employee_2 = Employee("Bella", 7540)    # Second instance (Object) of class Employee
""" Notice how both instances of Employee class takes 2 arguments. This is because 
we passed the arguments during initialization in the __init__ method """

print(employee_1.name)
print(employee_2.name)
print(employee_1.salary)
print(employee_2.salary)
print(employee_1.salary_after_monthly_tax())
print(employee_2.salary_after_monthly_tax())
print(employee_1.greetings_to_employee())
print(employee_2.greetings_to_employee())
print(Employee.greetings_to_employee(employee_1))
print(Employee.greetings_to_employee(employee_2))
print(Employee.num_of_employees)
