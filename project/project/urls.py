from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from rest_framework import routers
from api_app import views
from users.views import UserAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('myapp/',include('myapp.urls')),
    # path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('snippet/',include('snippets.urls')),
    path('blog/',include('blog.urls')), 
    path('student/',include('student.urls')),
    path('orm/',include('orm.urls')),
    path('home/',include('home.urls')),
    path('snipp/',include('snipp.urls')),
    path('make_curd/',include('make_curd.urls')),
    # path('users/',include('users.urls')),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserAPIView.as_view(), name='user'),
    # path('api/docs/', schema_view, name='swagger'),
    path('check_swagger/',include('check_swagger.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)