def atk(jrc:str, jrhp:float, dano:float): 
    jrhp -= dano
    jrc += 'BAREL ||'
    return jrhp, jrc