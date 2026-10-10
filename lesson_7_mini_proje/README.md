# Ders 7: Mini Proje (Gerçek Bir Veri Senaryosu)

Şu an gerçek bir projenin taslağındayız. İlk 6 derste öğrenilen tüm temel taşları (veri tipleri, eksik veri mantığı, veriyi okuma, filtreleme, gruplama ve anlam çıkarma) gerçekçi bir senaryoda uyguluyoruz.

Bir e-ticaret şirketinde Veri Bilimci olarak analiz yaptığımızı düşünelim. Yöneticimiz `satis_verileri.csv` dosyasını gönderdi ve bazı analizler yapmamızı istedi.

Veri setinde 5 sütun bulunuyor:
- **Siparis_ID** (Sipariş Numarası)
- **Musteri_Yas** (Müşterinin Yaşı)
- **Sehir** (Müşterinin Şehri)
- **Kategori** (Satın Alınan Ürün Kategorisi)
- **Satis_Miktari** (Harcama Tutarı - TL)

Bu klasördeki `proje.py` dosyası, aşağıda istenen analizlerin nasıl kodlandığını göstermektedir.

---

### Yöneticinin Talepleri ve Çözümler

**Görev 1 (Gözlem ve Eksik Veri):** 
Müşterilerimizin yaş ortalaması sorulduğunda, `satis_verileri.csv` dosyasına bakarsak bazı müşterilerin (örneğin 1003 ve 1009 ID'li müşteriler) yaş bilgisinin boş olduğunu görürüz. Eksik veriler (Null/NaN) nedeniyle yaş ortalamasını direkt hesaplamak istatistiksel sapmalara yol açar. Bu yüzden önce veri temizliği (silme veya doldurma) yapılmalıdır.
*Çözüm Kodu (Eksik veriyi ortalama ile doldurmak):*
```python
ortalama_yas = df["Musteri_Yas"].mean()
df["Musteri_Yas"] = df["Musteri_Yas"].fillna(ortalama_yas)
```
*(Normalde eksik veriye sahip satırları tamamen silebilirdik. Ancak veri sayımız az olduğu için ve o satırları silersek o müşterilerin "Şehir" ve "Satış Miktarı" gibi diğer değerli bilgilerini de çöpe atacağımız için, ortalama ile doldurmayı tercih ettik. Eksik hücreleri sütunun ortalamasıyla doldurmak, o sütunun genel ortalamasını bozmaz; böylece zarar vermeden veriyi kurtarmış oluruz.)*

**Görev 2 (Veriyi Okumak):** 
Verinin Pandas kütüphanesi ile okunması ve ilk 5 satırının görüntülenmesi işlemi:
```python
import pandas as pd
df = pd.read_csv("satis_verileri.csv")
print(df.head())
```

**Görev 3 (Filtreleme):** 
Sadece "Elektronik" kategorisinde yapılan satışları listelemek:
```python
elektronik_satislar = df[ df["Kategori"] == "Elektronik" ]
print(elektronik_satislar)
```

**Görev 4 (Gruplama - Group By):** 
Şehirlere göre toplam harcama tutarlarını bulmak:
```python
sehir_toplamlari = df.groupby("Sehir")["Satis_Miktari"].sum()
print(sehir_toplamlari)
```

**Görev 5 (Anlam Çıkarma):**
Görev 4'ten çıkan sonuca göre (Ankara: 9200, İstanbul: 5870, İzmir: 5210 TL), reklam bütçesinin en büyük kısmı **Ankara'ya** ayrılmalıdır. Çünkü mevcut verilere göre açık ara en çok geliri Ankara'daki müşteriler sağlamaktadır. Pazarlama yatırımlarının en çok dönüş getiren veya potansiyeli yüksek alana yapılması ticari olarak en mantıklı adımdır.
