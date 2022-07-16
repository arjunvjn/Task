from django.db import models

# Create your models here.

class UserProfile(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=5)
    zip=models.IntegerField()
    email=models.EmailField()
    web=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.first_name