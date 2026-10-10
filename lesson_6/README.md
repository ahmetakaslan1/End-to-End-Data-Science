# Ders 6: Veriyi Özetlemek (Group By)

Analiz yaparken genellikle satır satır verilerden ziyade, büyük resmi görmek isteriz. "Hangi şehir toplamda ne kadar harcama yapmış?" veya "Şehirlerin yaş ortalaması nedir?" gibi soruların cevabını SQL'de `GROUP BY` komutuyla buluruz. Pandas kütüphanesinde de tam olarak aynı işlevi gören `groupby()` fonksiyonunu kullanırız.

Bu klasörde yer alan dosyalar:
1. `musteriler.csv`: Örnek veri setimiz.
2. `veri_grupla.py`: Gruplama (aggregation) işlemini gösteren örnek Python kodu.

### Görev
Lütfen `veri_grupla.py` dosyasını çalıştırıp çıktısını inceleyin.
Koddaki şu bölüme dikkat edelim:
`df.groupby("Sehir")["Harcama_TL"].sum()`

**Soru:** Eğer yöneticiniz sizden "Şehirlere göre *toplam harcamayı* değil de, şehirlere göre *yaş ortalamasını*" bulmanızı isteseydi, kodun bu satırını nasıl değiştirirdiniz?

**Cevap:**
Kod şu şekilde değiştirilirdi: `df.groupby("Sehir")["Yas"].mean()`

**Açıklama:**
* **`groupby("Sehir")`**: Veriyi şehirlere göre gruplar (İstanbul'dakiler bir araya, Ankara'dakiler bir araya).
* **`["Yas"]`**: Analiz edilecek sütun olarak "Harcama_TL" yerine "Yas" seçilir.
* **`.mean()`**: Pandas'ta aritmetik ortalama (average) almak için kullanılan fonksiyondur. (Toplam bulmak için `.sum()`, adet bulmak için `.count()`, ortalama için `.mean()` kullanılır). Toplamı adede bölmek de (sum/count) aynı matematiksel sonucu verecektir.
