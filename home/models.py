from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class PrakrutiResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    vata_score = models.IntegerField()
    pitta_score = models.IntegerField()
    kapha_score = models.IntegerField()
    prakruti_type = models.CharField(max_length=50)


