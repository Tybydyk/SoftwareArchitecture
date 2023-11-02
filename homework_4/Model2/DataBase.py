
from HomeWorks.homework_4.Model2.Ticket import Ticket
from HomeWorks.homework_4.Model2.Customer import Customer

class DataBase:
    def __init__(self, tickets: Ticket, customers: Customer):
        self.tickets = tickets
        self.customers = customers

    def getTickets(self, searchParam=None):
        pass

    def getCustomerTickets(self, customerId):
        pass

    def createTicketOrder(self, customerId, ticketId):
        pass

    def update(self, tickets):
        pass

