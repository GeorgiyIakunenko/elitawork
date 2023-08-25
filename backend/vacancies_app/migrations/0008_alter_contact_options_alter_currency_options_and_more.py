# Generated by Django 4.2.4 on 2023-08-25 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_app', '0007_remove_manager_picture_manager_photo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Валюта', 'verbose_name_plural': 'Валюты'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Менеджер', 'verbose_name_plural': 'Менеджеры'},
        ),
        migrations.AlterModelOptions(
            name='messengerplatform',
            options={'verbose_name': 'Мессенджер', 'verbose_name_plural': 'Мессенджеры'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Позиция', 'verbose_name_plural': 'Позиции'},
        ),
        migrations.AddField(
            model_name='position',
            name='slug',
            field=models.SlugField(default='lol', max_length=100, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='messenger_platforms',
            field=models.ManyToManyField(to='vacancies_app.messengerplatform', verbose_name='Мессенджеры'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=5, unique=True, verbose_name='Название (UAH, HUF и т.д.)'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='contacts',
            field=models.ManyToManyField(to='vacancies_app.contact', verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='photo',
            field=models.ImageField(null=True, upload_to='managers', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='positions',
            field=models.ManyToManyField(to='vacancies_app.position', verbose_name='Позиции'),
        ),
        migrations.AlterField(
            model_name='messengerplatform',
            name='logo',
            field=models.ImageField(upload_to='', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='messengerplatform',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название (Viber, Telegram и т.д.)'),
        ),
        migrations.AlterField(
            model_name='position',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies_app.currency', verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='position',
            name='important',
            field=models.BooleanField(verbose_name='Отметить как важную'),
        ),
        migrations.AlterField(
            model_name='position',
            name='location',
            field=models.CharField(max_length=100, verbose_name='Город, Страна'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название Позиции'),
        ),
        migrations.AlterField(
            model_name='position',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Примечание (если есть)'),
        ),
        migrations.AlterField(
            model_name='position',
            name='picture',
            field=models.ImageField(upload_to='positions', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='position',
            name='salary',
            field=models.FloatField(verbose_name='Зарплата в месяц'),
        ),
    ]
