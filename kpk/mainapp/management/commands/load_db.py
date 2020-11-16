import json

from django.core.management.base import BaseCommand
from mainapp.models import SubjectCategory


class Command(BaseCommand):
    help = 'Makes reserve copy'

    def handle(self, *args, **options):
        with open('subject_category.json', 'r', encoding='utf-8') as f:
            data_for_resore = json.load(f)

        for item in data_for_resore:
            SubjectCategory.objects.create(**{
                'name': item.name,
                'desc': item.desc,
            })
