import requests
import csv
import pytz
from django.utils.dateparse import parse_datetime
from django.core.management.base import BaseCommand

from patients.models import HourlyData

URL = "http://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours.csv"

FACILITY_NAME = "Nom_etablissement "
INSTALLATION_NAME = " Nom_installation "
LICENSE = " No_permis_installation "
STRETCHERS = " Nombre_de_civieres_fonctionnelles "
PATIENTS = " Nombre_de_civieres_occupees "
PATIENTS_24 = " Nombre_de_patients_sur_civiere_plus_de_24_heures "
PATIENTS_48 = " Nombre_de_patients_sur_civiere_plus_de_48_heures "
EXTRACTED_AT = " Heure_de_l'extraction_(image) "
UPDATED_AT = " Mise_a_jour"


class Command(BaseCommand):
    help = "Fetch hourly data"

    def handle(self, *args, **options):
        response = requests.get(URL)
        response.raise_for_status()
        reader = csv.DictReader(response.text.splitlines())

        for row in reader:
            HourlyData.objects.get_or_create(
                facility_name=row[FACILITY_NAME],
                updated_at=pytz.timezone("America/Montreal").localize(
                    parse_datetime(row[UPDATED_AT])
                ),
                defaults={
                    "installation_name": row[INSTALLATION_NAME],
                    "license": row[LICENSE],
                    "stretchers": row[STRETCHERS],
                    "patients": row[PATIENTS],
                    "patients_24": row[PATIENTS_24],
                    "patients_48": row[PATIENTS_48],
                    "extracted_at": row[EXTRACTED_AT],
                },
            )

        self.stdout.write(self.style.SUCCESS("Data fetched successfully"))
