from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name