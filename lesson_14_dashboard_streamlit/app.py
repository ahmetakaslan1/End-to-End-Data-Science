import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import joblib

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Müşteri Zekası Paneli", page_icon="🤖", layout="wide")

# 2. BAŞLIK VE AÇIKLAMA
st.title("📊 Müşteri Harcama Tahminleri Dashboard'u")
st.markdown("Bu panel, hem **PostgreSQL** veritabanımızdaki kayıtları canlı olarak görmenizi sağlar hem de sol menüden yepyeni müşteriler için **yapay zeka tahminleri** yapıp doğrudan **veritabanına (tabloya) kaydetmenize** olanak tanır!")

# 3. VERİTABANINA BAĞLAN
db_url = "postgresql://admin:gizlisifre@localhost:5432/veri_bilimi_db"
engine = create_engine(db_url)


# 4. SOL MENÜ (Sidebar) - CANLI TAHMİN VE VERİTABANINA KAYIT
st.sidebar.header("🤖 Canlı Tahmin Motoru")
st.sidebar.write("Yeni bir müşteri için tahmin yapın ve veritabanına ekleyin:")

yeni_yas = st.sidebar.number_input("Müşteri Yaşı:", min_value=18, max_value=80, value=30)
yeni_dakika = st.sidebar.number_input("Sitede Geçirdiği Dakika:", min_value=1, max_value=120, value=20)

# "Hemen Tahmin Et" Butonu
if st.sidebar.button("Hemen Tahmin Et"):
    try:
        model = joblib.load("../lesson_11_ml_giris/egitilmis_model.joblib")
        yeni_veri = pd.DataFrame({"Musteri_Yas": [yeni_yas], "Sitede_Gecirilen_Dakika": [yeni_dakika]})
        tahmin_sonucu = float(model.predict(yeni_veri)[0])
        
        # Tahmin sonucunu Streamlit'in hafızasına (Session State) kaydediyoruz
        st.session_state["gecici_tahmin"] = tahmin_sonucu
        st.session_state["gecici_yas"] = yeni_yas
        st.session_state["gecici_dakika"] = yeni_dakika
    except Exception as e:
        st.sidebar.error(f"Model yüklenemedi. Detay: {e}")

# Eğer hafızada bir tahmin varsa (yani butona basıldıysa) sonucu ve "Kaydet" butonunu göster
if "gecici_tahmin" in st.session_state:
    st.sidebar.success(f"Yapay Zeka Tahmini: **{st.session_state['gecici_tahmin']:.2f} TL**")
    
    if st.sidebar.button("💾 Tabloya (Veritabanına) Ekle"):
        # SQL INSERT komutu ile yeni kaydı PostgreSQL'e yazıyoruz
        with engine.connect() as conn:
            sorgu = text(f"INSERT INTO musteriler (yas, dakika, harcama_tahmini) VALUES ({st.session_state['gecici_yas']}, {st.session_state['gecici_dakika']}, {st.session_state['gecici_tahmin']:.2f})")
            conn.execute(sorgu)
            conn.commit()
            
        # İşlem bitince hafızayı temizle ve sayfayı yenile (Rerun) ki tablo güncellensin!
        del st.session_state["gecici_tahmin"]
        st.rerun()


# 5. ANA EKRAN - VERİTABANINDAN GÜNCEL VERİYİ ÇEK VE GÖSTER
try:
    df = pd.read_sql("SELECT * FROM musteriler", engine)
    df = df.dropna(subset=["harcama_tahmini"])
except Exception as e:
    st.error(f"❌ Veritabanına bağlanılamadı. Hata Detayı: {e}")
    st.stop()

if df.empty:
    st.warning("⚠️ Veritabanında şu an gösterilecek kayıt bulunmuyor.")
    st.stop()


# 6. GÖRSELLEŞTİRME VE TABLO (Sade ve Temiz Görünüm)
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Veritabanındaki Canlı Tablo")
    st.write("*(En son eklenen kayıtlar en üstte görünür)*")
    # Tabloyu ID'ye göre ters sıralıyoruz ki yeni eklediklerimizi anında en üstte görelim
    st.dataframe(df.sort_values(by="id", ascending=False), use_container_width=True)

with col2:
    st.subheader("📈 Yaş, Dakika ve Harcama İlişkisi")
    st.write("*(Nokta boyutu = Sitede geçirilen dakika)*")
    # 3 Değişkeni aynı anda göstermek için Scatter (Dağılım) grafiği kullanıyoruz
    st.scatter_chart(
        df,
        x="yas",
        y="harcama_tahmini",
        size="dakika"
    )
