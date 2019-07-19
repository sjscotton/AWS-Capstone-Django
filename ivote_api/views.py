from django.shortcuts import render
from django.http import JsonResponse
from ivote_api.models import Vote, Voter, Voting_Stats
# Create your views here.
def index(request):
    votes = Vote.objects.all()
    voters = Voter.objects.all()
    stats = Voting_Stats.objects.all()
    print(voters)
    data = {
      'Hello': 'Friend',
      "number of votes": len(votes),
      "num voter": len(voters),
      "stats": len(stats)

    }


    return JsonResponse({"data": data})