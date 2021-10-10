from django.db import models


class HourlyData(models.Model):
    facility_name = models.CharField(max_length=255, db_index=True)
    installation_name = models.CharField(max_length=255, db_index=True)
    license = models.IntegerField(help_text="Installation license number")
    stretchers = models.IntegerField(
        blank=True, null=True, db_index=True, help_text="Available Stretchers"
    )
    patients = models.IntegerField(
        blank=True, null=True, db_index=True, help_text="Patients on stretchers"
    )
    patients_24 = models.IntegerField(
        blank=True, null=True, help_text="Patients on stretchers for more than 24h"
    )
    patients_48 = models.IntegerField(
        blank=True, null=True, help_text="Patients on stretchers for more than 48h"
    )
    extracted_at = models.TimeField()
    updated_at = models.DateTimeField()
    model_created_at = models.DateTimeField(auto_now_add=True)
    model_updated_at = models.DateTimeField(auto_now=True)
