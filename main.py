# Program Prediksi Hujan
# Kelompok 1
# Muhammad Fatkhi Rakhman (16326007)
#Aiman Adhipramana (16326167)
#Fathur Syahri Raz (16326283)
#Salman Al-Farisi (16326343)
#Sayyid Abdullah Dinnejjad (16326383)


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
rh = float(input("Masukkan kelembapan relatif dalam persentase (angka 0-100): "))
while(rh < 0 or rh > 100):
    print("Kelemnbapan relatif diluar jangkauan (0-100).")
    rh = float(input("Masukkan kelembapan relatif dalam persentase (angka 0-100): "))

t = float(input("Masukkan suhu udara (C): "))
dp = float(input("Masukkan suhu titik jenuh (C): "))
while (dp > t or dp < 0):
    print("Suhu titik jenuh tidak bisa lebih dari suhu udara, atau kurang dari 0 C.")
    dp = float(input("Masukkan suhu titik jenuh (C): "))

p_aw = float(input("Masukkan tekanan atmosfer awal (hPa): "))
while (p_aw < 0):
    print("Tekanan tidak bisa kurang dari 0 hPa.")
    p_aw = float(input("Masukkan tekanan atmosfer awal dalam waktu 3 jam (hPa): "))
    
p_akh = float(input("Masukkan tekanan atmosfer akhir dalam waktu 3 jam (hPa): "))
while (p_akh < 0):
    print("Tekanan tidak bisa kurang dari 0 hPa.")
    p_akh = float(input("Masukkan tekanan atmosfer akhir (hPa): "))

ind_hujan = str(input("Apakah dalam 3 jam terakhir sudah hujan (ya/tidak)? "))
while (ind_hujan != "ya" and ind_hujan != "tidak"):
    print("Jawaban hanya menerima 'ya' atau 'tidak'.")
    ind_hujan = str(input("Apakah dalam 3 jam terakhir sudah hujan ya/tidak)? "))

# Subprogram Perhitungan Perbedaan Tekanan
def hitung_delta_p(p_aw, p_akh):
    delta_p = p_akh - p_aw
    return delta_p

# Subprogram Perhitungan Dewpoint
def hitung_dewpoint(t, dp):
    dp_depression = t - dp
    return dp_depression

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
if(ind_hujan == "ya"):
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