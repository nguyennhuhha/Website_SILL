from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.

#làm thêm bảng user, trên trang admin, thống kê được số lượt tải của user trong từng sản phẩm
class Collection(models.Model):
    ID = models.IntegerField(primary_key=True)
    IDtype = models.CharField(max_length=50)
    Name = models.CharField(max_length=200)
    Detail= models.CharField(max_length=500)
    Image = models.ImageField(null=True, blank=True, upload_to="images/")
    Image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    Image2 = models.ImageField(null=False, blank=True, upload_to="images/")
    Linkdownload = models.FileField( upload_to="file/",null=False,default=None)

    def __str__(self):
        return self.Name
    
class Download(models.Model):
    collection = models.ForeignKey(Collection,on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'style': 'width: 320px; height: 30px;'})
        self.fields['email'].widget.attrs.update({'style': 'width: 320px; height: 30px;'})
        self.fields['password1'].widget.attrs.update({'style': 'width: 320px; height: 30px;'})
        self.fields['password2'].widget.attrs.update({'style': 'width: 320px; height: 30px;'})