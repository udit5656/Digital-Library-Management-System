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
    name = models.CharField(max_length=30, verbose_name='Name')
    roll_no = models.PositiveIntegerField(verbose_name='Roll_no')
    year = models.PositiveIntegerField(verbose_name='Year')
    branch = models.CharField(max_length=5, verbose_name='Branch')
    programme = models.CharField(max_length=5, choices=PROGRAMME_STATES,
                                 default='Btech', verbose_name='Programme')
    email_id = models.EmailField(blank=True, verbose_name='Email ID')
    gender = models.CharField(max_length=6, verbose_name='Gender')
    profile_photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, user, name, roll_no, gender, year, branch, programme, email_id):
        profile = cls(user=user, name=name, roll_no=roll_no, gender=gender, year=year, branch=branch,
                      programme=programme,
                      email_id=email_id)
        return profile
