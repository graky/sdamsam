from django.db import models

class Predmet(models.model):
    class_text = models.CharField(max_length=200)
    def __str__(self):
        return self.class_text

# Create your models here.
