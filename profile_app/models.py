from django.db import models
from enterprise_model.models import Resource


class Profile(models.Model):
    name = models.CharField(u'Profile name', max_length=255)
    description = models.TextField(u'Description')

    class Meta:
        verbose_name = u'Profile'
        verbose_name_plural = u'Profiles'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    name = models.CharField(u'Treatment name', max_length=255)
    description = models.TextField(u'Description')
    profile = models.ForeignKey(Profile, related_name='related_profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Treatment'
        verbose_name_plural = u'Treatments'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class ProfileResourceRule(models.Model):
    profile = models.ForeignKey(Profile, related_name='related_profile_resource_rule', on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, related_name='related_resource_rule', on_delete=models.CASCADE)
    task_name = models.CharField(u'Task name', max_length=255)

    class Meta:
        verbose_name = u'Profile Resource Rule'
        verbose_name_plural = u'Profile Resource Rules'
        ordering = ('-id',)

    def __str__(self):
        return self.profile
