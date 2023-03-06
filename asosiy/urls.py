from django.urls import path
from .views import *
urlpatterns = [

    path('home2/',Home2View.as_view(),),
    path('home/',HomeView.as_view(),),
    path('bolimlar/',HammabolimView.as_view(),),
    path('bolim/<int:son>',BolimmahsulotView.as_view(),),
    path('bittamahsulot/<int:son>',BittaMahsulotView.as_view(),)

]