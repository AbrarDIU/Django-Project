from django.db import models

from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category) # akta post onek gulo category te thakte pare and akta category onek gulo post e thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # akta post er ekjon author thakbe, but akta author onek gulo post likhte parbe
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f"{self.title} - {self.author.name}"