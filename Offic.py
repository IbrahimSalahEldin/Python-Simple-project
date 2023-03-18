from Employee import  Employee
class Offic:
    __count = 0

    def __init__(self, name, Employees):
        self.name = name
        self.Employees = Employees

    def get_All_employees(self):
        for emp in self.Employees:
            print(emp.id)

    def get_employee(self, id):
        for emp in self.Employees:
            if emp.id == id:
                return emp

    def hire(self, emp):
        self.Employees.append(emp)
        Offic.__count += 1

    def fire(self, id):
        for emp in self.Employees:
            if emp.id == id:
                self.Employees.remove(emp)
        Offic.__count -= 1

    def deduct(self, id, deduction):
        for emp in self.Employees:
            if emp.id == id:
                emp.salary -= deduction

    def reward(self, id, rewards):
        for emp in self.Employees:
            if emp.id == id:
                emp.salary += rewards

    # @classmethod
    # def employeesNum(cls):
    #     return cls.count
    #
    # @classmethod
    # def change_emps_num(cls, num):
    #     cls.count = num
