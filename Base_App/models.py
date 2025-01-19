from django.db import models

# Create your models here.
class ItemCategory(models.Model):
    Category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_name
    

class ItemList(models.Model):
    Item_name = models.CharField(max_length=20)
    Item_description = models.TextField(blank=False)
    Item_price = models.IntegerField()
    Category = models.ForeignKey(ItemCategory, related_name='Item_Category', on_delete=models.CASCADE)
    Item_image = models.ImageField(upload_to='Items/')
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.Item_name

class Order(models.Model):
    pass

class Cart(models.Model):
    pass

class AboutUs(models.Model):
    AboutUs_description = models.TextField(blank=False)

class ContactUs(models.Model):
    pass

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    total_guests = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=False)

    def __str__(self):
        return f"Feedback from {self.name}"