# Menentukan kategori BMI
# Operator & Percabangan Logika

berat_kg = 60
tinggi_m = 1.69
bmi = berat_kg / (tinggi_m**2)

print(f"Skor BMI anda : {bmi:,.1f}")

if bmi < 18.5:
    kategori = "Berat badan kurang"
elif 18.5 <= bmi < 25.0:
    kategori = "Normal (Ideal)"
elif 25.0 <= bmi < 30.0:
  kategori = "Berat badan berlebih"
else:
  kategori = "Obesitas"

print(f"Kategori: {kategori}")