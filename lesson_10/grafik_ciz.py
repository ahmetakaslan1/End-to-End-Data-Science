import pandas as pd
import matplotlib.pyplot as plt

# 1. Veriyi Oku
df = pd.read_csv("satis_verileri.csv")

# 2. Şehirlere göre satışları topla (Ders 7'de yaptığımız gibi)
sehir_toplamlari = df.groupby("Sehir")["Satis_Miktari"].sum()

# 3. Görselleştirme (Bar Grafik - Çubuk Grafik)
# Pandas, matplotlib altyapısını kullanarak tek satırda grafik çizebilir:
sehir_toplamlari.plot(kind="pie", color=["blue", "orange", "green"])

# 4. Grafiğe Başlık Ekle ve Göster
plt.title("Şehirlere Göre Toplam Satışlar")
plt.ylabel("Toplam Satış (TL)")
plt.xlabel("Şehirler")
plt.tight_layout() # Yazıların sıkışmasını/kesilmesini önler

print("Grafik oluşturuluyor... Lütfen açılan pencereyi inceleyin.")
# Grafiği ekranda gösteren komut:
plt.show()
