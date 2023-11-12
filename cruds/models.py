from django.db import models
# Create your models here.


class Profile(models.Model):
    FullName = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250)
    Phone = models.CharField(max_length=12)
    Update = models.DateTimeField(auto_now=True)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FullName
