from django import forms
from .models import DangBan,DangMua

class DangBan_Form(forms.ModelForm):

    class Meta:
        model = DangBan
        fields = ['product_name', 'cover','description','product_price','link_Facebook']

class DangMua_Form(forms.ModelForm):

    class Meta:
        model = DangMua
        fields = ['product_name', 'cover','description','link_Facebook']