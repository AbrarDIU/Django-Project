from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name