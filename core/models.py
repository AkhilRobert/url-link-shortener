from django.db import models


class CoreModel(models.Model):
    original_url = models.TextField()
    shrink_id = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.original_url
