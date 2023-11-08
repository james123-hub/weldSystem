import os
from django.conf import settings
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Data
from welcomepage.models import userDetail

# Create your views here.
def picProcess(request):
    if request.method == 'POST':
        image = request.FILES['data']
        imagename = image.name
        data = Data()
        username = request.COOKIES['username']
        userdetail = userDetail.objects.filter(username= username)
        if len(userdetail) !=0 :
            userdetail = userdetail[0]
            subdir = str(userdetail.company.id)
        else:
            subdir = 'default'
        dataurl = os.path.join(settings.MEDIA_ROOT, subdir)
        if not os.path.exists(dataurl):
            os.makedirs(dataurl)
        with open(os.path.join(dataurl, image.name), 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        data.dataname = imagename
        data.dataUrl = os.path.join(subdir, image.name)
        data.save()
        return render(request, 'picprocess.html', {"dataUrl": settings.MEDIA_URL+data.dataUrl})
    return render(request, 'picprocess.html')
def test(request):
    print(type(request.POST.get("brightness")))
    print("成功")
    return render(request, 'test.html')
def piccut(request):
    return render(request, 'test1.html')
def picprdict(request):
    return render(request, 'picpredict.html')
def showresult(request):
    data = Data.objects.all()
    return render(request, 'result.html', {"datas": data})