import pandas as pd
import joblib
from sqlalchemy import create_engine, text

# 1. Veritabanına Bağlan (Docker'da kurduğumuz PostgreSQL)
# Format: postgresql://kullanici_adi:sifre@host:port/veritabani_adi
db_url = "postgresql://admin:gizlisifre@localhost:5432/veri_bilimi_db"
engine = create_engine(db_url)

print("\n--- AŞAMA 1: VERİTABANI HAZIRLIĞI ---")
# 2. Senaryo Gereği: Veritabanında tablo oluşturup yeni müşteriler ekleyelim
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS musteriler (
            id SERIAL PRIMARY KEY,
            yas INT,
            dakika INT,
            harcama_tahmini FLOAT
        );
    """))
    # İçini temizleyip 3 yeni müşteri ekleyelim (Kodu her çalıştırdığımızda temiz başlasın diye)
    conn.execute(text("TRUNCATE TABLE musteriler RESTART IDENTITY;"))
    conn.execute(text("INSERT INTO musteriler (yas, dakika) VALUES (26, 15), (42, 35), (31, 20);"))
    conn.commit()
print("1. Veritabanına bağlanıldı, 'musteriler' tablosu oluşturuldu ve yepyeni müşteriler eklendi.")

print("\n--- AŞAMA 2: VERİYİ ÇEKME VE TAHMİN ---")
# 3. Henüz tahmini yapılmamış müşterileri veritabanından PANDAS ile çek!
df_yeni_musteriler = pd.read_sql("SELECT * FROM musteriler WHERE harcama_tahmini IS NULL", engine)
print("2. Veritabanında tahmini bekleyen (NULL olan) müşteriler çekildi:")
print(df_yeni_musteriler)

# 4. Modeli Yükle (Ders 11'den)
try:
    model = joblib.load("../lesson_11_ml_giris/egitilmis_model.joblib")
    print("\n3. Ders 11'deki yapay zeka beyni hafızaya yüklendi.")
except FileNotFoundError:
    print("HATA: Model bulunamadı. Lütfen önce Ders 11'deki 'ilk_model.py' dosyasını çalıştırıp modeli kaydedin.")
    exit()

# 5. Tahmin Yap (Sadece modelin beklediği kolonları veriyoruz)
X_yeni = df_yeni_musteriler[["yas", "dakika"]]
# Sütun isimleri model eğitilirken "Musteri_Yas" ve "Sitede_Gecirilen_Dakika" idi. İsimleri eşleştirelim.
X_yeni.columns = ["Musteri_Yas", "Sitede_Gecirilen_Dakika"]

tahminler = model.predict(X_yeni)

print("\n--- AŞAMA 3: TAHMİNLERİ SQL'E YAZMA ---")
# 6. Tahminleri Veritabanına Geri Yaz (UPDATE işlemi)
with engine.connect() as conn:
    for index, musteri_id in enumerate(df_yeni_musteriler["id"]):
        bulunan_tahmin = tahminler[index]
        # SQL UPDATE sorgusu ile her ID için tahmin sonucunu yazdırıyoruz
        sorgu = text(f"UPDATE musteriler SET harcama_tahmini = {bulunan_tahmin:.2f} WHERE id = {musteri_id}")
        conn.execute(sorgu)
    conn.commit()

print("4. Tahminler yapıldı ve veritabanına (PostgreSQL) başarıyla KAYDEDİLDİ!")

# Son durumu görmek için veritabanını tekrar okuyalım:
df_son_durum = pd.read_sql("SELECT * FROM musteriler", engine)
print("\n--- VERİTABANININ (MUSTERILER TABLOSUNUN) SON HALİ ---")
print(df_son_durum)


# Burada bizler yeni kayıt olmuş  ve müşteri_yaş, Sitede_Gecirilen_Dakika sütunlarını bildğimiz müşterilerin 
# harcamalarını  tahmin ettik.