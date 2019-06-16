class Employee:
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name.lower() + '@example.com'

    @property
    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return self.fullname


employee_one = Employee('John', 'Doe', 56000)
print(employee_one, employee_one.email, employee_one.__repr__())