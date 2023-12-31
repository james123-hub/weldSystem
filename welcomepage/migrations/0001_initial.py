# Generated by Django 3.1 on 2023-11-07 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companyInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='公司编号')),
                ('company', models.CharField(max_length=50, null=True, verbose_name='公司名')),
            ],
            options={
                'verbose_name': '公司信息表',
                'db_table': 'CompanyInfo',
            },
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户编号')),
                ('username', models.CharField(max_length=30, verbose_name='用户名称')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('status', models.CharField(max_length=1, verbose_name='权限')),
                ('createdate', models.DateTimeField(auto_now_add=True, verbose_name='注册日期')),
            ],
            options={
                'verbose_name': '用户信息表',
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='userDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='个人信息编号')),
                ('username', models.CharField(max_length=30, null=True, verbose_name='用户姓名')),
                ('sex', models.CharField(max_length=1, verbose_name='性别')),
                ('createdate', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='welcomepage.companyinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='welcomepage.userinfo')),
            ],
            options={
                'verbose_name': '个人信息表',
                'db_table': 'UserDetail',
            },
        ),
    ]
