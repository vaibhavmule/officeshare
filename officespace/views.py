# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from oautherise.forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from officespace.forms import Officeform, messageform
from officespace.models import office, messages
from datetime import datetime

def index(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'GET':
        offices = office.objects.order_by('date')
        context_dict['offices'] = offices
    elif request.method == 'POST':
        if 'location' in request.POST:
            location = request.POST.get('location')
            try:
                offices = office.objects.filter(location=location)
                context_dict['offices'] = offices
            except:
                pass
    return render_to_response('officespace/index.html', context_dict, context)

def addspace(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        form = Officeform(request.POST)

        if form.is_valid():
            office = form.save(commit=False)

            try:
                users = User.objects.get(username=request.user)
                office.users = users

                if 'picture' in request.FILES:
                    office.picture = request.FILES['picture']
                office.save()
                return HttpResponseRedirect("/")
            except:
                pass
        else:
            print form.errors

    else:
        form = Officeform()

    context_dict['form'] = form

    return render_to_response('officespace/addofficeform.html', context_dict, context)


def officespaceinfo(request, id):
    context = RequestContext(request)
    context_dict = {}
    off = office.objects.get(id=id)
    context_dict['offices'] = off

    return render_to_response('officespace/info.html', context_dict, context)

def messag(request, receiverid):
    context = RequestContext(request)
    context_dict = {}
    # userfor = User.objects.get(username=receiverid)
    # receiverid=int(userfor.id)
    users = User.objects.get(id=receiverid)
    context_dict['users'] = users

    if request.method == 'GET':
        form = messageform()

    elif request.method == 'POST':
        form = messageform(request.POST)

        if form.is_valid():
            mess = form.save(commit=False)
            mess.receiverid = int(receiverid)
            users = User.objects.get(username=request.user)
            mess.senderid = int(users.id)
            mess.seen = 1
            mess.save()
            return HttpResponseRedirect("/")
        else:
            print form.errors

    context_dict['form'] = form
    return render_to_response('officespace/message.html', context_dict, context)


def showmessages(request):
    context = RequestContext(request)
    context_dict = {}
    users = User.objects.all()
    keymapper = {}
    for use in users:
        keymapper[use.id] = use.username

    context_dict['keymapper'] = keymapper
    usr = User.objects.get(username=request.user)
    message = messages.objects.filter(receiverid=int(usr.id))
    context_dict['messages'] = message

    return render_to_response('officespace/showmessages.html', context_dict, context)




