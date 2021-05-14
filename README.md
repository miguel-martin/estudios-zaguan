# Estudios

A python package to manage Estudios
+info https://redmine.unizar.es/issues/4186

## Uso

Ejemplo de doctorados.wsgi

'''
import os, sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

from estudios.lista_estudios import Programas_Doctorado

def application(environ, start_response):
    """ Generar un select con todos los estudios de doctorado ordenados por nombre """

    status = '200 OK'

    pd = Programas_Doctorado()
    output = pd.renderSelect(selectId='lista_doctorados')

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
'''
