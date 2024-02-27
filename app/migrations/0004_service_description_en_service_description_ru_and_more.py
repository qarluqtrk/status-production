# Generated by Django 4.2.1 on 2024-02-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
