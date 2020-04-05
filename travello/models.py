from django.db import models

# Create your models here.

















#This models.py is ment for database access hoever yo can also retrive data from python code

class Destination:

    def __init__(self,name,description,price,image,offer = False):
        self.name = name
        self.img = image
        self.desc = description
        self.price = price
        self.offer = offer

