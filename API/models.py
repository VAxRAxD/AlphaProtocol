from django.db import models

class LeaderBoard(models.Model):
    email=models.EmailField()
    story=models.CharField(max_length=1)
    name=models.CharField(max_length=50, null=True)
    level=models.IntegerField(blank=True,null=True)
    day=models.CharField(max_length=10,default="1")
    completion=models.FloatField(blank=True,null=True)

    def __str__(self) -> str:
        return self.email