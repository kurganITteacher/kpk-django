import json

from django.core.management.base import BaseCommand
from mainapp.models import SubjectCategory


class Command(BaseCommand):
    help = 'Makes reserve copy'

    def handle(self, *args, **options):
        items = SubjectCategory.objects.all()
        data_for_dump = []
        for item in items:
            data_for_dump.append({
                'name': item.name,
                'desc': item.desc,
            })
        with open('subject_category.json', 'w', encoding='utf-8') as f:
            json.dump(data_for_dump, f)
