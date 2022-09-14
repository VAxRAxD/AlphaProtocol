from django.db import models
from django.utils import timezone
import pytz

IST = pytz.timezone('Asia/Kolkata')

class LeaderBoard(models.Model):
    id=models.CharField(max_length=4, primary_key=True)
    name=models.CharField(max_length=50, null=True)
    email=models.EmailField()
    level=models.IntegerField(blank=True,null=True)
    start=models.TimeField(auto_now_add=True,null=True)
    completion=models.TimeField(blank=True,null=True)

    def __str__(self) -> str:
        return self.email