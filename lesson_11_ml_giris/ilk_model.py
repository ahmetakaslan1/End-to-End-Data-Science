import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Veriyi Oku
df = pd.read_csv("ml_verisi.csv")

# 2. X ve Y'yi Ayır
# X (Özellikler / Features): Modelin bakıp öğreneceği veriler
X = df[["Musteri_Yas", "Sitede_Gecirilen_Dakika"]]

# y (Hedef / Target): Modelin tahmin etmeye çalışacağı değer (Sonuç)
y = df["Harcama_TL"]

# 3. Modeli Oluştur ve Eğit (Öğrenme aşaması)
model = LinearRegression()
model.fit(X, y) # "Al bu X'lere bak, Y'leri nasıl oluşturduğunu öğren" diyoruz.

# 4. Geleceği Tahmin Et (Prediction)
yeni_musteri = pd.DataFrame({"Musteri_Yas": [30], "Sitede_Gecirilen_Dakika": [20]})
tahmin = model.predict(yeni_musteri)

print(f"Yapay Zeka Tahmini (Tüm Veri ile): 30 yaşında ve 20 dk sitede kalan müşteri ortalama {tahmin[0]:.2f} TL harcar.")


# ==============================================================================
# SENİN MÜHENDİSLİK MANTIĞINLA GELEN: "MODELİ TEST ETME" AŞAMASI
# ==============================================================================
print("\n" + "*"*60)
print("GERÇEK SENARYO: MODELİMİZ NE KADAR GÜVENİLİR?")
print("*"*60 + "\n")

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1. Veriyi Eğitim (%80) ve Test (%20) olarak ikiye böl
# Neden veriyi 2'ye bölüyoruz diyoruz ama ortaya 4 değişken çıkıyor?
# Çünkü veriyi hem "Soru/Cevap (X/Y)" olarak hem de "Çalışma/Sınav (Train/Test)" olarak kare şeklinde bölüyoruz:
# Özetle Sınav gibi düşünün X = Soru Y = Cevap vede 
# train yani modelin öğreneme aşamasındaki veriler.
# test yani modelin sınav tahmin ( test ) verileri.
# +---------------+---------------------------------------+----------------------------------------+
# |               | EĞİTİM VERİSİ (%80 - Ders Çalışma)    | TEST VERİSİ (%20 - Sınav Aşaması)      |
# +---------------+---------------------------------------+----------------------------------------+
# | X (Sorular)   | X_train (Modelin çalıştığı sorular)   | X_test (Sınavda sorulacak sorular)     |
# | y (Cevaplar)  | y_train (Çalışırken baktığı cevaplar) | y_test (Sınavı kontrol için bizde kalan|
# |               |                                       |         gerçek cevap anahtarı)         |
# +---------------+---------------------------------------+----------------------------------------+
# Yazım syntax bu sıra ile verilmediğinde hata alırız.
# Sağdan sola okunursa daha anlaşılır olur. Yani X_train ve  X_test = X'ten alınacak %80 %20'lik veriler vs.
# y_train ve y_test = y'den alınacak %80 %20'lik veriler vs.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Toplam Veri: {len(X)} satır. Eğitim için {len(X_train)} satır, Test (Sınav) için {len(X_test)} satır ayrıldı.\n")

# 2. Modeli SADECE Eğitim (Train) verisiyle baştan eğit
gercek_model = LinearRegression()
gercek_model.fit(X_train, y_train)

# 3. Modelden, daha önce HİÇ GÖRMEDİĞİ Test verisi ile tahminler yapmasını isteyelim
test_tahminleri = gercek_model.predict(X_test)

# 4. Tahminleri gerçek cevaplarla karşılaştırarak birkaç örnek görelim:
print("--- Sınav Aşaması: Tahminler vs Gerçekler ---")
# zip kullanarak test verisinin gerçek sonuçları ile modelin tahminlerini eşleştiriyoruz
for i, (gercek, tahmin) in enumerate(zip(y_test, test_tahminleri)):
    print(f"Örnek {i+1} -> Gerçekte Harcanan: {gercek} TL | Modelin Tahmini: {tahmin:.2f} TL")

# 5. Genel Başarı Puanı (Ortalama Mutlak Hata - MAE)
mae = mean_absolute_error(y_test, test_tahminleri)
print(f"\n--- Sonuç Karinesi ---")
print(f"Modelimiz hiç görmediği müşterilerin harcamalarını tahmin ederken ORTALAMA {mae:.2f} TL hata payı ile çalışmaktadır.")

# 6. Yüzdelik Başarı Oranı (R² Score - R-Kare Skoru)
# "Hata payı 5 TL ama toplamda % kaç başarılı?" sorusunun cevabı:
# DİKKAT: Biz burada fiyat (TL) gibi "Sayısal" bir tahmin yaptığımız için (Buna Regresyon denir) MAE ve R² kullandık.
# İleride "Evet/Hayır" veya "Hangi Kategori?" gibi kelimesel (Sınıflandırma) tahminleri yaparken 
# Accuracy (Doğruluk) isimli bambaşka metrikler kullanacağız. Şimdilik sayısal tahmin yaptığımız için R² kullanıyoruz.
from sklearn.metrics import r2_score
basari_orani = r2_score(y_test, test_tahminleri) * 100

print("\n" + "="*60)
print(f"⭐ MODELİN YÜZDELİK BAŞARI ORANI (R² Score): %{basari_orani:.2f} ⭐")
print("="*60 + "\n")

# 7. MODELİ KAYDETMEK (EXPORT) VE KENDİ TAHMİNİNİ YAPMAK
# Modelimizi eğittik, peki bilgisayarı kapatınca silinip gidecek mi? Hayır!
# joblib kütüphanesi ile eğitilmiş beyni (modeli) bir dosyaya kaydedebiliriz.
import joblib
joblib.dump(gercek_model, "egitilmis_model.joblib")
print("🧠 Modelin beyni 'egitilmis_model.joblib' dosyasına kaydedildi! Artık her seferinde baştan eğitmek zorunda değiliz.\n")



