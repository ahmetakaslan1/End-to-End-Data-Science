import pandas as pd

# Görev 2: Veriyi Okumak
print("--- İlk 5 Satır ---")
df = pd.read_csv("satis_verileri.csv")
print(df.head())

# Görev 1'in KOD Çözümü (Eksik Veriyi Temizlemek/Doldurmak):
print("\n--- Eksik Veri Temizliği ---")
# Mevcut yaşların ortalamasını bulalım:
ortalama_yas = df["Musteri_Yas"].mean()
# NaN (boş) olan yaş hücrelerini bu ortalama ile dolduralım (fillna):
df["Musteri_Yas"] = df["Musteri_Yas"].fillna(ortalama_yas)
print(f"Boş yaş hücreleri, mevcut yaşların ortalaması olan {ortalama_yas:.1f} ile dolduruldu.")

# Görev 3: Filtreleme
print("\n--- Elektronik Kategorisi Satışları ---")
elektronik_satislar = df[ df["Kategori"] == "Elektronik" ]
print(elektronik_satislar)

# Görev 4: Şehirlere Göre Toplam Satış
print("\n--- Şehirlere Göre Toplam Satış (TL) ---")
sehir_toplamlari = df.groupby("Sehir")["Satis_Miktari"].sum()
print(sehir_toplamlari)