# Generated by Django 4.1.7 on 2023-03-25 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calc', '0004_alter_variable_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='variable',
            name='name_var',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
