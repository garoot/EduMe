# Generated by Django 2.2 on 2019-04-29 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190429_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_rating',
            field=models.FloatField(null=True),
        ),
    ]