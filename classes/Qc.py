from typing import Dict,List
import json

import requests
from settings.settings import  URL_API_QC

from classes.backup import Backup

class Qc(Backup):
    
    def __init__(self):
        super().__init__()
    
    
    def handle_send_qc(self,data_json:Dict):
        """Manda las controles de calidad a la nube

        Args:
            data_json (Dict): Es el json que se va a mandar.
        """
        try:
            
            print('''
                **********************************************************
                *              guardando control de calidad              *
                **********************************************************
                ''')
            
            
            
            request = requests.post(URL_API_QC,data = json.dumps(data_json))
            
            if request.status_code == 200 :
                print(json.dumps(request.json(), indent = 4, separators=(","," : ")))
                self.__handle_send_json__()
            else:
                self.add_json(data_json)
            
            
            return data_json
        
        except Exception as e:
            self.add_json(data_json)
            
    
    def __handle_send_json__(self):
        try:
            # si existen datos los mandamos
            if self.__handle_get_length__() > 0:
                
                new_list:List[Dict] = []
                
                for elemets in self.__get_data__():
                    try:
                        request = requests.post(URL_API_QC,data = json.dumps(elemets))
                        if request.status_code != 200:
                            # Si paso algo lo guardamos en el json
                            new_list.append(elemets)
                        else:
                            print('log guardado')
                    except Exception as e:
                        error = e
                        # Si paso algo lo guardamos en el json
                        new_list.append(elemets)
                self.__update_json__(new_list)
        except Exception as e:
            pass