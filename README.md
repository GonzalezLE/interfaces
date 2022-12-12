## settings

### settings>settings.py

- Archivo de configuracion:

  - WORDS_OF_CONTROL

    Listado de palabras claves para saber que es un control de calidad.

  - URL_API_QC

    Url de la api donde van a caer los controles de calidad.

  - URL_MONGO

    La url de la base de datos de mongo

  - name_database

    nombre de la base de datos de mongo

  - name_collection

    Nombre se la coleccion donde se van a insertar los datos.

> Como usar clases

Para los equipos

- Vitros
- Horiba

```

from classes.parse import Parse

if __name__ == '__main__':

  '''
    cadena : la cadena del analizador

    posicion_nim: la posicion donde esta el nim
      - horiba : 2
      - vitros : 1

    udn: codigo de la udn

    separa_cadena
    
  '''
  obj = Parse(cadena=STRING,posicion_nim=2, udn='01')

  '''
  obj.separa_cadena('nombre del equipo') La funcion recibe como argumento el nombre del equipo
    - horiba : 'Horiba'
    - vitros : 'vitros'

  '''
  json = obj.separa_cadena('nombre del equipo')
  # json = json procesado
```

para el equipo Mini vidas

```
from classes.Mini_vidas import Mini_vidas

if __name__ == '__main__':

  obj = Mini_vidas('Mini vidad', '01', Cadena_del_analizador)

  # Regresa el json procesado
  obj.Parse()
```


