# 🚀 End-to-End Data Science Journey



Bu depo, Veri Bilimi (Data Science) dünyasına sıfırdan başlayıp, yapay zeka modellerini canlı bir veritabanı ile entegre ederek "Full-Stack" bir Dashboard'a dönüştürmeye kadar giden uçtan uca (end-to-end) yolculuğumu içermektedir.

Geleneksel kursların aksine, sadece Jupyter Notebook üzerinde model eğitip bırakmak yerine; veriyi işleme, model eğitme, veritabanı (PostgreSQL & Docker) entegrasyonu ve Streamlit ile interaktif web dashboard'u geliştirmeyi kapsayan mimari bir yaklaşım benimsenmiştir.

---

## 🛠️ Kullanılan Teknolojiler (Tech Stack)

* **Veri Analizi ve Bilimi:** Python, Pandas, NumPy, Scikit-Learn
* **Veritabanı & MLOps:** PostgreSQL, Docker, SQLAlchemy, Joblib
* **Görselleştirme & Arayüz:** Matplotlib, Streamlit

---

## 📂 Klasör Yapısı ve Eğitim Serüveni

Her bir klasör (`lesson_XX`) adım adım yeni bir beceriyi inşa etmek üzere tasarlanmıştır.

### Bölüm 1: Temeller (Data Manipulation & Visualization)
* **Lesson 1-10:** Pandas ile veri okuma, temizleme, NaN (boş veri) manipülasyonu, Matplotlib ile veriyi görselleştirme. Veri bilimi dünyasına giriş.

### Bölüm 2: Makine Öğrenmesi (Machine Learning Fundamentals)
* **Lesson 11-12:** Scikit-Learn kullanarak Makine Öğrenmesi algoritması (Linear Regression) kurulması, Train/Test ayrımı, MAE/R2 metrikleri ile modelin başarısının ölçülmesi ve son olarak modelin `joblib` ile diske kaydedilmesi. Ayrıca Overfitting ve gerçek dünya kısıtları üzerine teorik vizyon.

### Bölüm 3: Backend ve Veritabanı Entegrasyonu (MLOps)
* **Lesson 13:** **Docker & PostgreSQL Entegrasyonu!** Laboratuvarda eğitilen modelin gerçek dünyayla buluşması. Docker üzerinde koşan temiz bir PostgreSQL veritabanına bağlanıp, veritabanındaki yeni müşteriler için ML tahminleri yapılması ve SQL `INSERT / UPDATE` komutlarıyla sonuçların veritabanına geri yazılması.

### Bölüm 4: Frontend ve Görselleştirme (Data App)
* **Lesson 14:** **Streamlit Dashboard!** Sadece Backend'de kalmayıp, veritabanındaki ML sonuçlarının yöneticiler ve son kullanıcılar için interaktif, canlı ve filtreli bir Web Arayüzüne (Dashboard) dönüştürülmesi.

### Bölüm 5: İleri Seviye (Gerçek Dünya Senaryoları) - *Devam Ediyor...*
* **Lesson 15 ve Sonrası:** Bu aşamadan itibaren dış dünyadan alınan gerçek ve kirli verilerle çalışılacak, daha güçlü algoritmalar (Sınıflandırma, XGBoost vb.) kullanılacak ve ileri düzey Feature Engineering (Özellik Mühendisliği) yapılacaktır. *(Not: Her derste veritabanı veya dashboard zorunluluğu yoktur; dersler kendi konseptine odaklanır).*

---

## 💡 Vizyon
Bu projedeki asıl amacım sadece algoritmaların matematiğini öğrenmek değil; eğitilen bir yapay zeka modelinin canlı bir sistemde (Production ortamında) veritabanı ve arayüzlerle nasıl entegre çalıştığını kanıtlamaktır. Tam teşekküllü bir **Makine Öğrenmesi Mühendisliği (MLOps)** simülasyonudur.
