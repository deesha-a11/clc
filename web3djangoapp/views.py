
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model  # 👈 FIXED IMPORT
from .serializers import CustomUserSerializer
CustomUser = get_user_model()



User = get_user_model()

# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer




class UserListCreateView(generics.ListCreateAPIView):
    """
    GET -> List all users
    POST -> Create new user
    """
    queryset = CustomUser.objects.all().order_by("-joined_date")
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can view/create

    def perform_create(self, serializer):
        # Prevent anyone from creating a superadmin via API
        if serializer.validated_data.get("role") == "superadmin":
            raise PermissionError("Superadmin cannot be created via API.")
        serializer.save()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET -> Retrieve user details
    PUT/PATCH -> Update user
    DELETE -> Delete user
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Prevent updating/demoting/deleting the superadmin
        instance = self.get_object()
        if instance.role == "superadmin":
            if "role" in serializer.validated_data:
                raise PermissionError("Superadmin role cannot be changed.")
            if "is_active" in serializer.validated_data and not serializer.validated_data["is_active"]:
                raise PermissionError("Superadmin cannot be deactivated.")
        serializer.save()

    def perform_destroy(self, instance):
        # Prevent deleting the superadmin
        if instance.role == "superadmin":
            raise PermissionError("Superadmin cannot be deleted.")
        super().perform_destroy(instance)


class CurrentUserView(APIView):
    """
    Get details of the currently logged-in user
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)









# ----------------- JWT Login -----------------
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customize JWT to include role, department, and employee_id"""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["role"] = user.role
        token["department"] = user.department
        token["employee_id"] = user.employee_id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["role"] = self.user.role
        data["department"] = self.user.department
        data["employee_id"] = self.user.employee_id
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
