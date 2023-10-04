from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.drop),
    path('saveimage/', views.saveimage),
    path('img/',views.imagesucess),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)