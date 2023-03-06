from django.contrib import admin
from django.urls import path,include
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(),),
    path('register/',RegisterView.as_view(),),
    path('logout/',LogoutView.as_view(),),
    path('asosiy/', include('asosiy.urls')),
    path('asosiy2/', include('asosiy2.urls')),
    # path('header/', NamunaView.as_view()),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
