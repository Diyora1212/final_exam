from django.db import models

# employees/models.py
from django.db import models


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

