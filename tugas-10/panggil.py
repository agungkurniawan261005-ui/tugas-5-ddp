import bangun_datar as bd
import bangun_ruang as br

print("="*4,"Luas Bangun Datar","="*4)
print(f"Luas persegi = {bd.luas_persegi(5)}")
print(f"Luas segitiga = {bd.luas_segitga(5,5)}")
print(f"Luas lingkaran = {bd.luas_lingkaran(10)}")
print(f"Luas ketupat = {bd.luas_ketupat(10,10)}")
print(f"Luas jajar genjang = {bd.luas_jajar_genjang(10,10)}")

print("="*4,"Luas Bangun Ruang","="*4)
print(f"Luas kubus = {br.luas_kubus(10)}")
print(f"Luas balok = {br.luas_balok(10,10,10)}")
print(f"Luas bola = {br.luas_bola(10)}")
print(f"Luas tabung = {br.luas_tabung(10,10)}")
print(f"Luas kerucut = {br.luas_kerucut(10,10)}")