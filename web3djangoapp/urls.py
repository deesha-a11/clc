from django.urls import path
from .views import ( TokenObtainPairView,)
from django.urls import path
from .views import UserListCreateView, UserDetailView
from .views import UserListCreateView, UserDetailView, CurrentUserView


urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
        # JWT Login
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]

