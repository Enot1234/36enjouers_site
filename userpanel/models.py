from django.db import models
class Test(models.Model):
    title = models.CharField("Название", max_length=100)
    link = models.TextField("Ссылка", max_length=120)

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

class Result(models.Model):
    title = models.CharField("Название", max_length=100)
    link = models.TextField("Ссылка", max_length=120)

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

class Study(models.Model):
    title = models.CharField("Название", max_length=100)
    link = models.TextField("Ссылка", max_length=120)

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Обучение"
        verbose_name_plural = "Курсы"
