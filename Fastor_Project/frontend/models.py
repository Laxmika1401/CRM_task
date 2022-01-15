from django.db import models

# Create your models here.

class Teachers(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    field = models.BooleanField()
    def __str__(self):
        return self.name
    
# 0 means Private
# 1 means Public