from rest_framework import viewsets
from .models import Profile, Project, Certificate, CertifyingInstitution
from .serializers import ProfileSerializer, ProjectSerializer, CertificateSerializer, CertifyingInstitutionSerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.method == 'GET':
            context = {'profile': instance}  #
            return render(request, 'profile_detail.html', context)
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
