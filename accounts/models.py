from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

# Create your models here.
from django.db.models.signals import post_save


class Profile(models.Model):
    PROGRAMME_STATES = (('Btech', 'Btech'),
                        ('Mtech', 'Mtech'),
                        ('Phd', 'Phd'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30)
    roll_no = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    branch = models.CharField(max_length=5)
    programme = models.CharField(max_length=5, choices=PROGRAMME_STATES,
                                 default='Btech')
    email_id = models.EmailField(blank=True)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, user, name, roll_no, gender, year, branch, programme, email_id):
        profile = cls(user=user, name=name, roll_no=roll_no, gender=gender, year=year, branch=branch,
                      programme=programme,
                      email_id=email_id)
        return profile
