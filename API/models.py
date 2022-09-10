from django.db import models

class LeaderBoard(models.Model):
    id=models.CharField(max_length=4, primary_key=True)
    email=models.EmailField()
    level=models.IntegerField(blank=True,null=True)
    time=models.TimeField(blank=True,null=True)

    def __str__(self) -> str:
        return self.email