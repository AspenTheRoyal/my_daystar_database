from django.http import HttpResponse
from django.template import loader
from .models import Character

def character_data(request):
  mycharacters = list(Character.objects.all().order_by('fullname').values())
  template = loader.get_template('all_characters.html')
  context = {
    'mycharacters': mycharacters,
  }
  return HttpResponse(template.render(context, request))

def details(request, fullname):
  mycharacter = Character.objects.get(fullname=fullname)
  template = loader.get_template('details.html')
  context = {
    'mycharacter': mycharacter,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())