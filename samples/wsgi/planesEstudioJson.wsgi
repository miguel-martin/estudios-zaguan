# -*- coding: utf-8 -*-

import os, sys, urlparse, json

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

from estudios.estudio import Estudio

def application(environ, start_response):
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

    try:
        e = Estudio(codigo_estudio_sigma)
        #output += e.renderPlanesSelect(selectId='planes')
        output += e.planesJson()
    except Exception as e:
        output += json.dumps([])
 
    #response_headers = [('Content-type', 'text/html'),
    #                    ('Content-Length', str(len(output)))]

    response_headers = [('Content-type', 'application/json'),
                    ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
