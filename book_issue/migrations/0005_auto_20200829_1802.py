# Generated by Django 3.1 on 2020-08-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_issue', '0004_auto_20200828_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissuecode',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookreturn',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
