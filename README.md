# Estudios

A python package to manage Estudios
+info https://redmine.unizar.es/issues/4186

## Uso

[Ejemplo de WSGI para obtener json de doctorados](samples/wsgi/programasDoctorado.wsgi)
[Ejemplo de WSGI para obtener json de codigos de plan de un estudio determinado](samples/wsgi/planesEstudioJson.wsgi)
[Ejemplo de como consumir con JS el endopoint de doctorados](samples/js/index.js)

</script>
```

## Consideraciones

Para que funcione correctamente hay que tener instalado invenio y ademas las siguientes tablas definidas en la BD

```
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
```

