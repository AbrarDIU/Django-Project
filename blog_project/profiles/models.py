from django.db import models
from author.models import Author
# Create your models here.
class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None) # akta profile er ekjon author thakbe, but akta author er ekta profile thakbe

    def __str__(self):
        return self.user_name