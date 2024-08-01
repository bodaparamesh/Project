from django.db import models

# Create your models here.
class Marks(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=20)
    subject1=models.FloatField()
    subject2=models.FloatField()
    subject3=models.FloatField()