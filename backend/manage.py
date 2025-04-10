#!/usr/bin/env python
###Iniando el archivo de configuración manager de Django
import os
import sys
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings') 
    try:
        execute_from_command_line        
    except ImportError as exc:
        raise ImportError(
            'No se pudo importar Django. ¿Estás seguro de que está instalado y disponible en tu PYTHONPATH?'
            ) from exc
        execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

