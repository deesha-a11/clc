from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "username", "email", "first_name", "last_name",
        "role", "department", "employee_id",
        "is_active", "is_staff", "is_superuser",
    )
    list_filter = ("role", "department", "is_active", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {
            "fields": (
                "first_name", "last_name", "email",
                "role", "department", "employee_id"
            )
        }),
        ("Permissions", {
            "fields": (
                "is_active", "is_staff", "is_superuser",
                "groups", "user_permissions"
            )
        }),
        ("Important dates", {"fields": ("last_login", "joined_date")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "first_name", "last_name",
                "role", "department", "employee_id",
                "password1", "password2",
            ),
        }),
    )

    search_fields = ("username", "email", "first_name", "last_name", "employee_id")
    ordering = ("username",)

    # ✅ joined_date is auto_now_add → make it readonly
    readonly_fields = ("joined_date",)

    def get_readonly_fields(self, request, obj=None):
        """
        Make sure that for superadmin, is_active / is_staff / is_superuser
        cannot be unchecked in the admin.
        """
        readonly = list(super().get_readonly_fields(request, obj))
        if obj and obj.role == "superadmin":
            readonly += ["is_active", "is_staff", "is_superuser"]
        return readonly
