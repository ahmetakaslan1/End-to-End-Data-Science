import pandas as pd

df = pd.read_csv("kategorik_veri.csv")
print("--- Doldurulmadan Önce ---")
print(df)

# En çok tekrar eden şehri (Mod - Mode) bulalım
# mode() fonksiyonu birden fazla değer dönebileceği için ilkini [0] alıyoruz
en_cok_tekrar_eden = df["Sehir"].mode()[0]

# Eksik (NaN) şehirleri bu değer ile dolduralım
df["Sehir"] = df["Sehir"].fillna(en_cok_tekrar_eden)

print(f"\nBoş şehir hücreleri, en çok tekrar eden '{en_cok_tekrar_eden}' ile dolduruldu.")
print("\n--- Doldurulduktan Sonra ---")
print(df)
