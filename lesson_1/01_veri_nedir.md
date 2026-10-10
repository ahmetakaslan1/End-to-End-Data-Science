# Bizler ders 4 te csv, python ile ilgili veri analizi yapacaz. Ders  Ama şimdiden temelleri atalım.

# Ders 1: Veri Nedir?

Bu dersteki tek hedefimiz: "Veri", "tablo", "satır" ve "sütun" kavramlarını anlamak; bir tablodaki her satırın neyi temsil ettiğini fark etmektir.

Aşağıdaki tablo gerçek bir veri seti değildir, sadece öğrenme amacıyla oluşturulmuş temsili bir örnektir. Bir kafedeki siparişleri göstermektedir:

| Sipariş No | İçecek | Boy | Fiyat (TL) |
| :--- | :--- | :--- | :--- |
| 101 | Filtre Kahve | Büyük | 55 |
| 102 | Çay | Orta | 20 |
| 103 | Latte | Küçük | 65 |
| 104 | Filtre Kahve | Orta | 45 |

**Soru:** Sence bu tablodaki bir satır neyi temsil ediyor?

**Senin Cevabın:** Tabloya bakarak hangi içeceğin ne kadar satıldığını, gün sonunda ne kadar para kazanıldığını görebiliriz. Tablo genel olarak bunları temsil ediyor.


Tablodaki **sadece bir satır** (örneğin 102 numaralı satır), o gün kafeye gelen **tek bir müşterinin verdiği tek bir siparişi (tekil bir olayı)** temsil eder. 
- **Satır (Veri biliminde 'Gözlem' denir):** Gerçekleşen tekil bir işlemi, kişiyi veya nesneyi gösterir. (Bu örnekte: 1 adet sipariş eylemi).
- **Sütun (Veri biliminde 'Değişken' veya 'Özellik' denir):** O olayla/nesneyle ilgili özellikleri (içecek türü, boyu, fiyatı) gösterir.

---

### Yeni Örnek
Aşağıdaki tablo, bir kütüphanedeki bazı kitapları göstermektedir:

| Kitap ID | Kitap Adı | Yazar | Sayfa Sayısı |
| :--- | :--- | :--- | :--- |
| 1 | Şeker Portakalı | J.M. de Vasconcelos | 183 |
| 2 | 1984 | George Orwell | 352 |

**Soru 2:** Bu yeni tabloda **bir satır** neyi temsil etmektedir?



Evet, bu tabloda bir satır **tek bir kitabı** (kütüphanedeki spesifik bir kitabı) temsil ediyor. Sütunlar ise o kitabın özelliklerini (yazarı, sayfa sayısı) veriyor.

---

### Son Kontrol Sorusu
Şimdi bugünün son ve en önemli sorusuna gelelim:

**Soru 3:** Satırın neyi temsil ettiğini bilmeden tablodan sonuç çıkarmak neden tehlikeli olabilir?

**Cevap:** Satırın neyi temsil ettiğini (yani gözlem biriminin ne olduğunu) bilmezsek, veriye doğru soruları soramayız. Tablonun bize ne tür sonuçlar veya anlamlar üretebileceğinin sınırlarını belirleyen şey, bir satırın neyi temsil ettiğidir. Bu temel taşı anlamadan veriyi analiz etmek, tamamen yanlış veya anlamsız sonuçlar doğurur.
