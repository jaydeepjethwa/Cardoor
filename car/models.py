from django.db import models
from django.conf import settings


class Car(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    carModel = models.CharField(max_length=50)
    carNumber = models.CharField(max_length=20)
    rate = models.IntegerField()
    seat = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="car/images")
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.carNumber
