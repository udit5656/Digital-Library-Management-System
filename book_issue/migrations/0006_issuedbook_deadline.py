# Generated by Django 3.1 on 2020-08-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_issue', '0005_auto_20200829_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='deadline',
            field=models.DateField(blank=True, default=None),
            preserve_default=False,
        ),
    ]
