""" Courtier Model """
from django.db import models


class Courtier(models.Model):
    """ Courtier is a team of seller """

    code_courtier = models.CharField(max_length=255)
    cabinet_name = models.CharField(max_length=255)
    orias_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    postcode = models.Field()
    city = models.CharField(max_length=255)
    country = models.Field()
    phone_number = models.Field()
    email_address = models.Field()
    iban = models.Field()
    bic = models.Field()

    """ Director: """
    director_firstname = models.CharField(max_length=255)
    director_lastname = models.CharField(max_length=255)
    director_emailaddress = models.Field()

    """ Inspector: """
    inspector_name = models.Field()
    inspector_phonenumber = models.Field()
    inspector_emailaddress = models.Field()
