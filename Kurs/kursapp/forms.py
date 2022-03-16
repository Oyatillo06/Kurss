from django.forms import ModelForm

from .models import *

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['nom', 'batafsil', 'savol_soni', 'davomiyligi']

class SavolForm(ModelForm):
    class Meta:
        model = Savol
        fields = ['matn','quiz']