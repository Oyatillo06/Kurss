from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from kursapp.models import Quiz,Savol,Javob


class LoginPageView(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        l = request.POST['login']
        p = request.POST['parol']
        users = authenticate(request, username=l, password=p)
        if users is None:

            return redirect('home')
        else:
            login(request, users)
            return redirect('quiz')

class RegistrationsView(View):
    def get(self,request):
        return render(request, "reg.html")
    def post(self,request):
        User.objects.create_user(
            username=request.POST["login"],
            password=request.POST["parol"]

        )
        return redirect("home")

def Logout(request):
    logout(request)
    return redirect('home')