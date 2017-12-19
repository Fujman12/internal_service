from rest_framework import serializers
from .models import Domain, Resource, Instance


class DomainListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Domain
        fields = [
            'id',
            'name',
            'description',
        ]
