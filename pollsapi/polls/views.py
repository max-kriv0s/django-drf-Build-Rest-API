from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"result": list(polls.values("pk","question", "create_by__username", "pub_date"))}
    return JsonResponse(data)


def polls_details(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"result": {
        "question": poll.question,
        "create_by__username": poll.create_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)
