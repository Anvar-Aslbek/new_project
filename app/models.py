from tabnanny import verbose
from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.


class Viloyat(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50,verbose_name="Holat nomlari")

    def __str__(self):
        return self.name

class Loyiha(models.Model):
    viloyat = models.ForeignKey(Viloyat,on_delete = models.SET_NULL, null=True)
    tuman = models.CharField(max_length=40)
    status = models.ForeignKey(Status,on_delete=models.SET_NULL,null=True,verbose_name="Loyiha holati")
    tashabbuskor = models.CharField(max_length=100,verbose_name="loyiha tashabbuskori")
    maqsad = models.CharField(max_length=200,verbose_name="loyiha maqsadi")
    qiymati = models.BigIntegerField(default=0,verbose_name="loyiha qiymati (mln. sumda)")
    mablag = models.BigIntegerField(default=0,verbose_name="Uz mablag'lari")
    kredit = models.BigIntegerField(default=0,verbose_name="Bank kreditlari")
    valyuta = models.BigIntegerField(default=0,verbose_name="Milliy valyuta")
    valyuta_xorij = models.BigIntegerField(default = 0,verbose_name="Xorijiy valyuta")
    investitsiya = models.BigIntegerField(default=0,verbose_name="Xorijiy invastitsiya")
    ishchi_urin = models.IntegerField(default=0,verbose_name="Ishchi O'rin")
    bank_kredeti = models.BigIntegerField(default=0,verbose_name="Haqiqatda ajratilgan bank kreditlari")
    muddat = models.DateField(verbose_name="Loyiha ishga tushish muddati")
    izoh = models.TextField()

    def __str__(self):
        return self.tuman + " tumanidagi loyiha"