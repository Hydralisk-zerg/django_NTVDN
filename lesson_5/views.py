from decimal import Decimal
from uuid import uuid4
from django.shortcuts import render

from django.http import HttpResponse
from lesson_5.models import Flower, Bouquet, Client

def create_flower(request):
    rouse = Flower()
    rouse.count = 5
    rouse.description = 'Ро́за — собирательное название видов и сортов'\
    ' представителей рода Шиповник, выращиваемых человеком и растущих в'\
    ' дикой природе. Большая часть сортов роз получена в результате'\
    ' длительной селекции путём многократных повторных скрещиваний и'\
    ' отбора. Некоторые сорта являются формами дикорастущих видов.'
    rouse.could_use_in_bouquet = True
    rouse.wiki_page = 'https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%B7%D0%B0'
    rouse.name = 'Роза чайная'
    rouse.save()
    return HttpResponse('Created!!')

    
def create_client(request):
    with open('requirements.txt', 'r') as _file:
        tmp_file = _file.read

    Client.objects.create(**{
        'second_email': 'admin@amdmin.com',
        'name': 'MyName',
        'invoice': tmp_file,
        'user_uuid': uuid4(),
        'discount_size': Decimal('0.00052'),
        'client_ip': '192.0.2.1',
    })
    return HttpResponse(request, 'Created!!')

    
def get_flower(request):
    return HttpResponse('Flowers')
