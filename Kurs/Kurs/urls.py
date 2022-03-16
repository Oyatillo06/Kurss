from django.contrib import admin
from django.urls import path
from kursapp.views import QuizView,SavolJavobView
from userapp.views import LoginPageView,RegistrationsView,Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginPageView.as_view(),name='home'),
    path('registration/',RegistrationsView.as_view(),name='registration'),
    path('quiz/',QuizView.as_view(),name='quiz'),
    path('savol/<int:pk>/',SavolJavobView.as_view()),
    path('logout/',Logout,name='logout'),


]
