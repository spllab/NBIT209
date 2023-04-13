# Author PAUL OFFEI
# Date 4/11/2023
# Program Description: Employee Interface to be used by Payroom Engineering Team

class Employee:
    total_recruitment = 0

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.promotion = False
        Employee.total_recruitment += 1

    def __str__(self):
        return f"Employee ID: {self.id}\nEmployee Name: {self.name}\nEmployee Salary: ${self.salary:.2f}\nPromotion Status: {self.promotion}"
    
    def get_id(self):
        return self.id 
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def set_id(self, new_id):
        self.id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def get_total_recruitment(self = None):
        return Employee.total_recruitment
    
    def increase_salary(self, rate):
        if rate <= 1 and rate >= 0:
            self.salary *= rate
        else:
            self.salary *= rate / 100

    
    def get_promotion(self):
        return self.promotion 
