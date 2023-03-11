# Generated by Django 4.1.7 on 2023-03-11 06:08

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=sorl.thumbnail.fields.ImageField(upload_to='photos/category_icon/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='certificate_photo',
            field=sorl.thumbnail.fields.ImageField(upload_to='photos/certificate/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='video',
            field=models.FileField(upload_to='videos/lecture_video/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=sorl.thumbnail.fields.ImageField(upload_to='photos/socialmedia_icon/%Y/%m/%d/'),
        ),
    ]