from django.db import models
from django.conf import settings


class Test(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=100)
    link = models.CharField("Ссылка", max_length=200)

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=100)
    link = models.CharField("Ссылка", max_length=200)

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

class Study(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=100)
    link = models.CharField("Ссылка", max_length=200)

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Обучение"
        verbose_name_plural = "Курсы"
