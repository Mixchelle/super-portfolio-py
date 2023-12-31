from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'certificates', views.CertificateViewSet)
router.register(r'certifying-institutions', views.CertifyingInstitutionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
