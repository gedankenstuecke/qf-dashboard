from django.core.management.base import BaseCommand
from main.models import Member
import requests
from django.conf import settings

class Command(BaseCommand):
    help = 'Process so far unprocessed data sets'

    def handle(self, *args, **options):
        #how to keep the heroku app alive despite a free dyno :joy:
        response = requests.get('https://www.openhumans.org/api/public-data/members-by-source/?source={}'.format(settings.OH_PROJECT_ID))
        response_members = response.json()['results'][0]['usernames']
        for response_member in response_members:
            member, _ = Member.objects.get_or_create(member_name=response_member)
            member.save()
            print(member)
        all_saved_members = Member.objects.all()
        for saved_member in all_saved_members:
            if saved_member.member_name not in response_members:
                saved_member.delete()
