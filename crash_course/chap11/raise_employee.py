
from  employee import Employee

my_employee1 = Employee('luis', 'cavanzo',10000)
my_employee2 = Employee('leon', 'kennedy',10000)
my_employee3 = Employee('cloud', 'strife', 10000)
my_employee3.give_raise()
my_employee3.give_raise(10000)
print(my_employee1)
print(my_employee2)
print(my_employee3)
