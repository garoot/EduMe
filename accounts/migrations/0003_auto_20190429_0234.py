# Generated by Django 2.2 on 2019-04-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190429_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorreport',
            name='number_of_students',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='instructorreport',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]