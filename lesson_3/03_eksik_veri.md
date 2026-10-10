# Ders 3: Eksik Veri (Missing Data)

Gerçek dünyada topladığımız veriler neredeyse hiçbir zaman kusursuz veya eksiksiz değildir. Bazen sistemsel bir hata, bazen müşterinin bir alanı doldurmak istememesi nedeniyle tablomuzdaki bazı hücreler boş kalır. Veri biliminde bu boş hücrelere **Eksik Veri (Missing Data / Null / NaN)** denir.

Eksik veriler, veri analizindeki en büyük baş ağrılarından biridir çünkü hesaplamalarımızı doğrudan etkiler.

### Örnek Tablo: Müşteri Yaşları
Aşağıdaki temsili tabloda, bir sisteme üye olan üç kişinin bilgileri yer almaktadır:

| Müşteri No | Yaş | Üyelik Tipi |
| :--- | :--- | :--- |
| 1 | 25 | Premium |
| 2 | ? (Boş) | Standart |
| 3 | 41 | Premium |

*(Not: 2 numaralı müşterinin yaşı sistemde bilinmemektedir, o hücre boştur.)*

**Soru 1:** Patronunuz sizden bu platformdaki müşterilerin "Yaş Ortalamasını" bulmanızı istedi. Tablodaki bu eksik veri (boş hücre) varken yaş ortalamasını hesaplamaya çalışırsak sence nasıl bir mantıksal veya matematiksel sorunla karşılaşırız? 

**Cevap 1:**
Eksik veri, hesaplamalarımızı doğrudan yanıltır ve istatistiksel bir belirsizlik yaratır.
Eğer sadece yaşı bilinen 2 kişinin ortalamasını alırsak (25 + 41) / 2 = 33 buluruz. Ancak sistemde 3 kişi vardır. Yaşı bilinmeyen müşteri 90 yaşındaysa gerçek ortalama 52'ye çıkar; 10 yaşındaysa 25'e düşer.
Sonuç olarak: Eksik veriler varken "Müşteri kitlemizin yaş ortalaması nedir?" gibi sorulara doğru ve güvenilir yanıtlar veremeyiz. Analizimiz eksik veya yanlış sonuçlar doğurur.

---

### Eksik Veriyle Nasıl Başa Çıkılır?
Veri biliminde eksik verilerle karşılaştığımızda genellikle şu iki yoldan birini seçeriz:
1. **Silmek (Drop):** Eksik veriye sahip satırı tamamen veri setinden çıkarmak. (Eğer veri setimiz çok büyükse ve eksik veri sayısı azsa tercih edilir).
2. **Doldurmak (Imputation):** Boş hücreyi mantıklı bir tahminle doldurmak. (Örneğin, bilinen diğer müşterilerin yaş ortalamasını alıp boş hücreye yazmak).

