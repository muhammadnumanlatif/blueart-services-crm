from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # SOURCE_CHOICES = (
    #     ('YouTube','YouTube'),
    #     ('Facebook','Facebook'),
    #     ('Instagram','Instagram'),
    #     ('Google','Google'),
    #     ('Newsletter','Newsletter'),
    # )

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
