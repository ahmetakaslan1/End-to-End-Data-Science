import pandas as pd

# CSV dosyasını okuyalım
df = pd.read_csv("musteriler.csv")

# Tablonun ilk birkaç satırını ekrana yazdıralım
print(df.head())
