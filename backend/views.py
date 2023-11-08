from django.shortcuts import render
from welcomepage.models import userDetail
from picprocess.models import Data

# Create your views here.
def userManage(request):
    userdetail = userDetail.objects.all()
    return  render(request, 'usermanage.html', {"userdetails": userdetail})
def dataManage(request):
    data = Data.objects.all()
    return render(request, 'dataManage.html', {"datas": data})