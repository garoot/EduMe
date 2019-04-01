# Generated by Django 2.1.2 on 2019-03-31 19:26

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('EmailAddress', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('BirthDate', models.DateField(blank=True, max_length=12)),
                ('PhoneNumber', phone_field.models.PhoneField(max_length=31)),
                ('Country', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('UserStatus', models.BooleanField(default=False, verbose_name='user_status')),
                ('InstructorStatus', models.BooleanField(default=False, verbose_name='instructor status')),
            ],
        ),
        migrations.CreateModel(
            name='InstructorCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_id', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CoursesList', to='InstructorAuthentication.Instructor')),
            ],
        ),
    ]
