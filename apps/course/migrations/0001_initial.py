# Generated by Django 4.1.7 on 2023-03-10 11:31

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('icon', models.ImageField(upload_to='photos/category_icon%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('certificate_photo', models.ImageField(upload_to='photos/certificate%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('badge_id', models.CharField(blank=True, choices=[('bestseller', 'bestseller'), ('recommended', 'recommended')], max_length=20, null=True)),
                ('original_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Discount')),
                ('discount_expire_date', models.DateField()),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('ranking', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Ranking')),
                ('comment_text', ckeditor.fields.RichTextField(verbose_name='comment')),
                ('status', models.IntegerField(verbose_name='status')),
            ],
            options={
                'verbose_name': 'Course Comment',
                'verbose_name_plural': 'Course Comments',
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('video_duration', models.TimeField()),
                ('photo', models.ImageField(upload_to='photos/interviews%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Interview',
                'verbose_name_plural': 'Interviews',
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('is_paid', models.BooleanField()),
                ('order', models.IntegerField()),
                ('video', models.FileField(upload_to='videos/lecture_video%Y%m%d/')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Lecture',
                'verbose_name_plural': 'Lectures',
            },
        ),
        migrations.CreateModel(
            name='LectureComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('comment_text', models.TextField(verbose_name='Comment')),
                ('status', models.IntegerField()),
                ('index', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Lecture Comment',
                'verbose_name_plural': 'Lecture Comments',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('icon', models.ImageField(upload_to='photos/socialmedia_icon%Y/%m/%d/')),
                ('link', models.URLField()),
                ('redirects', models.IntegerField()),
                ('order', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=100)),
                ('index', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LectureViewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lecture')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
