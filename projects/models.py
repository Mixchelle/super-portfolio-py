from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=50)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField()
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
   

class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    certifying_institution = models.ForeignKey(CertifyingInstitution, on_delete=models.CASCADE, related_name='certificates')
    timestamp = models.DateTimeField(default=timezone.now)
    profiles = models.ManyToManyField(Profile, related_name='certificates')

    def __str__(self):
        return self.name



