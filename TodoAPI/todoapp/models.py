from django.db import models
from django.db import models


class Todo(models.Model):
    tid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.title}"