import json
from classes.parse import Parse

STRING ="""
b''
b''
b'\x05'
b'\x021H|\\^&|||ABX|||||||P|E1394-97|20221207152047\r\x0356\r\n'
b'\x022P|1||||^|||U\r\x0356\r\n'
b'\x023O|1|PCH18740936^10^01||^^^DIF|||||||||||Est\xe1ndar||||||||||F\r\x03C3\r\n'
b'\x024C|1|I|Alarm_ANALYSER^QC|I\r\x03D7\r\n'
b'\x025R|1|^^^WBC^804-5^1|5.2|1||||F||ABX ABX||20221207080634\r\x0320\r\n'
b'\x026R|2|^^^LYM#^731-0^1|1.32|1||||W||ABX ABX||20221207080634\r\x0395\r\n'
b'\x027R|3|^^^LYM%^736-9^1|25.3|1||||W||ABX ABX||20221207080634\r\x03AB\r\n'
b'\x020R|4|^^^MON#^742-7^1|0.37|1||||W||ABX ABX||20221207080634\r\x0396\r\n'
b'\x021R|5|^^^MON%^744-3^1|7.0|1||||W||ABX ABX||20221207080634\r\x0365\r\n'
b'\x022R|6|^^^NEU#^751-8^1|3.34|1||||W||ABX ABX||20221207080634\r\x0399\r\n'
b'\x023R|7|^^^NEU%^770-8^1|63.8|1||||W||ABX ABX||20221207080634\r\x03A5\r\n'
b'\x024R|8|^^^EOS#^711-2^1|0.10|1||||W||ABX ABX||20221207080634\r\x0389\r\n'
b'\x025R|9|^^^EOS%^713-8^1|1.9|1||||W||ABX ABX||20221207080634\r\x036E\r\n'
b'\x026R|10|^^^BAS#^704-7^1|0.10|1||||W||ABX ABX||20221207080634\r\x03AA\r\n'
b'\x027R|11|^^^BAS%^706-2^1|2.0|1||||W||ABX ABX||20221207080634\r\x037C\r\n'
b'\x020R|12|^^^RBC^789-9^1|5.62|1||||W||ABX ABX||20221207080634\r\x039F\r\n'
b'\x021R|13|^^^HGB^717-9^1|19.7|1||HH||F||ABX ABX||20221207080634\r\x0315\r\n'
b'\x022R|14|^^^HCT^4544-3^1|56.7|1||HH||W||ABX ABX||20221207080634\r\x0363\r\n'
b'\x023R|15|^^^MCV^787-2^1|101|1||H||W||ABX ABX||20221207080634\r\x03BA\r\n'
b'\x024R|16|^^^MCH^785-6^1|35.0|1||HH||F||ABX ABX||20221207080634\r\x031B\r\n'
b'\x025R|17|^^^MCHC^786-4^1|34.7|1||||F||ABX ABX||20221207080634\r\x03D5\r\n'
b'\x026R|18|^^^RDW^788-0^1|12.8|1||||F||ABX ABX||20221207080634\r\x03A4\r\n'
b'\x027R|19|^^^PLT^777-3^1|204|1||||W||ABX ABX||20221207080634\r\x0388\r\n'
b'\x020R|20|^^^MPV^776-5^1|9.0|1||||F||ABX ABX||20221207080634\r\x036D\r\n'
b'\x021R|21|^^^RDWSD^2100-5^1|46|1||||F||ABX ABX||20221207080634\r\x03F2\r\n'
b'\x022L|1|N\r\x0305\r\n'
b'\x04'
"""


