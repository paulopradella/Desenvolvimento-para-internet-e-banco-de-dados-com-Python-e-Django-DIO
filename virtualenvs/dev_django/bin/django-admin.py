#!/Users/paulo.pradella/OneDrive/Cursos Diversos/Cursos DIO/Cursos Python/Desenvolvimento pra Internet e Banco de dados com Python e Django/DESENVOLVIMENTO-PARA-INTERNET-E-BANCO-DE-DADOS-COM-PYTHON-E-DJANDO-DIO/virtualenvs/dev_django/bin/python3
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
