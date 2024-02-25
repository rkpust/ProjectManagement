from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
]