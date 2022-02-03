from django.db import models

# Create your models here.

class Message(models.Model):
    
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=140)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=10000)
  
    
    def __str__(self):
        return self.name
    



