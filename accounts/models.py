from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    PROGRAMME_STATES = (('Btech', 'Btech'),
                        ('Mtech', 'Mtech'),
                        ('Phd', 'Phd'))

    name = models.CharField(max_length=30)
    roll_no = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    branch = models.CharField(max_length=5)
    programme = models.CharField(max_length=5, choices=PROGRAMME_STATES,
                                 default='Btech')
    email_id = models.EmailField(blank=True)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.roll_no

    @classmethod
    def create(cls, name, roll_no, year, branch, programme, gender):
        profile = cls(name=name, roll_no=roll_no, year=year, branch=branch, programme=programme, gender=gender)
        return profile

