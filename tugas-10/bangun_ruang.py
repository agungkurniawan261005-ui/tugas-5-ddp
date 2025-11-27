import math

def luas_kubus(sisi):
    return 6 * (sisi ** 2)
def luas_balok(panjang, lebar, tinggi):
    return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
def luas_bola(jari_jari):
    return 4 * math.pi * (jari_jari ** 2)
def luas_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)
def luas_kerucut(jari_jari, tinggi):
    garis_pelukis = math.sqrt((jari_jari ** 2) + (tinggi ** 2))
    return math.pi * jari_jari * (jari_jari + garis_pelukis)