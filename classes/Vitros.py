import re
from typing import List,Dict
import itertools
class Vitros():
    
    def __init__(self,results):
        """_summary_

        Args:
            results (Srray): Dataset the results to clean
        """
        self.results:List = results
    
    def __delete_duplicates__(self,results:List[Dict]):
        """this funtion delete duplicates un the array of results
        
        Args:
            results (List[Dict]): array of results

        Returns:
            - List[Dict]: array of results
                - example : 
            ```
            [
                {
                    'app_code': 'app_code',
                    'resultado': 'resultado',
                    'unidad': 'unit'
                },
                {
                    'app_code': 'app_code',
                    'resultado': 'resultado',
                    'unidad': 'unit'
                },
            ]
            ```
                
            
        """
        
        list_of_data_uniq:List[Dict] = []
        
        for data in results:
            if data not in list_of_data_uniq:
                list_of_data_uniq.append(data)
        
        return list_of_data_uniq
        
    
    def __get_app__(self):
        try:
            
            salto:bool = False
            response:List[Dict] = []
            
            for item in self.results:
                if salto:
                    dataset:List = item.split('|')
                    results:str = dataset[1]
                    
                    if '^^^' in results:
                        result_dataset : List = results.split('+')
                        
                        manualdilution:str = f'{result_dataset[0]}'
                        app_code:str = f'{result_dataset[1]}'
                        testdilution:str = f'{result_dataset[2]}'
                        
                        resultado:str = f'{dataset[2]}'
                        unit:str = f'{dataset[3]}'
                        
                        response.append({                    
                            'app_code': app_code,
                            'resultado': resultado,
                            'unidad': unit
                        })
                
                salto = True
            
            response = self.__delete_duplicates__(response)
            
            return response
        except Exception as e:
            print(e)
            return []
    
