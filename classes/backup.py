from typing import Dict, List
import json


class Backup:
    def __init__(self, router: str = "./classes/Backup_QC.json"):
        """_summary_

        Args:
            router (str, optional): ruta donde se encuentra el json para los backups. Defaults to './classes/Backup_QC.json'.
        """

        self.__router_file = router

    def add_json(self, __json__: Dict):
        """agrega elementos al json

        Args:
            __json__ (Dict): nodo o json que se va a agregar al archivo json.

        Returns:
            Dict: El nodo o json que se inserto
        """
        with open(self.__router_file, "r+", encoding="utf-8") as file:

            data = json.load(file)
            data.append(__json__)
            file.seek(0)
            json.dump(data, file, indent=2, sort_keys=True)

        return __json__

    def __handle_get_length__(self):
        """regresa el tamaño del json

        Returns:
            int: tamaño del json
        """
        counter: int = 0

        with open(self.__router_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            counter = len(data)
            file.close()

        return counter

    def __get_data__(self):
        """regresa todos los datos del json

        Returns:
            List[Dict]: regresa el json
        """

        response: List[Dict] = []

        with open(self.__router_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            response = data
            file.close()

        return response

    def __update_json__(self, new_json: List[Dict]):
        """Actualiza todo el json
        
        Args:
            new_json (List[Dict]): Los nuevo datos para el json
            
        Returns:
            bool: True se actualizo
                False no se actualizo
        """
        try:
            with open(self.__router_file, "w+", encoding="utf-8") as file:
                json.dump(new_json, file, indent=2, sort_keys=True)
                file.close()
                return True
            
            return False
            
        except Exception as e:
            return False
        
