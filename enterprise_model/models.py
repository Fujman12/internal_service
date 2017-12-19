from django.db import models
from django.contrib.postgres.fields import JSONField


class Domain(models.Model):
    name = models.CharField(u'Domain name',  max_length=255)
    description = models.TextField(u'Description')

    class Meta:
        verbose_name = u'Domain'
        verbose_name_plural = u'Domains'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(u'Resource name', max_length=255)
    description = models.TextField(u'Description')
    domain = models.ForeignKey(Domain, related_name='related_domain', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Resource'
        verbose_name_plural = u'Resources'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Instance(models.Model):
    external_identifier = models.CharField(u'External identifier',  max_length=255)
    resource = models.ForeignKey(Resource, related_name='related_resource', on_delete=models.CASCADE)
    data = JSONField(u'Data')

    class Meta:
        verbose_name = u'Instance'
        verbose_name_plural = u'Instances'
        ordering = ('-id',)

    def __str__(self):
        return self.external_identifier

