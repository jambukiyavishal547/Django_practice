from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',views.student_list, name='student_data'),
]