# Program Prediksi Hujan
# Memprediiksi apakah akan terjadi hujan berdasarkan syarat-syarat tertentu
# yang ditentukan melalui skor

# KAMUS
# rh = float
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

# Input tiap variabel
rh = float(input("Masukkan kelembapan relatif (%): "))
dp = float(input("Masukkan suhu titik jenuh (C): "))
t = float(input("Masukkan suhu udara (C): "))
p_aw = float(input("Masukkan tekanan awal (hPA): "))
p_akh = float(input("Masukkan tekanan akhir (hPA): "))
ind_hujan = str(input("Apakah dalam 3 jam terakhir sudah hujan (Ya/Tidak)? "))

def hitung_delta_p(p_aw, p_akh):
    delta_p = p_akh - p_aw
    return delta_p

def hitung_dewpoint(t, dp):
    dp_depression = t - dp
    return dp_depression# Perhitungan Dew Point Depression (Selisih titik embun)

# Skoring Kelembapan Relatif
if(rh >= 90):
    rh_skor = 3
elif(rh >= 77):
    rh_skor = 2
else:
    rh_skor = 0

# Skoring Selisih Titik Embun
if(hitung_dewpoint(t, dp) <= 3):
    dp_depskor = 2
else:
    dp_depskor = 0

# Skoring Perubahan Tekanan
if(hitung_delta_p(p_aw, p_akh) <= -2):
    delta_pskor = 2
else:
    delta_pskor = 0

# Skoring Indikator Hujan
if(ind_hujan == "Ya"):
    ind_hujanskor = 1
else:
    ind_hujanskor = 0

# Perhitungan Total Skor
total_skor = rh_skor + dp_depskor + delta_pskor + ind_hujanskor

# Output
if(total_skor > 5):
    print(f"Terdapat kemungkinan besar akan hujan dengan skor: {total_skor}")
elif(total_skor >= 3):
    print(f"Terdapat kemungkinan akan hujan dengan skor: {total_skor}")
else:
    print(f"Terdapat kemungkinan kecil akan hujan dengan skor: {total_skor}")