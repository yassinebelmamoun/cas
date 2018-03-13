""" Client Model """
from django.db import models
from utilisateur.models import User


class Client(models.Model):
    seller = models.ForeignKey(User)
    email = models.EmailField('Addresse éléctronique')
    first_name = models.CharField('Prénom', max_length=30)
    last_name = models.CharField('Nom', max_length=30)
    phone_number = models.CharField('Numéro de téléphone', max_length=30)

    CIVILITY_CHOICES = (
        ('M', 'Monsieur'),
        ('Mme', 'Madame'),
        ('Mlle', 'Mademoiselle'),
    )
    civility = models.CharField(max_length=4, choices=CIVILITY_CHOICES)

    MARIAL_STATUS_CHOICES = (
        ('Célibataire', 'Célibataire'),
        ('Marié(e)', 'Marié(e)'),
        ('Veuf(ve)', 'Veuf(ve)'),
        ('Divorcé(e)', 'Divorcé(e)'),
    )
    marital_status = models.CharField(max_length=250, choices=MARIAL_STATUS_CHOICES)
    birthday = models.DateField()
    postcode = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250)
    social_security_number = models.CharField(max_length=255)
    social_security_organism_name = models.CharField(max_length=255)
    social_security_organism_code = models.CharField(max_length=255)

    # Creation/ Update DateTime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_courtier(self):
        return self.seller.courtier
