from rest_framework import serializers
from .models import WorkshopEntry
from .models import Workshopattendees

class WorkshopEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopEntry
        fields = '__all__'
from .models import WorkshopEntry

class WorkshopattendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshopattendees
        fields = '__all__'
