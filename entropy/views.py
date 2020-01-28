from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twentropy.models import Hacker 
import os
from django.conf import settings


@csrf_exempt
def home(request):
        if request.GET.get('view'):
            data = Hacker.objects.first()

            return HttpResponse(data.name)

        posted = 0
        if request.method == 'POST':
            #Hacker(name=request.POST.get('name'), email=request.POST.get('email'), phone=request.POST.get('phone'), text=request.POST.get('message')).save()
            fd = os.open( settings.BASE_DIR + "/users.txt", os.O_RDWR)
            line = str.encode(request.POST.get('email', '') + "," + request.POST.get('name', '') + "," + request.POST.get('phone', '') + "," + request.POST.get('message','') )
            print(line)
            numBytes = os.write(fd, line) 

            posted = 1
        return render(request, 'index.html', {'posted': posted} )
        #return HttpResponse("Hello there world.")

def pseudostatic(request):
        return HttpResponse("Hello")
