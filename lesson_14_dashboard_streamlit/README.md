# Ders 14: Veri Biliminin Vitrini (Streamlit ile Dashboard)

Yapay zeka modellerini eğitmek ve veritabanına kaydetmek işin mutfağıdır (Backend). Ancak yöneticiler, müşteriler veya diğer departmanlar o veritabanındaki karmaşık SQL tablolarına bakmak istemezler; görsel, anlaşılır ve etkileşimli (interaktif) raporlar görmek isterler (Frontend).

Bu derste Python'un veri bilimciler için geliştirdiği, **hiç HTML, CSS veya Javascript yazmadan** saniyeler içinde web siteleri (Dashboard'lar) yapabildiğimiz devrimsel **Streamlit** kütüphanesini kullanacağız.

### Kurulum
Senin adına `streamlit` kütüphanesini arka planda kuruyorum.

### Adım 1: Web Uygulamasını Çalıştırın!
Streamlit uygulamaları normal Python dosyaları gibi `python app.py` yazılarak **çalıştırılmaz**. Bir web sunucusu (localhost) ayağa kaldırması gerektiği için kendine has bir komutu vardır. Terminalde `lesson_14_dashboard_streamlit` klasörüne geçtikten sonra şu komutu yazmalısın:

```bash
streamlit run app.py
```

Bu komutu yazdığında sisteminde kendi kendine çalışan bir web sunucusu (Server) başlayacak ve otomatik olarak tarayıcında harika bir arayüz açılacak!

### Bu Dashboard Neler Yapıyor?
1. Veritabanına (Docker üzerindeki PostgreSQL) canlı olarak bağlanıyor.
2. Yapay zekanın doldurduğu `harcama_tahmini` sütununu çekiyor.
3. Sol tarafa dinamik bir "Yaş Filtresi" koyuyor. Sen yaş aralığını değiştirdikçe arkadaki veritabanı sorgusu ve grafikler anında güncelleniyor!
4. Müşteri zekasına dayalı "Beklenen Toplam Gelir" gibi özet metrikleri (KPI) hesaplıyor.
