from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from core.models import IP
from core.models import Access

def hit(request):

    remote_addr = request.META['REMOTE_ADDR'];
    access_time = datetime.now()

    try:
        ip = IP.objects.get(address=remote_addr)
    except IP.DoesNotExist:
        ip = IP(address=remote_addr)
        ip.save()

    access = Access(ip=ip, time=access_time)
    access.save()

    return HttpResponse("Access registered")

def list(request):
    accesses = Access.objects.all()
    response = '<p/>'.join(map(str,accesses))
    return HttpResponse(response)