from django.db import models

# Create your models here.
class userInfo(models.Model):
    id = models.AutoField(verbose_name = '用户编号', primary_key = True)
    username = models.CharField(verbose_name= '用户名称', max_length = 30)
    password = models.CharField(verbose_name = '密码', max_length = 20)
    status = models.CharField(verbose_name = '权限', max_length = 1)
    createdate = models.DateTimeField(verbose_name= '注册日期', auto_now_add = True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '用户信息表'
        db_table = 'UserInfo'
class userDetail(models.Model):
    id = models.AutoField(verbose_name = '个人信息编号', primary_key = True)
    username = models.CharField(verbose_name= '用户姓名', max_length = 30, null = True )
    sex =models.IntegerField(verbose_name = '性别')
    company = models.CharField(verbose_name= '公司名', max_length = 50, null = True)
    createdate = models.DateTimeField(verbose_name = '修改时间', auto_now = True)
    user = models.OneToOneField(userInfo, on_delete = models.CASCADE, null = False)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '个人信息表'
        db_table = 'UserDetail'
