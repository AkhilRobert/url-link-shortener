import string
import random
from django.db import models


class CoreModel(models.Model):
    original_url = models.TextField()
    shrink_id = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.shrink_id = self.gen_rand_id()
        return super(CoreModel, self).save(*args, **kwargs)

    def gen_rand_id(self):
        char = string.ascii_letters + string.ascii_lowercase + \
            string.ascii_uppercase + string.digits
        id = ''.join(random.choice(char) for _ in range(6))
        if CoreModel.objects.filter(shrink_id=id).exists():
            return self.gen_rand_id(self)
        return id

    def __str__(self) -> str:
        return self.original_url
