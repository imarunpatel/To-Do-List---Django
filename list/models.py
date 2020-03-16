from django.db import models
from django.utils import timezone

class Todo_list(models.Model):
    title = models.CharField(max_length=200)
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title