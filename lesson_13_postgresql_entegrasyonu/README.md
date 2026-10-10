# Ders 13: Veritabanı Entegrasyonu (PostgreSQL & Docker)

Veri biliminde laboratuvar ortamında (bilgisayarımızda) eğittiğimiz bir modeli gerçek dünyayla (Backend / Canlı Sistem ile) konuşturmanın en iyi yolu, tahminleri doğrudan şirketin veritabanına yazıp okumaktır. 

Bu derste Ders 11'de kaydettiğimiz beyni (`egitilmis_model.joblib`) çağıracak, veritabanına yeni kaydolmuş müşterileri çekecek ve harcamalarını yapay zekaya tahmin ettirip sonuçları tekrar veritabanına kaydedeceğiz.

---

### Neden Docker Kullanıyoruz?
Bir veritabanı (PostgreSQL, MySQL vb.) ile çalışacaksanız, bunu bilgisayarınıza Next-Next-Install şeklinde fiziksel olarak kurmak sisteminizi zamanla kirletir. İlla kullanmak zorunda değilsiniz, standart kurulum da yapabilirsiniz ancak bilgisayarı dağınık bırakmamak ve sistemi temiz tutmak için veritabanını **Docker** üzerinde bir "konteyner" olarak ayağa kaldırmak tam bir **sektör standardıdır**.

### Kurulum ve Çalıştırma Adımları

**Adım 1: Veritabanını Ayağa Kaldır (Docker)**
Bilgisayarında Docker açıksa, terminaline şu komutu yapıştırarak saniyeler içinde sağlam bir PostgreSQL veritabanı başlatabilirsin. En son sürüm yerine kurumsal hayatta çok daha stabil ve oturmuş kabul edilen **PostgreSQL 15** sürümünü kullanıyoruz:

```bash
docker run --name veri_bilimi_db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=gizlisifre -e POSTGRES_DB=veri_bilimi_db -v "${PWD}/pg_data:/var/lib/postgresql/data" -p 5432:5432 -d postgres:15
```
*(Bu komut; `admin` kullanıcısıyla, `veri_bilimi_db` isimli bir veritabanı ayağa kaldırır. `-v` parametresi sayesinde veritabanındaki tüm kayıtlar, bulunduğumuz klasörün içindeki `pg_data` klasörüne fiziksel olarak kaydedilir. Konteyner silinse bile verileriniz asla kaybolmaz!)*

**Adım 2: Gerekli Python Kütüphanelerini Kur**
Python kodumuzun veritabanıyla konuşabilmesi (SQL sorguları atabilmesi) için terminale şu komutu yazarak kütüphaneleri kurmalısın:
```bash
pip install psycopg2-binary sqlalchemy
```

**Adım 3: Kodu Çalıştır!**
Bu klasördeki `db_yaz.py` dosyasını terminalden `python db_yaz.py` yazarak çalıştır. Kod kendi kendine şunları yapacak:
1. Docker'daki PostgreSQL'e bağlanacak.
2. Otomatik olarak bir `musteriler` tablosu oluşturup, içine henüz "harcama tahmini" yapılmamış (Null) 3 yeni müşteri ekleyecek.
3. Ders 11'de ürettiğimiz `egitilmis_model.joblib` beynini hafızaya yükleyecek.
4. Bu 3 kişinin yaş ve sürelerine bakıp tahminde bulunacak.
5. SQL'de `UPDATE` işlemi yaparak o boş sütunları dolduracak ve veritabanının son halini ekrana basacak.

---

### 💡 Ekstra İpucu: Veritabanını Görsel Olarak İncelemek (DBeaver)
Python koduyla veritabanına veri yazdık ve okuduk. Peki ya bu tabloyu kendi gözlerimizle, bir Excel dosyası gibi görsel bir arayüzde görmek istersek?

Bunun için sektörde standart haline gelmiş **DBeaver** uygulamasını kullanmanızı şiddetle tavsiye ederim. DBeaver ücretsiz ve evrensel bir veritabanı aracıdır. Sadece PostgreSQL değil; MySQL, Microsoft SQL Server, Oracle, MariaDB, SQLite ve daha adını bile duymadığınız onlarca veritabanını tek bir ekrandan görsel olarak yönetmenizi sağlar.

**Nasıl Bağlanılır?**
1. İnternetten **DBeaver** uygulamasını indirip kurun.
2. Uygulamayı açıp "Yeni Bağlantı (New Connection)" butonuna tıklayın ve **PostgreSQL**'i seçin.
3. Bizim Docker'da ayağa kaldırdığımız veritabanına girmek için şu ayarları doldurun:
   - **Host:** `localhost` *(Kendi bilgisayarımızda çalıştığı için)*
   - **Port:** `5432`
   - **Database:** `veri_bilimi_db`
   - **Username:** `admin`
   - **Password:** `gizlisifre`

Bağlan dediğinizde, sol menüden tabloları genişletip `musteriler` tablosuna çift tıklayarak Python'un ürettiği o tahminlerin SQL tablomuza nasıl şık bir şekilde oturduğunu görebilirsiniz!
