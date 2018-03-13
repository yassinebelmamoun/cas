""" Contrat Model """
from django.db import models
from client.models import Client 
from courtier.models import Courtier


class Contract(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    """ Product """
    contract = models.ForeignKey(Contract)
    name = models.CharField(max_length=255)


class CourtierProduct(models.Model):
    """ Product's allowed for Specific Courtier """
    product = models.ForeignKey(Product)
    courtier = models.ForeignKey(Courtier)
    commission = models.Field()
    is_enabled = models.BooleanField()

    # Creation/ Update DateTime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.product, self.courtier)


class ClientProduct(models.Model):
    """ The client subscribe to a product """
    client = models.ForeignKey(Client)
    product = models.ForeignKey(Contract)
    state = models.Field() # Is verified? Signasur or Signature?

    # Creation/ Update DateTime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.client, self.product)

    def get_seller(self):
        """ return the courtier's seller for this contract """
        pass

    def get_courtier(self):
        """ return the courtier of this contract """
        pass
