from logging import exception
from tkinter import EXCEPTION
from settings.settings import REMOVE_WORDS



class General_resuls():
    
    def __init__(self,results):
        """_summary_

        Args:
            results (Array): Dataset the results to clean
        """
        self.results = results
        
        
    def __get_app__(self):
        
        salto = False
        response = []
        
        for part in self.results:            
            try:
                if salto:
                    part = part.split('|')
                    
                    app_code_dirty = part[1]
                    for word in REMOVE_WORDS:
                        # print(word)
                        app_code_dirty = app_code_dirty.replace(word,'') 
                                        
                    # app_code = re.sub(r'[^a-zA-Z0-9]', ' ', part[1])
                    app_code = app_code_dirty.strip()                
                    try:
                        response.append({                    
                            'app_code': app_code,
                            'resultado': part[2],
                            'unidad': part[3]  
                        })
                    except Exception as e :
                        print(e)
                    
                salto = True
            except exception as err:
                print(f'log get results : {err}')
                
        
        
        return response
