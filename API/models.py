from django.db import models

class LeaderBoard(models.Model):
    id=models.CharField(max_length=4, primary_key=True)
    name=models.CharField(max_length=50, null=True)
    email=models.EmailField()
    level=models.IntegerField(blank=True,null=True)
    completion=models.FloatField(blank=True,null=True)

    def __str__(self) -> str:
        return self.email