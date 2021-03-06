# Generated by Django 3.1 on 2020-09-04 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_issue', '0008_latefine'),
    ]

    operations = [
        migrations.AddField(
            model_name='latefine',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookreturn',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Returned Date'),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Issued Date'),
        ),
    ]
