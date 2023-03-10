# Generated by Django 4.1.7 on 2023-03-10 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('payment_type_id', models.CharField(blank=True, choices=[('uzcard', 'payme'), ('humo', 'apelsin'), ('visa', 'visa'), ('click', 'click'), ('mastercard', 'mastercard'), ('kpay', 'kpay'), ('cash', 'cash')], max_length=20, null=True, verbose_name='Payment_type')),
                ('payed_at', models.DateTimeField(blank=True, null=True, verbose_name='Payment date')),
                ('payment_status', models.CharField(choices=[('purchased', 'purchased'), ('not puchased', 'not puchased'), ('in progres', 'in progres')], default='not puchased', max_length=20, verbose_name='Payment Status')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Course')),
                ('payer_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Payer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
