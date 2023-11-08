from django import forms
from django.core.exceptions import ValidationError


class UserRegForm(forms.Form):
    username = forms.CharField(max_length = 30 , error_messages={'required': '用户姓名不能为空', 'max_length': '用户名长度不超过30位'})
    password = forms.CharField(max_length = 20 , error_messages={'required': '密码不能为空', 'max_length': '密码长度不超过20位'})
    confirmpwd = forms.CharField(max_length = 20 , error_messages={'required': '密码不能为空', 'max_length': '密码长度不超过20位'})

    def clean(self):
        password = self.cleaned_data.get("password")
        confirmpwd = self.cleaned_data.get("confirmpwd")
        if password != confirmpwd:
            self.add_error("re_password", ValidationError("两次密码不一致"))

class UserDetailForm(forms.Form):
    username = forms.CharField(required = False,max_length=30, error_messages={'max_length': '用户名长度不超过30位'})
    sex = forms.CharField(error_messages={'required': '请选择性别'})
    company = forms.CharField(max_length = 50, error_messages={'required': '请填公司名','max_length': '公司名长度不超过20位'})

class UserPwdEdit(forms.Form):
    username = forms.CharField(max_length=30, error_messages={'required': '用户姓名不能为空', 'max_length': '用户名长度不超过30位'})
    password = forms.CharField(max_length=20, error_messages={'required': '密码不能为空', 'max_length': '密码长度不超过20位'})
    confirmpwd = forms.CharField(max_length=20, error_messages={'required': '密码不能为空', 'max_length': '密码长度不超过20位'})

    def clean(self):
        password = self.cleaned_data.get("password")
        confirmpwd = self.cleaned_data.get("confirmpwd")
        if password != confirmpwd:
            self.add_error("re_password", ValidationError("两次密码不一致"))