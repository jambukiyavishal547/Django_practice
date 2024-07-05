from django.urls import path
from django.contrib import admin
from home import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('homes/',views.home,name='home'),
    path('hom/',views.hom,name='hom'),

]
