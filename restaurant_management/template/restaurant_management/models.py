from django.db import models
class Restaurant(models.Model):
    name= models.CharField(max_length=200)
    phone_name= models.CharField(max_length=20)
    def__str__(self):
        return self.name
