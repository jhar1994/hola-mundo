from django import forms

from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model=Page
        fields=['title','content','order']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),
            'order':forms.NumberInput(attrs={'class':'form-control','placeholder':'Order'}),
        }
        
        lables={
            'title':'',
            'content':'',
            'order':'',
        }
# Compare this snippet from webplayground/pages/models.py:
# from django.db import models
#
# # Create your models here.
# class Page(models.Model):
#     title=models.CharField(max_length=50,verbose_name='Title')
#     content=models.TextField(verbose_name='Content')                      