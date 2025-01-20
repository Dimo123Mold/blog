from django.db import models


# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"Author({self.name})"


class Post(models.Model):
    title = models.CharField(max_length=52, unique=True)
    body = models.TextField()
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.author})"
