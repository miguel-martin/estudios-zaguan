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
    status = '200 OK'

    pd = Programas_Doctorado()
    output = pd.renderSelect(selectId='lista_doctorados')

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
'''

Ejemplo de planesEstudio.wsgi
'''
# -*- coding: utf-8 -*-

import os, sys, urlparse

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

from estudios.estudio import Estudio

def application(environ, start_response):
    """ Obtener todos los estudios de tipo doctorado """

    status = '200 OK'
    output = ''

    try:
        params = urlparse.parse_qs(environ["QUERY_STRING"])
        codigo_estudio_sigma = int(params['codigo_estudio_sigma'][0])
    except Exception as e:
        output += "Debe proporcionar un valor al parametro codigo_estudio_sigma"
        output += "\nERROR: "+ e.message
        response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output]

    e = Estudio(codigo_estudio_sigma)
    output += e.renderPlanesSelect(selectId='planes')

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
'''

## Consideraciones

Para que funcione correctamente hay que tener instalado invenio y ademas las siguientes tablas definidas en la BD

'''
CREATE TABLE uz_ESTUDIOS (
    ano_academico INT UNSIGNED NOT NULL,
    codigo_estudio_sigma INT unsigned NOT NULL PRIMARY KEY,
    codigo_estudio_mec VARCHAR(100) NOT NULL,
    tipo_estudio TINYINT NOT NULL,
    FOREIGN KEY (tipo_estudio) references uz_ESTUDIOS_TIPOS(tipo_estudio) ON DELETE CASCADE
) ENGINE = InnoDB ;

CREATE TABLE uz_ESTUDIOS_TIPOS (
    tipo_estudio TINYINT NOT NULL PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL
) ENGINE = InnoDB ;

CREATE TABLE uz_ESTUDIOS_NOMBRES (
    codigo_estudio_sigma INT unsigned NOT NULL,
    codigo_idioma VARCHAR(6) NOT NULL,
    descripcion VARCHAR(250) NOT NULL,
    PRIMARY KEY (codigo_estudio_sigma, codigo_idioma),
    FOREIGN KEY (codigo_estudio_sigma) references uz_ESTUDIOS(codigo_estudio_sigma) ON DELETE CASCADE
) ENGINE = InnoDB;

CREATE TABLE uz_PLANES (
    codigo_plan INT unsigned NOT NULL PRIMARY KEY,
    codigo_estudio_sigma INT unsigned NOT NULL,
    FOREIGN KEY (codigo_estudio_sigma) references uz_ESTUDIOS(codigo_estudio_sigma) ON DELETE CASCADE
) ENGINE = InnoDB ;
'''
