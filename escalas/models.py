from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Escalas(models.Model):

    class Meta:

        db_table = "escalas"

    codvendedor = models.CharField(max_length=30)
    periodo     = models.CharField(max_length=10)
    valor       = models.CharField(max_length=10)

    def __str__(self):
        return self.codvendedor