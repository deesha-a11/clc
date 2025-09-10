from django.shortcuts import render
from rest_framework import generics
from .models import WorkshopEntry, SampleEntry
from .serializers import WorkshopEntrySerializer  # you must create this serializer

# DRF API View for WorkshopEntry (GET list + POST create)
class WorkshopEntryListCreateView(generics.ListCreateAPIView):
    queryset = WorkshopEntry.objects.all().order_by("-submitted_at")
    serializer_class = WorkshopEntrySerializer


from .models import Workshopattendees, SampleEntry
from .serializers import WorkshopattendeesSerializer  # you must create this serializer

# DRF API View for WorkshopEntry (GET list + POST create)
class WorkshopattendeesListCreateView(generics.ListCreateAPIView):
    queryset = Workshopattendees.objects.all().order_by("-submitted_at")
    serializer_class = WorkshopattendeesSerializer









# Normal Django View for SampleEntry
def sample_list(request):
    samples = SampleEntry.objects.all().order_by("-created_at")
    return render(request, "sample_list.html", {"samples": samples})
