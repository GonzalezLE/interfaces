from classes.Mini_vidas import Mini_vidas


if __name__ == '__main__':

    STRING = """
    b''
    b'\x05'
    b''
    b''
    b'\x02\x1emtrsl|\x1epi|\x1epn|\x1esi|\x1eciTIC21103806|\x1ertATPO|\x1ernAnti-TPO|\x1ett13:55|\x1etd12/07/21|\x1eql|\x1eqn274.0 IU/ml|\x1d37'
    b''
    b'\x03\x04'
    b''
    """
    
    obj = Mini_vidas('Mini vidad', '01', STRING)

    print(obj.Parse())

    # print(obj.cadena)
