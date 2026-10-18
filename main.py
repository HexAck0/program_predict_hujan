# Program Prediksi Hujan


# KAMUS
# rh = int
# rh_skor = int
# dp = float
# t = float
# dp_dep = float 
# dp_depskor = int
# delta_p = float
# delta_pskor = int
# ind_hujan = str
# ind_hujanskor = int

# ALGORITMA

rh = int(input("Masukkan kelembapan relatif (%): "))
dp = float(input("Masukkan suhu titik jenuh (C): "))
t = float(input("Masukkan suhu udara (C): "))
delta_p = float(input("Masukkan perubahan tekanan dalam 3 jam terakhir (+/- hPa): "))
ind_hujan = str(input("Apakah dalam 3 jam terakhir sudah hujan (Ya/Tidak)? "))

dp_dep = t - dp

if(rh >= 77):
    rh_skor = 2
elif(rh >= 90):
    rh_skor = 3
else:
    rh_skor = 0

if(dp_dep <= 3):
    dp_depskor = 2
else:
    dp_depskor = 0

if(delta_p <= -2):
    delta_pskor = 2
else:
    delta_pskor = 0

if(ind_hujan == "Ya"):
    ind_hujanskor = 1
else:
    ind_hujanskor = 0


total_skor = rh_skor + dp_depskor + delta_pskor + ind_hujanskor

if(total_skor > 5):
    print(f"Terdapat kemungkinan besar akan hujan dengan skor: {total_skor}")
elif(3 < total_skor < 4):
    print(f"Terdapat kemungkinan akan hujan dengan skor: {total_skor}")
else:
    print(f"Terdapat kemungkinan kecil akan hujan dengan skor: {total_skor}")