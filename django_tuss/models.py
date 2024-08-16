from django.db import models
from django.utils.translation import gettext_lazy as _


class CodeSystem(models.Model):
    '''
    https://fhir-hm.ans.gov.br/artifacts.html
    '''
    slug = models.CharField(max_length=32, unique=True, primary_key=True, verbose_name=_('id'))
    name = models.CharField(max_length=32, unique=True, verbose_name=_('nome'))
    url = models.URLField(max_length=256)
    version = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('versão'))
    title = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('título'))
    description = models.CharField(max_length=256, null=True, blank=True, verbose_name=_('descrição'))
    date = models.DateTimeField(null=True, blank=True, verbose_name=_('data'))
    publisher = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('autor'))
    em_uso = models.BooleanField(default=True, verbose_name=_('em uso'))
    atualizada = models.DateTimeField(auto_now=True, verbose_name=_('atualizada em'))

    def __str__(self):
        return '{} - {}'.format(self.slug, self.title) or self.slug
    
    class Meta:
        verbose_name = _('sistema de código')
        verbose_name_plural = _('sistemas de códigos')


class CodeSystemContent(models.Model):
    code_system = models.ForeignKey(to='CodeSystem', on_delete=models.CASCADE, verbose_name=_('sistema de código'))
    code = models.CharField(max_length=64, verbose_name=_('código'))
    display = models.TextField(verbose_name=_('descrição'))

    def __str__(self):
        return '{} - {}'.format(self.code, self.display)

    class Meta:
        unique_together = ['code_system', 'code']
        verbose_name = _('conteúdo sistema de código')
        verbose_name_plural = _('conteúdos dos sistemas de códigos')
