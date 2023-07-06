from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

