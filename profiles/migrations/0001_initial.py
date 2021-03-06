# Generated by Django 3.1 on 2020-08-25 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('roll_no', models.PositiveIntegerField(verbose_name='Roll_no')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('branch', models.CharField(max_length=5, verbose_name='Branch')),
                ('programme', models.CharField(choices=[('Btech', 'Btech'), ('Mtech', 'Mtech'), ('Phd', 'Phd')], default='Btech', max_length=5, verbose_name='Programme')),
                ('email_id', models.EmailField(blank=True, max_length=254, verbose_name='Email ID')),
                ('gender', models.CharField(max_length=6, verbose_name='Gender')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
