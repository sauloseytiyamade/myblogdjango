from django.db import models

class projects(models.Model):
    name = name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    link = models.CharField(max_length=1500)
    tags = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name