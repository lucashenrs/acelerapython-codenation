from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee(ABC):
    WORKING_HOURS = 8
    BONUS = 0.15
    
    @classmethod
    def get_hours(self):   
        return Employee.WORKING_HOURS

    def __init__(self, code, name, salary, department):
        self.name = name
        self.salary = salary
        self.__department = department

    def get_departament(self):
        return self.__department.name
    
    def set_departament(self, new_dept):
        self.__department = new_dept

    @abstractmethod
    def calc_bonus(self):
        pass

class Manager(Employee):
    def __init__(self, code, name, salary):
        Employee.__init__(self, code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * Employee.BONUS


class Seller(Employee):
    
    def __init__(self,code, name, salary):
        Employee.__init__(self, code, name, salary, Department('sellers', 2))
        self.__sales = 0
    
    def get_sales(self):
        return self.__sales
    
    def put_sales(self, value):
        self.__sales += value
    
    def calc_bonus(self):
        return self.__sales * Seller.BONUS
         
