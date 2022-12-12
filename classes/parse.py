import re
from datetime import datetime
from typing import List
from classes.Vitros import Vitros
from classes.Horiba import Horiba
from classes.General_resuls import General_resuls

from settings.settings import WORDS_OF_CONTROL


class Parse():

    def __init__(self, cadena:str,posicion_nim:int,udn:str):
        """_summary_

        Args:
            cadena (str): Cadena en crudo como viene del equipo
            posicion_nim (int): Posicion del nim
        """
        # super().__init__(cadena=cadena,keywords=keywords_clean)
        self.cadena =  cadena
        self.__posicion_nim = posicion_nim
        self.__udn__ = udn
        self.__equipo__ = ''


    def clean_string(self):
        """Esto limpia la cadena 

        Returns:
            str : cadena limpia
        """
        patters:List = [
            "b''",
            "'\nb'",
            "b'\x05'",
            "b'\x02",
            '\x03',
            "b'",
            "'b'",
            '\/n',
            '\/r',
            "'",
            '"',
            "\x02",
            ]
        
        cadena:str = self.cadena
        
        for word in patters:
            cadena = re.sub(word,'',cadena)         
        
        return cadena

    def separa_cadena(self,equipo):
        
        """
            Separo la cadena por los resultados la primera posicion no la tomo en cuenta por que es el header                        
        """
        cadena:str = self.clean_string()
        self.__equipo__ = equipo
        conjuntos = cadena.split('R|')
        
        data = self.finding_the_analyzer(equipo,conjuntos)
        
        """
            creamos arreglo con los estudios
        """        
            
        now = datetime.now()
        _NIM = self.handle_get_nim()
        json_response = {
            'nim' : _NIM,
            'resultados' : data,
            'cadena' : self.cadena,
            'date' : now.strftime('%Y-%m-%d'),
            'hour' : f'{now.hour}:{now.minute}:{now.second}',
            'flag' : 0,
            'branch' : self.__udn__,
            'analyzer' : equipo,
            'is_control':self.is_control()
        }                
        
        return json_response               
    
    def  handle_get_nim(self):
        """ Regresa el nim de la cadena
        
            O|
        Returns:
            _type_: _description_
        """
        try:
            
            cadena = self.cadena
            cadena = cadena.rstrip('\n')
            separa = self.cadena.split('O|',1)   
            
            dataset =  separa[1].split('|')
            nim:str = re.sub(r'[^0-9]', ' ', dataset[self.__posicion_nim])
            nim = nim.strip()
            
            temp_equipo = self.__equipo__
            temp_equipo = temp_equipo.upper()
            
            if temp_equipo == 'VITROS':
                if ' ' in nim:
                    cut_nim:List = nim.split(' ')
                    nim = cut_nim[0]
            
            
            return nim.strip()
        except Exception as e:
            print(f'I have a problem in the generate nim {e}')
            return 'na'
        
    
    def is_control(self):
        """Es para la bandera 
        
        - Esta funcion busca en las cadena las palabras claves para ver si es un control de calidad
        
        Returns:
            int: 0 => si no es un control de calidad 
                 1 => si es control de calida
        """
        
        for  word in WORDS_OF_CONTROL:
            if word in self.cadena:                
                return 1
        
        # si nunca salio es porque no la encontro
        return 0
    
    
    def finding_the_analyzer(self,analyzer:str = '', Dataset:List = []):
        """Busca el analizador por el nombre para llamar a su clase que regresa los resultados

        Args:
            analyzer (str, optional): nombre del analizador. Defaults to ''.
            Dataset (List, optional): Array de resultados sin procesar |R. Defaults to [].

        Returns:
            - List: Arreglo con los resultados ya procesados
                - ejemplo.
                [
                  {
                    'app_code': '',
                    'resultado': '',
                    'unidad': ''
                  },
                ]
        """
        
        response:List = []
        analyzer = analyzer.upper()
        
        if analyzer == 'VITROS':
            object_analizer  = Vitros(Dataset)
            response = object_analizer.__get_app__()
        elif analyzer == 'HORIBA':
            object_analizer  = Horiba(Dataset)
            response = object_analizer.__get_app__()
        else:
            object_analizer  = General_resuls(Dataset)
            response = object_analizer.__get_app__()
        
        return response