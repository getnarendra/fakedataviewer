
# Create your models here.
from django.db import models

class MongoDBConnection(models.Model):
    ENVIRONMENT_CHOICES = (
        ('dev', 'Development'),
        ('staging', 'Staging'),
        ('prod', 'Production'),
    )

    environment = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES)
    host = models.CharField(max_length=100)
    port = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # Add more fields as needed

    def __str__(self):
        return f"{self.environment} - {self.host}:{self.port}"
