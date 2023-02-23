from django.db import models

# Create your models here.
#Tables
class Tasks(models.Model):
    title=models.CharField(max_length=200)
    Description=models.TextField(max_length=250,default=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title