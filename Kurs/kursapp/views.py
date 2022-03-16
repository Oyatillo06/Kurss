from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .models import *
from userapp.models import Foydalanuvchi



class QuizView(View):
    def get(self,request):
        if request.user.is_authenticated:
            q=Quiz.objects.all()

            return render(request,'quiz.html',{"quiz":q})
        else:
            return redirect('home')
class SavolJavobView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            q=Quiz.objects.get(id=pk)
            s=Savol.objects.filter(quiz=q)
            j=Javob.objects.filter(savol=s)
            list_for_random = range(5)
            return render(request,'sj.html',{"savol":s,"javob":j,'list_for_random': list_for_random})
        else:
            return redirect('home')