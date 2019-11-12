from django.db import models


class CPU(models.Model):

    class Meta:
        verbose_name_plural = "CPUs"

    TYPES = (
        ('h', 'High-End'),
        ('m', 'Middle'),
        ('l', 'Low-End')
    )

    name = models.TextField()
    price = models.FloatField()
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self): return self.name
