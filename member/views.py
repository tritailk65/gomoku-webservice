from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def lobby(request):
    template = loader.get_template('lobby.html')
    return HttpResponse(template.render())

def member(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_member.html');
    context = {
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())