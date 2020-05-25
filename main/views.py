from django.shortcuts import render
from .models import Member
# Create your views here.


def index(request):
    """
    Starting page for app.
    """
    members = Member.objects.all().order_by('-created')
    context = {'member_count': len(members), 'members': members}

    return render(request, 'main/index.html', context=context)
