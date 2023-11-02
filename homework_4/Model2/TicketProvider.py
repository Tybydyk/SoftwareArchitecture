
from HomeWorks.homework_4.Model2.PaymentProvider import PaymentProvider
from HomeWorks.homework_4.Model2.DataBase import DataBase


class TicketProvider:
    def __init__(self, paymentProvider: PaymentProvider, database: DataBase):
        self.database = database
        self.paymentProvider = paymentProvider

    def searchTicket(self, customerId):
        pass

    def buyTicket(self, customerId, ticketId, paymentCustomerData):
        pass

