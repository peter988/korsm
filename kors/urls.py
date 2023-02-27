
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from mikeal.views import menfun , womfun,kidsfun,handbagsfun,add,main,shoes
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("men/", menfun),
    path("women/", womfun),
    path("kids/", kidsfun),
    path("handbags/", handbagsfun),
    path("add/", add),
    path("shoes/", shoes),
    path("", main)
]



