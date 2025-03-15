from django.db import models
from django.contrib.auth.models import User


# ------------------district------------------- 
class District(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
# --------------temple---------------- 
class Temple(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    address = models.TextField()
    google_maps_link = models.URLField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    pooja_timings = models.TextField()
    facilities = models.TextField(blank=True, null=True)  # Example: Parking, Annadhanam
    contact_number = models.CharField(max_length=15)
    main_image = models.ImageField(upload_to='temple_images/', blank=True, null=True)  # Image Upload
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


# -----------------

class Booking(models.Model):
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    purpose = models.TextField()

    def __str__(self):
        return f"Booking for {self.temple.name} by {self.name} on {self.date}"



