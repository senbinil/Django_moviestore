from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=200)
    title=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='uploads')
    img.blank=True