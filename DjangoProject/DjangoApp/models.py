from importlib.util import set_loader
from pydoc import describe
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import *



# Create your models here.

# mail validation
def is_Esprit_Email(value):
    if not str(value).endswith('@esprit.tn'):
        raise ValidationError('Please enter an Email Address with @esprit', params={'value': value})
    return value

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(validators=[is_Esprit_Email])  # de base charfield


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Student(User):
    pass


class Coach(User):
    pass


class Projet(models.Model):
    project_name = models.CharField(max_length=50)
    dure = models.IntegerField()
    temps_allocated = models.IntegerField(validators=[MinValueValidator(10, "Minimum time = 10")])
    besoin = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    isValid = models.BooleanField(default=False)
    creator = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='creators'
    )
    supervisor = models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        related_name='supervisors'
    )
    membre = models.ManyToManyField(
        Student,
        # on_delete=models.CASCADE,
        through='MemberShip',
        related_name='membres'
    )  # classe intermediaire nommé memberShip


class MemberShip(models.Model):
    projet = models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        related_name='projets'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='students'
    )

    temps_allocated_by_member = models.IntegerField(default=0)
