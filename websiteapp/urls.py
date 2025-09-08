from django.urls import path
from .views import WorkshopattendeesListCreateView, sample_list

urlpatterns = [
    # API endpoint for WorkshopEntry (GET & POST)

    path("workshop/", WorkshopattendeesListCreateView.as_view(), name="workshop_list_create"),
    # Normal Django template view for SampleEntry
    path("samples/", sample_list, name="sample_list"),
]
