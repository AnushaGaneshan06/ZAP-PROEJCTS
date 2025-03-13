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
    





