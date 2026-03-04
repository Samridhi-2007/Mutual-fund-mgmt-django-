from django.db import models


class Advisor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=200)
    experience_years = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
