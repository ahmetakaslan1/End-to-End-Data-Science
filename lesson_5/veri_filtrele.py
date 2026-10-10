import pandas as pd

# 1. Veriyi Oku
df = pd.read_csv("musteriler.csv")

# 2. Şehri İstanbul olanları filtrele
istanbul_musterileri = df[ df["Sehir"] == "Istanbul" ]

# 3. Sonucu ekrana yazdır
print("--- Tüm Tablo ---")
print(df.head(2)) # Sadece kıyaslama için ilk 2 satır

print("\n--- Sadece İstanbul Müşterileri ---")
print(istanbul_musterileri)
