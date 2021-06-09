from django.db import models


class Bike(models.Model):
    name = models.CharField(max_length=100)
    displacement = models.IntegerField()
    maker = models.CharField(max_length=100)

    def __str__(self):
        return self.name
