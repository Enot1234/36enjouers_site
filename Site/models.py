from django.db import models


class Schools(models.Model):
    FIO = models.TextField("ФИО")
    tel = models.IntegerField("Телефон", max_length=8)
    email = models.EmailField("email")
    INN = models.PositiveIntegerField("Телефон", max_length=10)
    name = models.CharField("Название организации", max_length=50)
    adress = models.TextField("Адрес организации")

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организация"

    def __str__(self):
        return self.name
