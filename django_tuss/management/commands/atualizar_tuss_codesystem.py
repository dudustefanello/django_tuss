import requests

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from django_tuss.models import CodeSystem, CodeSystemContent


class Command(BaseCommand):
    help = _('Atualiza o conteúdo do CodeSystem para todos os registros ativos')

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for code in CodeSystem.objects.filter(em_uso=True):
            try:
                with transaction.atomic():
                    response = requests.request('GET', code.url)
                    result = response.json()

                    code.version = result['version']
                    code.name = result['name']
                    code.title = result['title']
                    code.date = result['date']
                    code.publisher = result['publisher']
                    code.description = result['description']
                    code.save()

                    for concept in result['concept']:
                        CodeSystemContent.objects.update_or_create(
                            code_system=code,
                            code=concept['code'],
                            defaults={'display': concept['display']},
                        )

                    print('{}: {}'.format(_('Sistema'), code.slug), end='\t')
                    print('{}: {}'.format(_('Status'), response.status_code), end='\t')
                    print('{}: {}'.format(_('Códigos'), len(result['concept'])))
            except Exception as e:
                    print('{}: {}'.format(_('Sistema'), code.slug), end='\t')
                    print('{}: {}'.format(_('Exceção'), e))
