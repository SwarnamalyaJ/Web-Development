from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['Customer_Age','Gender','Education_Level','Income_Category','Card_Category','Credit_Limit','Total_Trans_Amt']
