from Person import  Person
from Employee import  Employee
from Car import Car
from Offic import Offic
car1 = Car("BMW")
car1.setvelocity(150)
car1.setfuelRate(200)
# print(car1.getvelocity())
car2 = Car("marsides")
car2.setvelocity(140)
car2.setfuelRate(180)

employees = []
#first object
em1=Employee("ali",5000,1,150)
em1.salary=8000
em1.car=car1

#second object
em2=Employee("ahmed",7000,2,150)
em2.salary=8000
em2.car=car2

employees.append(em1)
employees.append(em2)

for emp in employees:
    print(emp.name)

offic1= Offic("IT",employees)

print(offic1.get_employee(1))
