from datetime import datetime
from typing import List
import re


class CleanString():

    def __init__(self, cadena: str, keywords: List):
        self.__cadena__ = cadena
        self.___keywords__ = keywords

    def Clean(self):
        """
        This funtion is for clean to string
        """
        cadena: str = self.__cadena__

        for word in self.___keywords__:
            cadena = re.sub(word, '', cadena)

        cadena = cadena.strip()

        return cadena

    def Clean_result(self, result: str):
        result = re.sub('qn', '', result)
        return result


class Mini_vidas(CleanString):

    def __init__(
            self,
            name_of_analyzer: str,
            udn: str,
            cadena: str,
            keywords_clean: List = ["b'\x02", '\x03', '\x04', 'x1', "b'", '\n', '\\\\x1', "'", '"', '', '', '', "'",]):
        
        super().__init__(cadena=cadena, keywords=keywords_clean)

        # limpio mi cadena
        self.cadena: str = self.Clean()
        self.__name_of_analyzer__: str = name_of_analyzer
        self.__udn__: str = udn

    def Parse(self):
        dataset: List[str] = self.cadena.split('|')

        nim: str = dataset[4]
        app: str = dataset[5]

        result_and_unit: str = dataset[10]

        result, unit = self.__get_result_and_unit__(result_and_unit)

        now = datetime.now()

        json = {
            "nim": nim,
            "resultados":
                {
                    'app_code': app,
                    'resultado': result,
                    'unidad': unit
                },
            "cadena": self.cadena,
            "date": now.strftime('%Y-%m-%d'),
            "hour": f'{now.hour}:{now.minute}:{now.second}',
            "flag": False,
            "branch": self.__udn__,
            "analyzer": self.__name_of_analyzer__,
            "is_control": False,
            "epoch": 0
            # "ns": "01" => esta si finciona
        }

        return json

    def __get_result_and_unit__(self, result_and_unit: str):
        """
        Args:
            result_and_unit (str): is the string with the result and unit of measure
        Returns:
            - return 2 vars example

                - result : is the result of test
                - unit : is the unit of measure
        """

        result_and_unit = self.Clean_result(result_and_unit)

        result: str = ''
        unit: str = ''

        if ' ' in result_and_unit:

            dataset_result_and_unit = result_and_unit.split(' ')
            result = dataset_result_and_unit[0]
            unit = dataset_result_and_unit[1]
            return result, unit

        return result, unit
