from django.db import models
from datetime import datetime

# Model that stores information about Realtor
class Realtor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
