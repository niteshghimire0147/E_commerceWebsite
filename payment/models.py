from django.db import models
from django.conf import settings

# Create your models here.
class Khalti(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/khalti')
    Refrence_Code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username