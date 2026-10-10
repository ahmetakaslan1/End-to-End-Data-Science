# Ders 5: Veriye Soru Sormak (Filtreleme)

Veriyi okumak sadece başlangıçtır; asıl mesele verinin içinden istenilen bilgi kümesini çekip almaktır. SQL'deki `SELECT * FROM Tablo WHERE Sehir = 'Istanbul'` mantığı, Pandas kütüphanesinde filtreleme (filtering) işlemleriyle yapılır. Sözdizimi (syntax) farklı olsa da temel mantık aynıdır.

Bu klasörde yer alan dosyalar:
1. `musteriler.csv`: Filtreleme işlemlerini uygulamak için kullanılan örnek veri seti.
2. `veri_filtrele.py`: Pandas ile filtreleme işleminin nasıl yapılacağını gösteren örnek Python kodu.

### Görev
`veri_filtrele.py` dosyasını çalıştırıp çıktıyı inceledikten sonra, koddaki şu ifadenin mantığını anlamaya çalışalım:
`df[ df["Sehir"] == "Istanbul" ]`

**Soru:** Burada neden iki kere `df` kelimesi kullanılmıştır? Dışarıdaki köşeli parantezin içindeki `df` ile, içerideki `df["Sehir"]` kısmının farkı ve görevi nedir?

### Filtreleme İşleminin Mantığı (Neden iki defa df?)

`df[ df["Sehir"] == "Istanbul" ]` ifadesi, SQL'deki `SELECT * FROM tablo WHERE Sehir = 'Istanbul'` sorgusunun Pandas'taki karşılığıdır. İşlem sırası içten dışa doğru gerçekleşir:

1. **İç Kısım (`df["Sehir"] == "Istanbul"`):** Pandas önce tablonun "Sehir" sütununa bakar ve her bir satır için bu şartın sağlanıp sağlanmadığını kontrol eder. Sonuç olarak `[True, False, False, True, True, False]` gibi bir **Doğru/Yanlış (Boolean) listesi** üretir.
2. **Dış Kısım (`df[ ... ]`):** Dıştaki `df` yapısı, içeriden gelen bu Doğru/Yanlış listesini filtre olarak kullanır. Sadece `True` (Doğru) olan satırları tutar ve bunları yeniden bir **DataFrame (Tablo)** olarak bize döndürür. 

Bu yapı sayesinde, filtrelenen veriler de her zaman üzerinde işlem yapılabilir bir tablo (DataFrame) formatında kalmış olur.
