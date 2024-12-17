from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from app.api import viewsets as viewsets

route = routers.DefaultRouter()
route.register(r'despesas',viewsets.DespesaViewSet,basename='despesas')
route.register(r'receitas',viewsets.ReceitaViewSet,basename='receitas')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    