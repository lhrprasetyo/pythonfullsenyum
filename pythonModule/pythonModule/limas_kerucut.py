def luas_limas(luas_sisi_alas:float,luas_sisi_tegak:float):
    return luas_sisi_alas + luas_sisi_tegak

def volume_limas(luas_alas:float,t:float):
    return 1/3 * luas_alas*t

def luas_kerucut(r:float,s:float):
    return (3.14*r**2)+(3.14*r*s)

def volume_kerucut(r:float,t:float):
    return 1/3*3.14*r**2*t