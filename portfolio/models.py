from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title

