from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.

mymembers = Members.objects.all().values()
context = {
  'my_members': mymembers,
}

def index(request):
    template = loader.get_template("myfirstapp.html")
    return HttpResponse(template.render(context, request))

def members_table(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)

def add(request):
  template = loader.get_template("add.html")
  return HttpResponse(template.render({}, request))

def added_record(request):
  x = request.POST['firstname']
  y = request.POST['lastname']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  member = Members.objects.get(id=id)
  template = loader.get_template("update.html")
  context = {
      'my_member': member,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['firstname']
  last = request.POST['lastname']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
  
def testing(request):
  mydata = Members.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('testing.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

def testing1(request):
  template = loader.get_template('template.html')
  context = {
    'mycar': {
      'brand': 'Ford',
      'model': 'Mustang',
      'year': '1964',
      },
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange'],
    'name': "Capt'n Jack",
  }
  return HttpResponse(template.render(context, request)) 