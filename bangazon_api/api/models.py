from django.db import models


class Customer(models.Model):
    """Class designed for creating customers within database

    Methods:

    Author: [Talbot Lawrence]
    """
    FirstName = models.CharField(max_length=44)
    LastName = models.CharField(max_length=44)
    JoinDate = models.DateField(max_length=20)
    InactiveDate = models.DateField(max_length=20)
    Inactive = models.IntegerField()

class ProductType(models.Model):
    """ Class to expose the product types to the API.

    Author: James Tonkin
    """
    name = models.CharField(max_length=255)


class PaymentType(models.Model):
    '''
    A class that adds a PaymentType table to the database.

    Arguments:
    A model provided by django framework.

    Author:
    wocaldwell
    '''
    AccountNumber = models.IntegerField()
    Name = models.CharField(max_length=255)
    CustomerId = models.ForeignKey(Customer)


class Product(models.Model):
    """Class for adding product table to the database

    Methods:

    Author: Aaron Barfoot
    """
    CategoryId = models.ForeignKey(ProductType)
    CustomerId = models.ForeignKey(Customer)
    Title = models.CharField(max_length=55)
    Description = models.CharField(max_length=150)
    Price = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    """This class defines what bangazon's Order table within the database will look like
        You need both PaymentType and Customer table for this to work correctly

    Attributes:
        PaymentTypeId (INT): Payment Type Id referencing Payment Type table (FK)
        CustomerId (INT): Customer Id referencing Customer table (FK)

    Author: Taylor Perkins
    """
    PaymentTypeId = models.ForeignKey(PaymentType)
    CustomerId = models.ForeignKey(Customer)

class ProductOrder(models.Model):
    """This class is a join table for both the Product and Order Table within Bangazon db
        You will need both the Product and Order tables created for this table to apply

    Attributes:
        ProductId (INT): Product Id referencing Product table (FK)
        OrderId (INT): Order Id referencing Order table (FK)

    Author: Taylor Perkins
    """
    ProductId = models.ForeignKey(Product)
    OrderId = models.ForeignKey(Order)


class Department(models.Model):
    """
    Class for adding product table to the database


    Name = models.CharField(max_length=55)
    Budget = models.DecimalField(max_digits=6, decimal_places=2)

    Author:
    wocaldwell
    """

class Training(models.Model):
	"""Class for adding training program to the database

	Methods:

	Author: Aaron Barfoot
	"""
	Title = models.CharField(max_length=55)
	StartDate = models.DateField(max_length=10)
	EndDate = models.DateField(max_length=10)
	Max = models.IntegerField()

class EmployeeTraining(models.Model):
    """This class is a join table for both the Employee and Training Table within Bangazon db
        You will need both the Employee and Training tables created for this table to apply

    Attributes:
        EmployeeId (INT): Employee Id referencing Employee table (FK)
        TrainingId (INT): Training Id referencing Training table (FK)

    Author: Aaron Barfoot
    """
    EmployeeId = models.ForeignKey(Employee)    
    TrainingId = models.ForeignKey(Training)   






