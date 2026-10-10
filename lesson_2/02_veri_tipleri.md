# Ders 2: Veri Tipleri (Sayısal ve Kategorik Veriler)

Verileri doğru analiz edebilmek için, sütunlarda (değişkenlerde) ne tür veriler tuttuğumuzu bilmeliyiz. Veri biliminde temelde iki ana veri tipi ile sıkça karşılaşırız:

1. **Sayısal (Numerical) Veri:** Matematiksel işlemler (toplama, ortalama alma vb.) yapılabilen, miktar veya ölçü belirten sayılardır.
2. **Kategorik (Categorical) Veri:** İsimleri, etiketleri, türleri veya grupları ifade eder. Üzerinde matematiksel işlemler yapılamaz.

### Örnek Tablo: Müşteri Profilleri
Aşağıdaki öğrenme amaçlı temsili tabloyu inceleyelim:

| Müşteri No | Yaş | Cinsiyet | Eğitim Durumu | Boy (cm) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 28 | Kadın | Üniversite | 165 |
| 2 | 35 | Erkek | Lise | 178 |
| 3 | 22 | Kadın | Yüksek Lisans | 170 |

**Soru 1:** Sence bu tablodaki sütunlardan hangileri "Sayısal", hangileri "Kategorik" veridir? Nedenleriyle birlikte kısaca açıklar mısın?

**Cevap 1:** 
- **Yaş ve Boy (cm):** Sayısal (Numerical) verilerdir. Yaşların ortalamasını alabilir veya boyları toplayıp çıkarabiliriz, bunlar bize matematiksel olarak anlamlı sonuçlar verir.
- **Cinsiyet ve Eğitim Durumu:** Kategorik (Categorical) verilerdir. Matematiksel bir işleme tabi tutulamazlar, sadece grupları veya sınıfları (kadın/erkek, lise/üniversite vb.) ifade ederler.

**Peki ya "Müşteri No"?**
Müşteri numaraları (ID'ler) tabloya bakıldığında "1, 2, 3" gibi sayılardan oluştuğu için ilk bakışta sayısal veri (numerical) gibi görünür.

**Soru 2:** İki farklı müşterinin "Müşteri No"sunu toplamak (örneğin 1 + 2 = 3) veya bunların ortalamasını almak veri analizi açısından anlamlı bir sonuç verir mi? Bu durumda Müşteri No, "Sayısal" veri tanımımıza tam olarak uyuyor mu?

**Cevap 2:** Hayır, anlamlı bir sonuç vermez. İki farklı müşterinin ID'sini toplamak (1+2 = 3) bize "3 numaralı müşteri" hakkında veya müşterilerin genel bir "ortalaması" hakkında hiçbir matematiksel gerçek sunmaz. 
Bu yüzden Müşteri No, TC Kimlik No, Telefon Numarası veya Posta Kodu gibi sayılardan oluşan veriler **Kategorik (veya Tanımlayıcı - Identifier)** veri olarak kabul edilir. Sırf rakamlardan oluşmaları onları matematiksel "Sayısal" veri yapmaz.

