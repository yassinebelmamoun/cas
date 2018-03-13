""" Courtier Model """
from django.db import models


class Courtier(models.Model):
    """ Courtier is a team of seller """
    code_courtier = models.CharField(max_length=255)
    cabinet_name = models.CharField(max_length=255)
    orias_code = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    bic = models.CharField(max_length=255)

    """ Director: """
    director_firstname = models.CharField(max_length=255)
    director_lastname = models.CharField(max_length=255)
    director_emailaddress = models.CharField(max_length=255)

    """ Inspector: """
    inspector_name = models.CharField(max_length=255)
    inspector_phonenumber = models.CharField(max_length=255)
    inspector_emailaddress = models.CharField(max_length=255)

    # Creation/ Update DateTime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cabinet_name

    def get_team(self):
        from utilisateur.models import User
        return User.objects.filter(courtier=self)

    def get_team_size(self):
        from utilisateur.models import User
        return User.objects.filter(courtier=self).count()

    def director_full_name(self):
        return '{} {}'.format(self.director_firstname, self.director_lastname)
