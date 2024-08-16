from django.contrib import admin

from django_tuss.models import CodeSystem, CodeSystemContent


admin.site.register(CodeSystem)
admin.site.register(CodeSystemContent)
