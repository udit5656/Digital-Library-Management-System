# Generated by Django 3.1 on 2020-08-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=50)),
                ('publisher_name', models.CharField(blank=True, max_length=50)),
                ('pages', models.PositiveIntegerField(blank=True, null=True)),
                ('pub_year', models.PositiveIntegerField()),
                ('books_available', models.IntegerField()),
            ],
        ),
    ]
