from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.content