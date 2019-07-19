from django.shortcuts import render
from django.http import JsonResponse
from ivote_api.models import Vote, Voter
# Create your views here.
def index(request):
    votes = Vote.objects.all()
    voters = Voter.objects.all()
    print(voters)
    data = {
      'Hello': 'Friend',
      "number of votes": len(votes),
      "num voter": len(voters),

    }


    return JsonResponse({"data": data})