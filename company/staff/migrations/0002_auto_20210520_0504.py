# Generated by Django 3.0.7 on 2021-05-19 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
