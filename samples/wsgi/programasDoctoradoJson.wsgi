# -*- coding: utf-8 -*-

import os, sys, urlparse

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

from estudios.lista_estudios import Programas_Doctorado

def application(environ, start_response):
    """ Obtener todos los estudios de tipo doctorado """ 

    status = '200 OK'
    output = ''

    pd = Programas_Doctorado()
    #output += pd.renderSelect(selectId='lista_doctorados')
    output += pd.toJson()

    #response_headers = [('Content-type', 'text/html'),
    #                    ('Content-Length', str(len(output)))]

    response_headers = [('Content-type', 'application/json'),
                    ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
