# Author PAUL OFFEI
# Date 4/11/2023
# Program Description: Testing Application for LinkedList

from slinkedlist import LinkedList
import singlylinkedlist as sll


#students_age = LinkedList()
# students_age.insert(23)
# students_age.insert(25)
# students_age.insert(19)
# students_age.append(40)
# students_age.append(60)
# print(students_age.print_item())

Student_email = sll.LinkedList()
Student_email.add("offei@gmail.com")
Student_email.add("paul@gmail.com")
print(Student_email)
print(len(Student_email))
Student_email.remove_first()
print(Student_email)
print(len(Student_email))
Student_email.add_last("esi@gmail.com")
Student_email.add_last("jeff@gmail.com")
print(Student_email)
print(len(Student_email))