from django.db import models
from datetime import datetime
from django.utils.dateparse import parse_date


class PersonneManager(models.Manager):
    """
    Modèle du Manager de modèle Personne
    """
    def create_personne(self, name, first_name, date_of_birth):
        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        delta = datetime.now().date() - date_of_birth
        if delta.days > 365*150:
            too_old = "Personne de plus de 150 ans"
            return too_old
        personne_object = self.create(name=name, first_name=first_name, date_of_birth=date_of_birth)
        return personne_object


class Personne(models.Model):
    """
    Modèle de Personne
    """
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    objects = PersonneManager()
