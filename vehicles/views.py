from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions

from core.permissions import IsOwnerOfVehicleOrRecord


from vehicles.models import Vehicle, VehicleType
from vehicles.serializers import VehicleTypeSerializer, VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
  queryset = Vehicle.objects.all()
  serializer_class = VehicleSerializer
  permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]
  
  def get_queryset(self):
    user = self.resquest.user
    if user.is_staff:
      return Vehicle.objects.all()
    return Vehicle.objects.filter(owner__user = user)

class VehicleTypeViewSet(viewsets.ModelViewSet):
  queryset = VehicleType.objects.all()
  serializer_class = VehicleTypeSerializer
  permission_classes = [DjangoModelPermissions, IsAdminUser]