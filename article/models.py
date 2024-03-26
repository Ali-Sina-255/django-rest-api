from django.db import models

class Journalist(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    biography = models.TextField()
    
    def __str__(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete = models.CASCADE, related_name='article')
    title = models.CharField(max_length=255)
    description = models.TextField()
    main_text = models.TextField()
    published_time = models.DateField()
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    