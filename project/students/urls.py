from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('addrec/',views.addrec, name='addrec'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    # path('uprec/<int:id>/', views.uprec, name='uprec'),  # Not needed anymore
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# REST API routes
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


