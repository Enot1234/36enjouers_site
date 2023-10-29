from django.db import models
from django.conf import settings


class school(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    FIO = models.CharField("ФИО", max_length=70)
    tel = models.IntegerField("Телефон")
    email = models.EmailField("email")
    INN = models.PositiveIntegerField("ИНН")
    name = models.CharField("Название организации", max_length=50)
    adress = models.CharField("Адрес организации", max_length=200)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организация"