from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(5,"title name must contain at least 5 characters")])
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return f"Todo Items:{self.title}, Description:{self.description}, Deadline:{self.deadline}"
