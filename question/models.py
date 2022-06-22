from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=50)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content