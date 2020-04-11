# Generated by Django 3.0 on 2020-04-11 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloggerBlogList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BlogListBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=254)),
                ('nationality', models.CharField(blank=True, max_length=255)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('is_student', models.BooleanField(default=True)),
                ('is_blogger', models.BooleanField(default=False)),
                ('is_promoter', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('instructor_application_status', models.CharField(choices=[('none', 'None'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='None', max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wish_list', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='WishListCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('wish_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='accounts.WishList')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_list', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('purchase_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased_course', to='accounts.PurchaseList')),
            ],
        ),
        migrations.CreateModel(
            name='PayPalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilename', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('payment_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paypal_info', to='accounts.PaymentInfo')),
            ],
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info', to='accounts.Profile'),
        ),
        migrations.CreateModel(
            name='CardPaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('card_number', models.IntegerField()),
                ('expriy_date', models.DateField()),
                ('security_number', models.IntegerField()),
                ('payment_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_info', to='accounts.PaymentInfo')),
            ],
        ),
    ]
