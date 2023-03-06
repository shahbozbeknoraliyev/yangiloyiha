from django.http import HttpResponse

from django.views import View
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class HomeView(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                "bolimlar":Bolim.objects.all()[:7],
                "chegirmalilar":Mahsulot.objects.filter(chegirma__gt=0).order_by('-chegirma')[:5]
            }
            return render(request,"page-index.html",data)
        return redirect('/')
class LoginView(View):
    def get(self,request):
        return render(request,"page-user-login.html")
    def post(self,request):
        user=authenticate(username=request.POST.get('l'),
                          password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request,user)
        return redirect('/asosiy/home')

class Home2View(View):
    def get(self,request):
        return render(request,"page-index-2.html")
class HammabolimView(View):
    def get(self,request):
        data={'bolimlar':Bolim.objects.all()}

        return render(request,"page-category.html",data)
class BolimmahsulotView(View):
    def get(self,request,son):
        data={
            "mahsulot":Mahsulot.objects.filter(bolim__id=son)
        }
        return render(request,"page-listing-grid.html",data)
class BittaMahsulotView(View):
    def get(self,request,son):
        data={
            "mahsulot":Mahsulot.objects.get(id=son)
        }
        return render(request,"page-detail-product.html",data)
class LogoutView(View):
    def get(self,requset):
        logout(requset)
        return redirect('/')
class RegisterView(View):
    def get(self,request):
        return render(request,'page-user-register.html')
    def post(self,request):
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')

        )
        return redirect('/')