from django.db import models

class Predmet(models.Model):
    predmet_text = models.CharField(max_length=200)
    def __str__(self):
        return self.predmet_text

# Create your models here.
