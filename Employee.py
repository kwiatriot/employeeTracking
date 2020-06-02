import logging


# Base class for employee creation
class Employee:

    def __init__(self, first, last):
        self.first = first 
        self.last = last

    @property
    def full_name(self):
        return f'{self.first.title()}{self.last.title()}'

    @property
    def email(self):
        return f'{self.first[0].upper()}.{self.last.title()}@companyemail.com'

    


