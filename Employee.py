import re
from Person import Person
from Car import Car
class Employee(Person):


    def __init__(self,name,money,id=0,distanceToWork=0 ):
        super(Employee,self).__init__(name,money)
        self._car = None
        self.__email = None
        self.id=id
        self._salary=1000
        self.distanceToWork=distanceToWork


        #sleep method
    def sleep(self,hours):
        if(hours == 7):
            self._mood= self._mood[0]
        elif(hours < 7):
            self._mood= self._mood[1]
        else:
            self._mood= self._mood[2]
        #eat Method
    def eat(self,meals):
        if(meals == 3):
            self._healthRate="100%"
        elif(meals == 2):
            self._healthRate="75%"
        elif(meals == 1):
            self._healthRate = "50%"
        else:
            print("you will die")
        #buy method
    def buy(self,items):
        self.money-=items*10

        #work method
    def work(self, hours):
        if (hours == 8):
            self._mood= self._mood[0]
        elif (hours >8):
            self._mood= self._mood[1]
        else:
            self._mood= self._mood[2]
        #drive method
    def drive(self, distance):
        if self._car.fuelRate == 0:
            self.refuel()
        self._car.run(self._car.velocity,distance)
       #refule method
    def refuel(self,gasAmount=100):
        self._car.fuelRate(gasAmount)
       #email method
    def sent_email(self):
        pass


    ##getter and setter methods
    def getMood(self):
        return self._mood
    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car

    # @property
    def getemail(self):
        return self._email

    # @email.setter
    def setemail(self, email):
        # match = re.match(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$", email)
        if re.fullmatch("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",email):
            self.__email = email
        else:
            self.__email = "none"

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary > 1000:
            self.__salary = salary