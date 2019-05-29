# Generated by Django 2.2 on 2019-05-29 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardPaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('card_number', models.IntegerField()),
                ('expriy_date', models.DateField()),
                ('security_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstructorBankingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=455)),
                ('banking_info', models.CharField(max_length=455)),
            ],
        ),
        migrations.CreateModel(
            name='InstructorCoursesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InstructorReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_revenue', models.FloatField(max_length=200, null=True)),
                ('number_of_students', models.IntegerField(null=True)),
                ('rating', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstructorResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('None', 'None'), ('D', 'Diploma'), ('B', "Bachelor's Degree"), ('M', "Master's Degree"), ('PH', 'PhD')], default='None', max_length=2)),
                ('major', models.CharField(max_length=344)),
                ('experience', models.TextField(help_text='Briefly, describe your background knowledge related to the topics you want to teach')),
                ('status', models.CharField(choices=[('None', 'None'), ('submitted', 'Submitted'), ('processed', 'Decision has been made')], default='None', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PayPalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilename', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=254)),
                ('nationality', models.CharField(max_length=255)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('is_student', models.BooleanField(default=True)),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_promoter', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('photo', models.ImageField(null=True, upload_to='users/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WishListCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
