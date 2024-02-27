# Generated by Django 4.2.1 on 2024-02-27 15:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(message="Telefon raqamingizni kiritishda xatolik bor! Iltimos, to'g'ri raqam kiriting.", regex='^\\+\\d{1,4} \\d{1,15}$')]),
        ),
    ]