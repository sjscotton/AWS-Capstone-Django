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
