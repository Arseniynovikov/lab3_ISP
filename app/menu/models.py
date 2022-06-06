from django.contrib.postgres.fields import ArrayField
from django.db import models


class Menuitem(models.Model):
    name = models.CharField('Название', max_length=200)
    components = ArrayField(
            models.CharField('Продукт', max_length=200),
    )
    price = models.FloatField('Цена')

    def __str__(self):
        return self.name

