from django.shortcuts import render
from .models import Member
from django.http import JsonResponse
# Create your views here.


def index(request):
    """
    Starting page for app.
    """
    members = Member.objects.all().order_by('-created')
    context = {'member_count': len(members), 'members': members}

    return render(request, 'main/index.html', context=context)


def graph_data(request):
    '''
    deliver data for metricsgraphics.js
    '''
    members = Member.objects.all().order_by('created')
    counter = 1
    member_list = []
    for m in members:
        member_list.append({'date': m.created, 'members': counter})
        counter += 1
    response = JsonResponse(member_list, safe=False)
    return response
