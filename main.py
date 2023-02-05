class Employee:  # Class-name
    tax = 1.05  # A class attribute
    num_of_employees = 0
    salary_raise = 1.10

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

    def salary_after_monthly_tax(self):  # This is another "REGULAR" method
        return self.salary / self.tax

    @classmethod
    def raise_amnt(cls, amount):
        """ This is a "CLASS" method. A class method takes in the class as
        it's first argument using the conventional keyword "cls". As seen in
        the declaration, there is a decorator (@classmethod) at the top of the function
        declaration. This decorator tells the machine and humans that the method to be
        defined is a class method. """
        cls.salary_raise = amount

    @staticmethod
    def workday(day):
        """ This is a "STATIC" method. A static method does not take a default argument
        unlike the regular and class methods which takes self(instance) and cls(class)
        arguments by default respectively. It is mainly used when we are not directly working
        with our instance and classes but a bit related. static methods do not operate directly
        on the instance or class """
        if day.weekday() == 5 or day.weekday() == 6:
            """ The weekday() method comes from the inbuilt datetime module. """
            return False
        return True


class Gender(Employee):
    """ This is a subclass to the Employee class. It takes the superclass(Employee) as it's only
    argument. All attributes of the superclass can be inherited once called in the subclass. In
    some cases, we always want to add attributes in the subclass. We can update the __init__
    method in the subclass with the new attribute without having to rewrite the previous attributes
    from the subclass. """

    def __init__(self, name, salary, gender):
        super().__init__(name, salary)
        """ The super() method, is used to update the __init__ of our subclass from the super class
        without having to rewrite our attributes from the superclass. This helps in keeping ones code
        DRY. """
        # Employee.__init__(self, name, salary)  # Another approach to using the super() method
        self.gender = gender


employee_1 = Employee("Daniel", 3550)  # First instance (Object) of class Employee
employee_2 = Employee("Bella", 7540)  # Second instance (Object) of class Employee
""" Notice how both instances of Employee class takes 2 arguments. This is because 
we passed the arguments during initialization in the __init__ method """

gender_1 = Gender("Daniel", 4550, "Male")
gender_2 = Gender("Bella", 8730, "Female")

import datetime

my_date = datetime.date(2023, 2, 5)

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
print(Employee.salary_raise)
print(Employee.workday(my_date))

print(gender_1.name)
print(gender_2.name)
print(gender_1.salary)
print(gender_2.salary)
print(gender_1.gender)
print(gender_2.gender)
