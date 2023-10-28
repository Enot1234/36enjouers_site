from django.db import models


class school(models.Model):
    FIO = models.CharField("ФИО", max_length=70)
    tel = models.IntegerField("Телефон")
    email = models.EmailField("email")
    INN = models.PositiveIntegerField("INN")
    name = models.CharField("Название организации", max_length=50)
    adress = models.CharField("Адрес организации", max_length=200)
    user = models.CharField("Пользователь", max_length=50)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организация"
