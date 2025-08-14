from django.db import models
class Restaurant(models.Model):
    name= models.CharField(max_length=200)
    phone_name= models.CharField(max_length=20)
    opening_hours= models.Charfiedl(max_length=255,blank=True,null=True)
    def__str__(self):
        return self.name
        class MenuItem(models.Model):
            name= models.CharField(max_length=200)
            address= models.CharField(max_length=255,blank=True, null=True)
            description= models.TextField()
            price = models.DecimalField(max_digits=6,decimal_places=2)
            image= models.ImageField(upload_to='menu_items/', blank=True,null=True)
            def__str__(self):
                return self.name
                class ContactSubmission(models.Model):
                    name= models.CharField(max_length=100)
                    emsil= models.EmailField()
                    submitted_at=models.DataTimeField(auto_now_add=True)
                    def__str__(self):
                        return f"Submission by{self.name} on {self.submitted_at.strftime('%Y-%m-%d')}"
class Order(models.Model):
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('processing','Processing'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    )
    def__str__(self):
        return "Order #{self.pk} by {self.customer.username}"
        class Contact(models.Model):
            name= models.CharField(max_length=100)
            email = models.EmailField()
            submitted_at=models.DataTimeField(auto_now_add=True)
            def__str__(self):
                return self.name
class MenuItem(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    price= models.DecimalField(max_digits=6,decimal_places=2)
    def__str__(self):
        return self.name
class Location(models.Model):
    address= models.CharField(max_length=255)
    city= models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code=models.CharField(max_length=10)
    def__str__(self):
        return f"{self.address},{self.city}"