from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime


# Create your models here.
class Vote(models.Model):

    state_voter_id = models.CharField(max_length=15, default='00')
    county_code = models.CharField(max_length=10, default='00')
    election_date = models.CharField(max_length=15, default="00")


class Voter(models.Model):
    state_voter_id = models.CharField(max_length=25, default='00')
    county_voter_id = models.CharField(max_length=25, default='00')
    f_name = models.CharField(max_length=30, default='00')
    m_name = models.CharField(max_length=30, default='00')
    l_name = models.CharField(max_length=30, default='00')
    name_suffix = models.CharField(max_length=10, default='00')
    birthdate = models.CharField(max_length=15, default='00')
    gender = models.CharField(max_length=5, default='00')
    st_num = models.CharField(max_length=15, default='00')
    st_frac = models.CharField(max_length=10, default='00')
    st_name = models.CharField(max_length=50, default='00')
    st_type = models.CharField(max_length=20, default='00')
    unit_type = models.CharField(max_length=15, default='00')
    st_post_direction = models.CharField(max_length=5, default='00')
    st_pre_direction = models.CharField(max_length=5, default='00')
    unit_num = models.CharField(max_length=15, default='00')
    city = models.CharField(max_length=30, default='00')
    state = models.CharField(max_length=10, default='00')
    zip_code = models.CharField(max_length=10, default='00')
    county_code = models.CharField(max_length=20, default='00')
    precinct_code = models.CharField(max_length=20, default='00')
    precinct_part = models.CharField(max_length=20, default='00')
    legislative_district = models.CharField(max_length=10, default='00')
    congressional_district = models.CharField(max_length=10, default='00')
    registration_date = models.CharField(max_length=15, default='00')
    absentee_type = models.CharField(max_length=10, default='00')
    last_voted = models.CharField(max_length=15, default='00')
    status_code = models.CharField(max_length=10, default='00')
    user = models.BooleanField(default=False)

    def get_age_group(self):
        year = datetime.datetime.now().year
        age = year - int(self.birthdate.split('/')[2])
        if age < 25:
            return '18-24'
        elif age < 35:
            return '25-34'
        elif age < 45:
            return '35-44'
        elif age < 55:
            return '45-54'
        elif age < 65:
            return '55-64'
        elif age < 75:
            return '65-74'
        elif age < 85:
            return '75-84'
        else:
            return '85+'

    def get_address(self):

        return f'{self.st_num} {self.st_pre_direction} {self.st_name} {self.st_type} {self.st_post_direction} {self.unit_type}{self.unit_num}, {self.city}, {self.state}, {self.zip_code}'


class Voting_Stats(models.Model):
    county_code = models.CharField(max_length=10, default='00')
    city = models.CharField(max_length=30, default='00')
    voting_freq = ArrayField(models.IntegerField(), size=10,)
    age_group = models.CharField(max_length=20, default='00')

    @staticmethod
    def get_max_votes(rows):
        totals = []
        for i in range(len(rows[0].voting_freq)):
            total = 0
            for row in rows:
                total += row.voting_freq[i]
            totals.append(total)
        sample_size = sum(totals)
        max_votes = len(totals) - 1
        for i in range(len(totals)):
            if (totals[max_votes] / sample_size) < .05:
                max_votes -= 1
            else:
                break
        return max_votes


class Visitor(models.Model):
    state_voter_id = models.CharField(max_length=25, default='00')
    f_name = models.CharField(max_length=30, default='00')
    l_name = models.CharField(max_length=30, default='00')
    birthdate = models.CharField(max_length=15, default='00')
    address = models.CharField(max_length=70, default='00')
    city = models.CharField(max_length=30, default='00')
    county_code = models.CharField(max_length=20, default='00')
    age_group = models.CharField(max_length=20, default='00')
    has_voting_history = models.BooleanField(default=False)
    voting_history = ArrayField(models.CharField(max_length=20), default=list)
