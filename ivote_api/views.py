from django.shortcuts import render
from django.http import JsonResponse
from ivote_api.models import Vote
# Create your views here.
def index(request):
    votes = Votes.object.all()
    data = {
      'Hello': 'Friend',
      "number of votes": len(votes)

    }


    return JsonResponse({"data": data})