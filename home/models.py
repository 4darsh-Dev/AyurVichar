from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class PrakrutiResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vata_score = models.IntegerField()
    pitta_score = models.IntegerField()
    kapha_score = models.IntegerField()
    prakruti_type = models.CharField(max_length=20)

    def __str__(self):
        return f'Prakruti Result for {self.user.username}'