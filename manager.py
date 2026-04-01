class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id


class Manager(Employee):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age, emp_id)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


m = Manager("John", 35, 201, "HR")
m.display()
