from django.db import models
from welcomepage.models import userDetail

# Create your models here.
class Data(models.Model):
    id = models.AutoField(verbose_name='数据编号', primary_key=True)
    dataUrl = models.CharField(verbose_name='数据路径',max_length = 500)
    upload_time = models.DateTimeField(auto_now_add=True)
    dataname = models.CharField(max_length = 150)

    def __str__(self):
        return self.dataname

    class Meta:
        verbose_name = '数据信息表'
        db_table = 'Datainfo'