STRING_2 ="""
b'\x05'
b'\x021H|\\^&|||ABX|||||||P|E1394-97|152146\r\x0356\r\n'
b'\x022P|1||||^|||U\r\x0356\r\n'
b'\x023O|1|PCH18741136^10^02||^^^DIF|||||||||||Est\xe1ndar||||||||||F\r\x03BD\r\n'
b'\x024C|1|I|Alarm_ANALYSER^QC|I\r\x03D7\r\n'
b'\x025R|1|^^^WBC^804-5^1|9.0|1||||F||ABX ABX||20221207080720\r\x031E\r\n'
b'\x026C|1|I|Alarm_WBC^LL|I\r\x035A\r\n'
b'\x027C|2|I|NRBCs|I\r\x03D6\r\n'
b'\x020R|2|^^^LYM#^731-0^1|3.08|1||||W||ABX ABX||20221207080720\r\x0390\r\n'
b'\x021R|3|^^^LYM%^736-9^1|34.1|1||||W||ABX ABX||20221207080720\r\x039F\r\n'
b'\x022R|4|^^^MON#^742-7^1|0.54|1||||W||ABX ABX||20221207080720\r\x0393\r\n'
b'\x023R|5|^^^MON%^744-3^1|6.0|1||||W||ABX ABX||20221207080720\r\x0362\r\n'
b'\x024R|6|^^^NEU#^751-8^1|5.03|1||||W||ABX ABX||20221207080720\r\x0395\r\n'
b'\x025R|7|^^^NEU%^770-8^1|55.6|1||||W||ABX ABX||20221207080720\r\x03A2\r\n'
b'\x026R|8|^^^EOS#^711-2^1|0.30|1||||W||ABX ABX||20221207080720\r\x0389\r\n'
b'\x027R|9|^^^EOS%^713-8^1|3.3|1||||W||ABX ABX||20221207080720\r\x0368\r\n'
b'\x020R|10|^^^BAS#^704-7^1|0.09|1||||F||ABX ABX||20221207080720\r\x0397\r\n'
b'\x021R|11|^^^BAS%^706-2^1|1.0|1||||F||ABX ABX||20221207080720\r\x0360\r\n'
b'\x022R|12|^^^RBC^789-9^1|4.84|1||||F||ABX ABX||20221207080720\r\x038F\r\n'
b'\x023R|13|^^^HGB^717-9^1|14.3|1||||F||ABX ABX||20221207080720\r\x037A\r\n'
b'\x024R|14|^^^HCT^4544-3^1|43.5|1||||F||ABX ABX||20221207080720\r\x03BA\r\n'
b'\x025R|15|^^^MCV^787-2^1|90|1||||F||ABX ABX||20221207080720\r\x0336\r\n'
b'\x026R|16|^^^MCH^785-6^1|29.6|1||||F||ABX ABX||20221207080720\r\x0392\r\n'
b'\x027R|17|^^^MCHC^786-4^1|33.0|1||||F||ABX ABX||20221207080720\r\x03CB\r\n'
b'\x020R|18|^^^RDW^788-0^1|13.1|1||||F||ABX ABX||20221207080720\r\x0394\r\n'
b'\x021R|19|^^^PLT^777-3^1|355|1||||F||ABX ABX||20221207080720\r\x0374\r\n'
b'\x022R|20|^^^MPV^776-5^1|9.1|1||||F||ABX ABX||20221207080720\r\x036C\r\n'
b'\x023R|21|^^^RDWSD^2100-5^1|42|1||||F||ABX ABX||20221207080720\r\x03EC\r\n'
b'\x024L|1|N\r\x0307\r\n'
b'\x04'
"""

if __name__ == '__main__':
    
    separa = """
    #######################################################################################################
    #                                                                                                     #
    #######################################################################################################
    """
    
    obj = Parse(cadena=STRING,posicion_nim=2, udn='01')
    dd = obj.separa_cadena('Horiba')
    
    print(
        json.dumps(
            dd, 
            sort_keys = False, 
            indent = 2)
        )
    print(separa)
    
    
    obj = Parse(cadena=STRING_2,posicion_nim=2, udn='01')
    dd = obj.separa_cadena('Horiba')
    # x = mycol.insert_one(dd)
    print(
        json.dumps(
            dd, 
            sort_keys = False, 
            indent = 2)
        )
    print(separa)
    
    