from enterprise_model.serializers import DomainListSerializer
from enterprise_model.models import Domain
from rest_framework.generics import ListCreateAPIView


class DomainListApiView(ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainListSerializer
