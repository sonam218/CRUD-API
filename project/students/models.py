from django.db import models

class Students(models.Model):
    std_name=models.CharField(max_length=50)
    std_class=models.IntegerField()
    mobile_number=models.IntegerField()
    image=models.ImageField()
    address=models.CharField(max_length=100)
    