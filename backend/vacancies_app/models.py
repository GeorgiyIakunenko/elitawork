from django.core.exceptions import ValidationError
from django.db import models


def validate_svg_file(value):
    # You can add more specific SVG validations here if needed.
    if not value.name.endswith('.svg'):
        raise ValidationError("Only SVG files are allowed.")


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Позиции")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    important = models.BooleanField(verbose_name="Отметить как важную")
    picture = models.ImageField(upload_to="positions", verbose_name="Картинка")
    salary = models.CharField(max_length=100, verbose_name="Зарплата")
    location = models.CharField(max_length=100, verbose_name="Город, Страна")
    note = models.CharField(blank=True, null=True, max_length=100, verbose_name="Примечание (если есть)")
    short_description = models.TextField(max_length=300, verbose_name="Краткое описание для мета тега, максимум 300 символов")
    description = models.TextField(verbose_name="Description")

    position_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"
        ordering = ['position_order']


class MessengerPlatform(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название (Viber, Telegram и т.д.)")
    logo = models.FileField(verbose_name="Логотип", validators=[validate_svg_file])

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
    job_position = models.CharField(max_length=50, verbose_name="Должность")
    contacts = models.ManyToManyField(Contact, verbose_name="Контакты")
    positions = models.ManyToManyField(Position, blank=True, verbose_name="Позиции")

    manager_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"
        ordering = ['manager_order']
