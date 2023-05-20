from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry, Point



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    location = models.PointField(srid=4326)

    def set_location(self, latitude, longitude):
        self.location = GEOSGeometry(Point(float(longitude), float(latitude)))

    def get_latitude(self):
        return self.location.y if self.location else None

    def get_longitude(self):
        return self.location.x if self.location else None

