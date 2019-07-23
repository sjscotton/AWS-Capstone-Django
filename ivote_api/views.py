from django.shortcuts import render
from django.http import JsonResponse
from ivote_api.models import Vote, Voter, Voting_Stats, Visitor
from django.db import models
import requests
import json
# Create your views here.


def index(request):
    vote = Vote.objects.first()
    voter = Voter.objects.first()

    data = {
        'Hello': 'Friend',
        "vote date": vote.election_date,
        "voter name": voter.f_name,


    }

    return JsonResponse({"data": data})


def get_voter(request):

    first_name = request.GET.get('first_name', None)
    last_name = request.GET.get('last_name', None)
    birthdate = request.GET.get('birthdate', None)
    voter_id = request.GET.get('voter_id', None)

    if voter_id:
        try:
            person = Visitor.objects.get(state_voter_id=voter_id)
            address = person.address
            age_group = person.age_group

        except:
            return JsonResponse({'message': f'Record not found for voter ID: {voter_id}.'}, status=404)

    else:
        if not first_name or not last_name or not birthdate:
            return JsonResponse({'message': "Must supply first_name, last_name and birthdate"}, status=400)

        try:
            person = Voter.objects.get(
                f_name=first_name.upper(), l_name=last_name.upper(), birthdate=birthdate.replace('-', '/'))
            address = person.get_address()
            age_group = person.get_age_group()
        except:
            return JsonResponse({'message': f'Record not found for {first_name} {last_name}.'}, status=404)

        if not person.user:
            Visitor.objects.create(
                f_name=person.f_name,
                l_name=person.l_name,
                state_voter_id=person.state_voter_id,
                address=person.get_address(),
                county_code=person.county_code,
                city=person.city,
                age_group=person.get_age_group(),
                birthdate=person.birthdate)
            person.user = True
            person.save()

    data = {
        'first_name': person.f_name,
        'last_name': person.l_name,
        'voter_id': person.state_voter_id,
        'address': address,
        'county_code': person.county_code,
        'city': person.city,
        'age_group': age_group
    }
    return JsonResponse(data, status=200)


def get_votes(request):
    voter_id = request.GET.get('state_voter_id', None)
    if not voter_id:
        return JsonResponse({'message': "Must supply state_voter_id"}, status=400)

    returning_user = request.GET.get('returning_user', None)
    remember_me = request.GET.get('remember_me', None)
    votes = []
    if returning_user == 'true':
        voter = Visitor.objects.get(state_voter_id=voter_id)
        votes = voter.voting_history
    else:
        voting_history = Vote.objects.filter(state_voter_id=voter_id)
        votes = [v.election_date for v in voting_history]
    if remember_me == 'true':
        voter = Visitor.objects.get(state_voter_id=voter_id)
        voter.voting_history.clear()
        for vote in votes:
            voter.voting_history.append(vote)
        voter.save()
    data = {
        'voting_days': votes
    }
    return JsonResponse(data, status=200)


def get_stats(request):

    city = request.GET.get('city', None)
    county_code = request.GET.get('county', None)

    if city:
        rows = Voting_Stats.objects.filter(city=city)
    elif county_code:
        rows = Voting_Stats.objects.filter(county_code=county_code)
    else:
        return JsonResponse({'message': "Must supply age_group, and city or county_code"}, status=400)
    max_votes = Voting_Stats.get_max_votes(rows)
    data = {}
    data['county_code'] = rows[0].county_code
    data['city'] = rows[0].city
    for row in rows:
        data[row.age_group] = row.voting_freq[:max_votes + 1]

    return JsonResponse({'stats': data}, status=200)


def get_reps(request):
    address = request.GET.get('address', None)
    if not address:
        return JsonResponse({'message': "Must supply address"}, status=400)

    """ Google Civic API call """

    payload = {'key': '',
               'address': address}
    url = 'https://www.googleapis.com/civicinfo/v2/representatives'
    response = requests.get(url, params=payload)

    reps = json.loads(response.text)
    """Cached response  """

    return JsonResponse({'reps': reps}, status=200)
