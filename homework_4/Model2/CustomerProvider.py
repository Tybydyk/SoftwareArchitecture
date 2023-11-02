
from HomeWorks.homework_4.Model2.DataBase import DataBase
from HomeWorks.homework_4.Model2.Customer import Customer

class CustomerProvider:
    def __init__(self, database: DataBase, customer: Customer):
        self.database = database
        self.customer = customer

    def getCustomer(self, customer):
        pass

