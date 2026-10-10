import pandas as pd

df = pd.read_csv("musteriler.csv")

# Hangi şehir toplamda ne kadar harcama yapmış?
sehir_harcamalari = df.groupby("Sehir")["Harcama_TL"].sum()

print("--- Şehirlere Göre Toplam Harcama ---")
print(sehir_harcamalari)
