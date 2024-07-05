from django.urls import path,include
from django.contrib import admin
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippet_list',views.SnippetViewSet.as_view({'get':'list'})),
    # path('snippet_detail/<int:pk>/',views.SnippetDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.userDetails.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]