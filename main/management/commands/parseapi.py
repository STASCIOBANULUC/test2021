from django.core.management import BaseCommand
import requests
from main.models import Transaction


class Command(BaseCommand):
    help = 'Extract API'

    def handle(self, *args, **options):
        url = 'http://193.122.78.15/api/ver1/events/all'
        headers = {'Authorization': 'Token b7e62e054daaab8c4cefb93027989bbd9a762261'}
        response = requests.get(url, headers=headers)
        print(response.json())
        for i in response.json():
            Transaction.objects.create(pk=i['id'], name=i["name"], surname=i["surname"], uuid=i["uuid"],
                                       plate_number=i["plate_number"], group=i["group"], date=i["date"],
                                       direction=i["direction"], status=i["status"], type_passage=i["type_passage"],
                                       photo=i["photo"], sync=i["sync"])
