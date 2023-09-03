from rest_framework import serializers
from .models import Profile, Project, Certificate, CertifyingInstitution


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = CertifyingInstitution
        fields = '__all__'
