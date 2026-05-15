from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import GeneroViewSet, FilmeViewSet

router = DefaultRouter()
router.register(r'generos', GeneroViewSet, basename='genero')
router.register(r'filmes', FilmeViewSet, basename='filme')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
