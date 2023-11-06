from django.db import models

# Create your models here.
class Data(models.Model):
    data = models.ImageField(upload_to='data/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data.name

    class Meta:
        verbose_name = '数据信息表'
        db_table = 'Datainfo'