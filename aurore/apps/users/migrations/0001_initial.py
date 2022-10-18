# Generated by Django 4.1.2 on 2022-10-18 17:33

import aurore.apps.users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "__first__"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="First name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="Last name"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="users/avatars",
                        verbose_name="Profile image",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="Phone number"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        default="M",
                        max_length=2,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of birth"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("jwt_key", models.UUIDField(default=uuid.uuid4)),
                ("social_auth", models.BooleanField(default=False)),
                ("note", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", aurore.apps.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=255, verbose_name="Name"),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="First name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Last name"
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=255,
                        verbose_name="Company name",
                    ),
                ),
                (
                    "street_address_1",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Street address 1"
                    ),
                ),
                (
                    "street_address_2",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Street address 2"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=255, verbose_name="City"),
                ),
                (
                    "city_area",
                    models.CharField(
                        blank=True, default="", max_length=255, verbose_name="City area"
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True,
                        default="",
                        help_text="Country of the address.",
                        max_length=2,
                        verbose_name="Country",
                    ),
                ),
                (
                    "country_area",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=255,
                        verbose_name="Country area",
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=255,
                        verbose_name="Postal code",
                    ),
                ),
                (
                    "phone",
                    aurore.apps.users.models.PossiblePhoneNumberField(
                        blank=True,
                        default="",
                        help_text="In case we need to call you.",
                        max_length=128,
                        region=None,
                        verbose_name="Phone number",
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
                "ordering": ("pk",),
            },
        ),
        migrations.CreateModel(
            name="UserOptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "options",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="useroptions",
                        to="common.options",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="useroptions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="addresses",
            field=models.ManyToManyField(
                blank=True, related_name="user_addresses", to="users.address"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="default_billing_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="users.address",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="default_shipping_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="users.address",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="options",
            field=models.ManyToManyField(
                blank=True,
                related_name="options",
                through="users.UserOptions",
                to="common.options",
                verbose_name="Options",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]