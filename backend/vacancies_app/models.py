from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=5, unique=True, verbose_name="Название (UAH, HUF и т.д.)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Позиции")
    important = models.BooleanField(verbose_name="Отметить как важную")
    picture = models.ImageField(upload_to="positions", verbose_name="Картинка")
    salary = models.FloatField(verbose_name="Зарплата в месяц")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Валюта")
    location = models.CharField(max_length=100, verbose_name="Город, Страна")
    note = models.CharField(blank=True, null=True, max_length=100, verbose_name="Примечание (если есть)")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"


class MessengerPlatform(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название (Viber, Telegram и т.д.)")
    logo = models.ImageField(verbose_name="Логотип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мессенджер"
        verbose_name_plural = "Мессенджеры"


class Contact(models.Model):
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    messenger_platforms = models.ManyToManyField(MessengerPlatform, verbose_name="Мессенджеры")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    photo = models.ImageField(null=True, upload_to="managers", verbose_name="Фото")
    contacts = models.ManyToManyField(Contact, verbose_name="Контакты")
    positions = models.ManyToManyField(Position, verbose_name="Позиции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"
