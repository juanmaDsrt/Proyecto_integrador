from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    def _str_(self): return self.headline
