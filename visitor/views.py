from django.shortcuts import render
from django.http import HttpResponse
from .models import Visitor

def index(request):
    visitor_ip = request.META.get('REMOTE_ADDR')
    visitor = Visitor(ip_address=visitor_ip)
    visitor.save()
    visitors = Visitor.objects.all()
    return render(request, 'index.html', {'visitors': visitors})
