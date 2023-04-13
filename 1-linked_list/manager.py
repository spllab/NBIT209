# Author PAUL OFFEI
# Date 4/11/2023
# Program Description: Manager Interface to be used by Payroom Engineering Team

from employee import Employee as Employ

class Manager(Employ):

    def __init__(self, id, name, salary, budget):
        super().__init__(id, name, salary)
        self.budget = budget

    def __str__(self):
        return f"{super().__str__()}\nProjects Budget: {self.budget:.2f}"
    
    def get_budget(self):
        return self.budget
    
    def set_budget(self, new_budget):
        self.budget = new_budget