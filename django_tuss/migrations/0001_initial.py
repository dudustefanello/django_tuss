# Generated by Django 5.1 on 2024-08-16 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSystem',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='nome')),
                ('url', models.URLField(max_length=256)),
                ('version', models.CharField(blank=True, max_length=32, null=True, verbose_name='versão')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='título')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='descrição')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='data')),
                ('publisher', models.CharField(blank=True, max_length=128, null=True, verbose_name='autor')),
                ('em_uso', models.BooleanField(default=True, verbose_name='em uso')),
                ('atualizada', models.DateTimeField(auto_now=True, verbose_name='atualizada em')),
            ],
            options={
                'verbose_name': 'sistema de código',
                'verbose_name_plural': 'sistemas de códigos',
            },
        ),
        migrations.CreateModel(
            name='CodeSystemContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, verbose_name='código')),
                ('display', models.TextField(verbose_name='descrição')),
                ('code_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_tuss.codesystem', verbose_name='sistema de código')),
            ],
            options={
                'verbose_name': 'conteúdo sistema de código',
                'verbose_name_plural': 'conteúdos dos sistemas de códigos',
                'unique_together': {('code_system', 'code')},
            },
        ),
    ]
