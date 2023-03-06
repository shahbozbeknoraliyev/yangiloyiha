from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bolim(models.Model):
    nom=models.CharField(max_length=50)
    rasm=models.FileField(upload_to='bolim')
    def __str__(self):
        return self.nom
class Mahsulot(models.Model):
    nom=models.CharField(max_length=50)
    narx=models.FloatField()
    brend=models.CharField(max_length=50)
    davlat=models.CharField(max_length=50)
    kafolat=models.CharField(max_length=50)
    bolim=models.ForeignKey(Bolim,on_delete=models.CASCADE)
    min_miqdor=models.PositiveSmallIntegerField()
    tasdiqlangan=models.BooleanField()
    yetkazish=models.CharField(max_length=50)
    mavjud=models.BooleanField()
    chegirma=models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.nom}, {self.brend}"
class Media(models.Model):
    rasm=models.FileField(upload_to='mahsulotlar')
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)

