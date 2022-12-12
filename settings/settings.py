from typing import List

WORDS_OF_CONTROL : List = [
        'QC-',
        'CONTROL',
        'Level 1',
        'Level 2',
        'QC',
        'qc',
        'qc-',
        'control',
        'level 1',
        'NQ'
    ]

REMOVE_WORDS = ["#^1","^1","#",'^']

""" QC
    Api donde se van a mandar los controles
"""
URL_API_QC : str = ""

"""
    Configuracion para los insert en mongo
"""
URL_MONGO : str = "mongodb://localhost:27017"
name_database : str = "interfaces"
name_collection : str ="dna_labs"
