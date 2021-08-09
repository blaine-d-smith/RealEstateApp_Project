from django.db import models
from datetime import datetime

# Model that stores information about Contacts
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    inquiry_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
