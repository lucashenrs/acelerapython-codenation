from abc import ABC, abstractmethod

class Department(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee(ABC):
    '''Esta é a classe mãe e 
    não pode ser instanciada diretamente
    '''
    WORKING_HOURS = 8
    BONUS = 0.15
    
    @classmethod
    def get_hours(self):   
        '''Retorna a carga horária diária'''
        return Employee.WORKING_HOURS

    def __init__(self, code, name,
                salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    def get_department(self):
        '''Retorna o nome do departamento do empregado.'''
        return self.__department.name
    
    def set_department(self, new_dept, new_dept_code):
        '''Atualiza o departamento do empregado.
        Argumento:
            -new_dept = nome do departamento 
            -new_dept_code = codigo do departamento
        '''
        self.__department.name = new_dept
        self.__department.code = new_dept_code

    @abstractmethod
    def calc_bonus(self):
        pass

class Manager(Employee):
    """Classe Manager, define objeto do departamento 'managers'

    Argumentos:
        - code
        - name
        - salary
    """
    def __init__(self, code, name, salary):
        Employee.__init__(
            self, code, name, salary,
            department= Department('managers', 1))

    def calc_bonus(self):
        '''Calcula bonus com base no salário
            Bonus = 0.15 * Salário
        '''        
        return self.salary * Employee.BONUS


class Seller(Employee):
    """Classe Seller, define objeto do departamento 'sellers'

    Argumentos:
        - code
        - name
        - salary
    """

    def __init__(self, code, name, salary): # Método construtor
        Employee.__init__(self, code, name, 
        salary, department= Department('sellers', 2))
        self.__sales = 0
    
    def get_sales(self):
        '''Retorna o valor total vendido pelo objeto vendedor.'''
        return self.__sales
    
    def put_sales(self, value):
        '''Adiciona valor das vendas do objeto vendedor.
        Argumento:
            - value
        '''
        self.__sales += value
    
    def calc_bonus(self):
        '''Calcula bonus com base nas vendas
            Bonus = 0.15 * Vendas
        '''
        return self.__sales * Employee.BONUS