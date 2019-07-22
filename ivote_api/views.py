from django.shortcuts import render
from django.http import JsonResponse
from ivote_api.models import Vote, Voter, Voting_Stats
# Create your views here.


def index(request):
    vote = Vote.objects.first()
    voter = Voter.objects.first()
    print(vote)
    print(voter)
    # stats = Voting_Stats.objects.all()
    # print(voters)
    data = {
        'Hello': 'Friend',
        "vote date": vote.election_date,
        "voter name": voter.f_name,
        # "stats": len(stats)

    }

    return JsonResponse({"data": data})


def get_voter(request):

    first_name = request.GET.get('first_name', None)
    last_name = request.GET.get('last_name', None)
    birthdate = request.GET.get('birthdate', None)
    voter_id = request.GET.get('voter_id', None)

    if voter_id:
        try:
            person = Voter.objects.get(state_voter_id=voter_id)
        except:
            return JsonResponse({'message': f'Record not found for voter ID: {voter_id}.'}, status=404)

    else:
        if not first_name or not last_name or not birthdate:
            return JsonResponse({'message': "Must supply first_name, last_name and birthdate"}, status=400)

        try:
            person = Voter.objects.get(
                f_name=first_name.upper(), l_name=last_name.upper(), birthdate=birthdate.replace('-', '/'))
        except:
            return JsonResponse({'message': f'Record not found for {first_name} {last_name}.'}, status=404)

    data = {
        'first_name': person.f_name,
        'last_name': person.l_name,
        "middle_name": person.m_name,
        'voter_id': person.state_voter_id,
        'address': person.get_address(),
        'county_code': person.county_code,
        'city': person.city,
        'age_group': person.get_age_group()
    }
    return JsonResponse(data, status=200)


def get_votes(request):
    voter_id = request.GET.get('state_voter_id', None)
    if not voter_id:
        return JsonResponse({'message': "Must supply state_voter_id"}, status=400)

    votes = Vote.objects.filter(state_voter_id=voter_id)
    data = {
        'voting_days': [vote.election_date for vote in votes]
    }

    return JsonResponse(data, status=200)
