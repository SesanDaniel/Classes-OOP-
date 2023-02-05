class Employee:  # Classname
    tax = 1.05 # A class attribute

    def __init__(self, name, salary):
        """ This is the init method, which runs the instance of a class
         everytime the class is instantiated. The __init__ takes "self"
         as first argument followed by any other argument we intend to
         use in class. The self argument refers to each instance of the class. """
        self.name = name
        self.salary = salary

    def greetings_to_employee(self):
        return f"Hi {self.name}, welcome to work!!!"

    def emp_salary(self):
        return int(self.salary)

    def salary_after_monthly_tax(self):
        return self.salary / self.tax


employee_1 = Employee("Daniel", 2000)
# employee_1.name = "Daniel"

print(employee_1.name)
print(employee_1.salary)
print(employee_1.salary_after_monthly_tax())
print(employee_1.greetings_to_employee())
print(Employee.greetings_to_employee(employee_1))


class Dog:
    num_of_dog = 0

    def __init__(self, bark):
        self.bark = bark
        Dog.num_of_dog += 1

    def color(self):
        return "This dog is {} in color".format(self.bark)


print(Dog.num_of_dog)
dog_1 = Dog("Blue")
dog_2 = Dog("Yellow")
dog_3 = Dog("Pink")
print(dog_1.color())
print(dog_2.color())
print(dog_3.color())
print(Dog.num_of_dog)
