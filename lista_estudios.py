from invenio.dbquery import run_sql

from .estudio import Estudio


def es_valido_tipo(tipo_estudio):
     if not isinstance(tipo_estudio, int):
         return False
     res = run_sql("SELECT DISTINCT tipo_estudio FROM uz_ESTUDIOS_TIPOS")
     tipos_validos = [x[0] for x in res]
     return (tipo_estudio in tipos_validos)


class Lista_Estudios(object):
    def __init__(self, tipo_estudio=None):
        self._estudios = {}
        if tipo_estudio is None:
            # crear lista con todos los estudios
            res = run_sql("SELECT DISTINCT codigo_estudio_sigma FROM uz_ESTUDIOS")
        elif es_valido_tipo(tipo_estudio):
            res = run_sql("SELECT DISTINCT codigo_estudio_sigma FROM uz_ESTUDIOS WHERE tipo_estudio={}".format(tipo_estudio))
        for r in res:
            codigo_estudio = int(r[0])
            self._estudios[codigo_estudio] = Estudio(codigo_estudio)


    def names_es(self):
        ''' devuelve un dict con los codigos sigma como keys y los nombres en espanol como value '''
        names = {}
        for c in self._estudios:
            names[c]=self._estudios[c].nombre_es
        return names

    def renderSelect(self, selectId='lista_estudios'):
        # sort by nombre_es
        ordenados_por_nombre = sorted(self.names_es().items(), key=lambda x: x[1]) 

        out="<select id={}>".format(selectId)
        for cod in ordenados_por_nombre:
            out += '<option value="{}">{}</option>'.format(cod[0], cod[1])
        out+="</select>"
        return out


class Programas_Doctorado(Lista_Estudios):

    def __init__(self):
        super(Programas_Doctorado, self).__init__(tipo_estudio=7)
