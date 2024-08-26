## Django Tuss

TUSS é a Terminologia Unificada da Saúde Suplementar do Brasil.

Este projeto busca estruturar esses dados em _Django models_ com métodos para atualizá-los diretamente dos dados públicos da ANS.

### Instalação:

```shell
pip install -i django-tuss
```
```python
# settings.py
INSTALLED_APPS = [
    ...
    'django_tuss',
    ...
]
```
```shell
python manage.py migrate
```

### Comando de atualização:

```shell
python manage.py atualizar_tuss_codesystem
```