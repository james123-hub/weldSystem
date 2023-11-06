from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import PhotoForm
from .models import Data

# Create your views here.
def picProcess(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            imgUrl = Data.objects.last().data.url
            return render(request, 'picprocess.html', {"dataUrl": imgUrl})
    return render(request, 'picprocess.html')
def test(request):
    print(type(request.POST.get("brightness")))
    print("成功")
    return render(request, 'test.html')
def piccut(request):
    return render(request, 'piccut.html')