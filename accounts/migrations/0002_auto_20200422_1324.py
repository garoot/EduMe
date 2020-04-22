# Generated by Django 3.0 on 2020-04-22 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloglistblog',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog'),
        ),
        migrations.AddField(
            model_name='bloglistblog',
            name='blog_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='accounts.BloggerBlogList'),
        ),
        migrations.AddField(
            model_name='bloggerbloglist',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blog_list', to='accounts.Profile'),
        ),
    ]