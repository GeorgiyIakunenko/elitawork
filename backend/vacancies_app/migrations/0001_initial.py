# Generated by Django 4.2.4 on 2023-08-25 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='Contact number')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Position Name')),
                ('picture', models.ImageField(upload_to='', verbose_name='Picture')),
                ('salary', models.FloatField(verbose_name='Salary in a month')),
                ('location', models.CharField(max_length=100, verbose_name='City, Country')),
                ('note', models.CharField(max_length=100, verbose_name='Note')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='MessengerPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name (Viber, Telegram, etc.)')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logotype')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies_app.contact')),
            ],
        ),
        migrations.CreateModel(
            name='HiringManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('positions', models.ManyToManyField(to='vacancies_app.position')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='hiring_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies_app.hiringmanager'),
        ),
    ]
