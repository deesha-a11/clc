from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("superadmin", "Super Admin"),  # Special role
        ("admin", "Admin"),
        ("marketing", "Marketing"),
        ("sales", "Sales"),
        ("support", "Support"),
        ("operations", "Operations"),
        ("finance", "Finance"),
        ("legal", "Legal"),
        ("hr", "HR"),
        ("technology", "Technology"),
        ("itsecurity", "IT & Security"),
        ("auditquality", "Audit & Quality"),
        ("employeemanagement", "Employee Management"),
        ("logistics", "Operations Logistics"),
        ("analytics", "Business Intelligence"),
        ("projectstasks", "Projects & Tasks"),
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default="sales",
    )

    department = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True, null=True)
    employee_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.role} ({self.department})"

    def save(self, *args, **kwargs):
        # ✅ Ensure only one superadmin exists
        if self.role == "superadmin":
            existing_superadmin = CustomUser.objects.filter(role="superadmin").exclude(pk=self.pk)
            if existing_superadmin.exists():
                raise ValidationError("There can only be one Super Admin in the system.")

            # ✅ Always enforce permissions for superadmin
            self.is_active = True
            self.is_staff = True
            self.is_superuser = True

        # ✅ Prevent demotion of superadmin
        if self.pk:
            old_role = CustomUser.objects.get(pk=self.pk).role
            if old_role == "superadmin" and self.role != "superadmin":
                raise ValidationError("Super Admin role cannot be changed or demoted.")

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.role == "superadmin":
            raise ValidationError("Super Admin cannot be deleted.")
        super().delete(*args, **kwargs)
