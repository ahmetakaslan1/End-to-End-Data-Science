# Ders 8: Kategorik Verilerde Eksik Hücreleri Doldurmak

"Peki ya eksik olan hücre yaş (sayısal) değil de, şehir veya kategori (kategorik) olsaydı? Kelimelerin ortalamasını alamayız, bu durumda boş hücreyi neyle dolduracağız?"

Kategorik verilerde eksik hücreleri doldurmak için veri biliminde en sık kullanılan iki ana yöntem vardır:

1. **Mod (En Çok Tekrar Eden Değer) İle Doldurmak:** Sayısal verilerde ortalama (mean) alıyorsak, kategorik verilerde de en popüler değere, yani **Mod (Mode)** değerine bakarız. Eğer veritabanımızdaki müşterilerin büyük çoğunluğu İstanbul'dansa, sisteme şehri girilmemiş (boş) olan birinin de İstanbul'dan olma ihtimali istatistiksel olarak en yüksektir. Bu yüzden o boşluğu Mod değeriyle (örn: "Istanbul") doldururuz.
2. **"Bilinmiyor" veya "Diğer" Olarak Etiketlemek:** Eğer en çok tekrar eden değerle doldurmak veriyi bozacaksa (örneğin şehirlerin dağılımı birbirine çok yakınsa), boş hücreleri silmek yerine oraya `"Bilinmiyor"` metnini yazar geçeriz. Böylece satırı silmeden veri kaybını önleriz.

Bu klasörde yer alan dosyalar:
1. `kategorik_veri.csv`: "Sehir" sütununda eksik veriler (virgüller arası boşluklar) olan küçük bir tablo.
2. `kategorik_doldur.py`: Eksik kategorik verileri, en çok tekrar eden değer (Mod) ile dolduran örnek kod.

### Görev
Lütfen `kategorik_doldur.py` dosyasını çalıştırın ve Pandas'ın `mode()` fonksiyonu sayesinde "kelimelerin ortalaması" yerine "en popüler kelimeyi" bularak boşlukları nasıl mantıklı bir şekilde doldurduğunu inceleyin.
