# Author PAUL OFFEI
# Date 4/11/2023
# Program Description: Using the employee and manager library for  Payroom product

from employee import Employee
from manager import Manager

joel = Employee("10559900", "Joel", 12000)
jeff = Employee("10779954", "Jeffery", 9567.988)
promise = Employee("10441256", "Promise", 10875.77654)

print(joel)
print("=======================================================")
print(jeff)
print("=======================================================")
print(promise)
print("=======================================================")

jeff.increase_salary(0.15)
print(jeff)
print("=======================================================")

promise.promotion = True
print(promise)
print("=======================================================")

print(Employee.total_recruitment)
print("=======================================================")
print(promise.get_total_recruitment())
print("=======================================================")


martin = Manager("17001788", "Martin", 20112.975, 120765.98)
print(martin)
print("=======================================================")
martin.increase_salary(25)
print(martin)
print("=======================================================")