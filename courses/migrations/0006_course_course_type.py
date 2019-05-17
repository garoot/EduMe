# Generated by Django 2.2 on 2019-05-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190514_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('academic', 'Academic Learning'), ('practical', 'Practical Learning'), ('tech', 'Tech-Related Courses'), ('theory', 'Theoretical Learning')], default='None', max_length=25),
        ),
    ]
