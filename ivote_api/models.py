from django.db import models

# Create your models here.
class Vote(models.Model):

    state_voter_id = models.CharField(max_length=15, default='00')
    county_code = models.CharField(max_length=10, default='00')
    election_date = models.CharField(max_length=15, default="00")