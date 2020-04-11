# Generated by Django 3.0 on 2020-04-11 17:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255)),
                ('blog_description', models.TextField(blank=True, max_length=255, null=True)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('blog_picture', models.ImageField(blank=True, null=True, upload_to='blogs/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_topic', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='blogs.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=355)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.Blog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blogs.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger_bloglist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogs', to='accounts.BloggerBlogList'),
        ),
    ]
