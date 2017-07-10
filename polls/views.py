from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import EkFile
from django.views.decorators.csrf import ensure_csrf_cookie
from .serialize import serialize
import json
# Create your views here.

@ensure_csrf_cookie
def upload(request):
    if request.method=='POST':
        instance=EkFile(file=request.FILES['files'])
        obj=instance.save();
        print (instance)
        values=serialize(instance)
        data={"files":values}
        response=json.dumps(data)
        print (response)
        return HttpResponse(response,content_type="application/json")
        

@ensure_csrf_cookie
def index(request):
    return render(request,'polls/index.html')

@ensure_csrf_cookie
def list_the_files(request):
    values=[serialize(instance) for instance in EkFile.objects.all()]
    data={"files":values}
    response=json.dumps(data)
    print (response)
    return HttpResponse(response,content_type="application/json")

@ensure_csrf_cookie
def delete_files(request):
    print ("Delete this file: "+request.POST['id'])
    instance=EkFile.objects.get(id=request.POST['id'])
    print (instance)
    instance.delete()
    return HttpResponse(json.dumps({"id":4}),content_type="application/json")