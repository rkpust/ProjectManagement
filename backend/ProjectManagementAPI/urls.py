from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
urlpatterns = router.urls

urlpatterns = [
    # Other URL patterns...
    path('api/', include(router.urls)),
]