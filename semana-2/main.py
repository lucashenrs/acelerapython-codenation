from abc import ABC, abstractmethod

class Department(ABC):
    def __init__(self, name, code):
        self.__department_name = name
        self.__department_code = code

    def get_department(self):
            '''Retorna o nome do departamento do empregado.'''
            return self.__department_name
    
    def get_departament_code(self):
            '''Retorna o código do departamento do empregado.'''
            return self.__department_code
    
    def set_departament(self, new_dept, new_dept_code):
        '''Atualiza o departamento do empregado.
        Argumento:
            -new_dept = nome do departamento 
            -new_dept_code = codigo do departamento
        '''
        self.__department_name = new_dept
        self.__department_code = new_dept_code
    
    @abstractmethod
    def calc_bonus(self):
        pass

class Employee(ABC):
    '''Esta é a classe mãe e 
    não pode ser instanciada diretamente
    '''
    BONUS = 0.15
    
    def __init__(self, code, name,
                salary):
        self.name = name
        self.salary = salary
        #self.__department = Department()
        self.__working_hours = 8
    
    def get_hours(self):   
        '''Retorna a carga horária diária'''
        return self.__working_hours
    
    @abstractmethod
    def calc_bonus(self):
        pass

class Manager(Employee, Department):

    """Classe Manager, define objeto do departamento 'managers'

    Argumentos:
        - code
        - name
        - salary
    """
    def __init__(self, code, name, salary):
        Employee.__init__(
            self, code, name, salary)
        Department.__init__(self, 'managers', 1)
        
    def calc_bonus(self):
        '''Calcula bonus com base no salário
            Bonus = 0.15 * Salário
        '''        
        return self.salary * Employee.BONUS


class Seller(Employee, Department):
    """Classe Seller, define objeto do departamento 'sellers'

    Argumentos:
        - code
        - name
        - salary
    """

    def __init__(self, code, name, salary):
        Employee.__init__(self, code, name, 
        salary)
        Department.__init__(self, 'sellers', 2)
        
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