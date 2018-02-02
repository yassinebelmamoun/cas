""" Client Model """
from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """ The client of the seller """

    seller = models.ForeignKey(User)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.Field()
    phone_number = models.Field()
    civility = models.Field()
    marital_status = models.Field()
    birthday = models.Field()
    postcode = models.Field()
    profession = models.Field()
    address = models.Field()
    address_2 = models.Field()
    city = models.Field()
    social_security_number = models.CharField(max_length=255)
    social_security_organism_name = models.CharField(max_length=255)
    social_security_organism_code = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
