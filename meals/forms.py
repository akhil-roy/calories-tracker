from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(format=('%d-%m-%Y'), 
                               attrs={'type':'date'}))
    class Meta:
        model = Meal
        fields = ["name","date","time","desc","calories"]