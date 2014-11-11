# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from oautherise.forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from officespace.forms import Officeform
from officespace.models import office
from datetime import datetime

def index(request):
    context = RequestContext(request)
    context_dict = {}
    offices = office.objects.all()
    context_dict['offices'] = offices
    return render_to_response('officespace/index.html', context_dict, context)

def addspace(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        form = Officeform(request.POST)

        if form.is_valid():
            office = form.save(commit=False)

            try:
                user = User.objects.get(username=request.user)
                office.user = user

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


def officespaceinfo(request, location):
    context = RequestContext(request)
    context_dict = {}

    off = office.objects.get(location=location)
    context_dict['offices'] = off

    return render_to_response('officespace/info.html', context_dict, context)
