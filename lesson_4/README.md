# Ders 4: Python ve Pandas'a Giriş

Gerçek dünya verileri genellikle Excel veya CSV (virgülle ayrılmış değerler) dosyalarında saklanır. Bu verileri okumak, temizlemek ve incelemek için Python'da en çok kullandığımız araç **Pandas** kütüphanesidir.

Bu klasörde senin için iki dosya hazırladım:
1. `musteriler.csv`: Gerçek bir veri setinin çok küçük bir simülasyonu. İçinde 4 müşterinin bilgisi var.
2. `veri_oku.py`: Bu CSV dosyasını Python ile okumamızı sağlayan çok kısa bir kod parçası.

### İlk Görev
Lütfen önce `veri_oku.py` dosyasını açıp içindeki 3 satırlık koda göz at. Kodun içindeki `pd.read_csv()` ve `df.head()` sence tam olarak ne işe yarıyor olabilir? (Kodu çalıştırmadan önce sadece bir yazılımcı olarak mantığını tahmin etmeni istiyorum).

**Cevap 1:**
Bu kod, CSV dosyasındaki verileri "Müşteri ID", "Yaş", "Şehir" gibi başlıkları sütun, altındaki verileri de satır satır olacak şekilde çok güzel bir tablo formatında okumamızı sağlıyor. `head()` fonksiyonu ise tablonun sadece ilk birkaç satırını (belirli bir sınırı olmalı) bize gösteriyor.

**Açıklama:**
- `pd.read_csv()`: O virgüllerle ayrılmış metin dosyasını alır, satırların ve sütunların olduğu düzenli bir tabloya çevirir. Pandas'ta bu tablo yapısına **DataFrame (df)** diyoruz.
- `df.head()`: Gerçek veri setleri milyonlarca satır olabilir. Hepsini ekrana yazdırmak bilgisayarı dondurur. Bu yüzden sadece verinin "kafasına" (ilk 5 satırına) bakarak tablonun neye benzediğini, doğru okuyup okuyamadığımızı anlarız. (Varsayılan olarak 5 satır getirir, bizim tablomuz zaten 4 satır olduğu için hepsini gösterdi).
