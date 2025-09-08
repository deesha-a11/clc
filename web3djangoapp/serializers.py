from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
            "role",
            "department",
            "employee_id",
            "joined_date",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
        read_only_fields = ["id", "joined_date", "is_superuser"]

    def validate(self, attrs):
        """Ensure passwords match."""
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        """Create a new user with hashed password."""
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Update user details & re-hash password if provided."""
        validated_data.pop("confirm_password", None)
        password = validated_data.pop("password", None)
        if password:
            instance.password = make_password(password)
        return super().update(instance, validated_data)
