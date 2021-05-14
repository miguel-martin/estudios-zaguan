import json
from invenio.dbquery import run_sql

class Estudio(object):

    def __init__(self, codigo):

        if not isinstance(codigo, int):
            print("Error: El codigo de estudio debe ser un entero")
            return

        self._codigo_estudio_sigma = codigo

        self._set_attrs()


    def __str__(self):
        self.toJson()

    def _set_attrs(self):
        try:
            res = run_sql("SELECT * from uz_ESTUDIOS where codigo_estudio_sigma = {}".format(self._codigo_estudio_sigma), with_dict=True)
            e = res[0]
        except:
            print("Error al obtener detalles del estudio {}".format(self._codigo_estudio_sigma))
            return
        
        self._ano_academico =  e['ano_academico'] 
        self._codigo_estudio_mec = e['codigo_estudio_mec']
        self._tipo_estudio = e['tipo_estudio']
        self._nombres=self._get_nombres()
        self._planes=self._get_planes() 


    def _get_nombres(self):
        try:
            res = run_sql("SELECT * from uz_ESTUDIOS_NOMBRES where codigo_estudio_sigma={}".format(self._codigo_estudio_sigma), with_dict=True)
            nombres = []
            for r in res:
                nombres.append({r["codigo_idioma"] : r["descripcion"]})
            return nombres
        except:
            print("Error al obtener nombre(s) del estudio {}".format(self._codigo_estudio_sigma))


    def _get_planes(self):

        planes = []
        try:
            res = run_sql("SELECT DISTINCT codigo_plan FROM uz_PLANES WHERE codigo_estudio_sigma={}".format(self._codigo_estudio_sigma), with_dict=True)
        except:
            print("Error al obtener codigos de plan del estudio {}".format(self._codigo_estudio_sigma))

        for r in res:
            planes.append(int(r["codigo_plan"]))
        
        return planes


    def toJson(self):
        return json(self.__dict__)

    
    @property 
    def codigo_estudio_sigma(self):
        return self._codigo_estudio_sigma


    @property
    def nombre_es(self, es_value='es.ES'):
        for i in range(0, len(self._nombres)+1):
            if es_value in self._nombres[i]:
                return self._nombres[i][es_value]
        return ''

    @property
    def planes(self):
        if '_planes' in self.__dict__:
            return self._planes
        return []
       
