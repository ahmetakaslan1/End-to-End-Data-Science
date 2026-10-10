# Ders 10: Veri Görselleştirme (Sayıları Şekillere Dönüştürmek)

Sayılarla dolu bir tabloyu veya terminal çıktısını incelemek, özellikle veri seti büyüdüğünde çok zorlaşır. İnsan beyni görsel örüntüleri (paternleri) ve oranları sayılardan çok daha hızlı algılar. Bu yüzden veriyi grupladıktan veya özetledikten sonraki ilk işimiz onu **görselleştirmektir**.

Python'da veri görselleştirmek için en yaygın kullanılan temel kütüphane **Matplotlib**'dir. Pandas kütüphanesi de arka planda bu aracı kullanarak bize tek satırda grafik çizme imkanı sunar.

Bu klasörde yer alan dosyalar:
1. `satis_verileri.csv`: Önceki projeden tanıdığımız veri seti.
2. `grafik_ciz.py`: Şehirlere göre satış toplamlarını alıp bunu bir Çubuk (Bar) grafiğe döken kodumuz.

### Görev
1. Öncelikle `grafik_ciz.py` dosyasını terminalden çalıştırın. (Eğer `No module named 'matplotlib'` gibi bir hata alırsanız, terminale `pip install matplotlib` yazarak bu kütüphaneyi kurabilirsiniz).
2. Kod çalıştıktan sonra ekranda açılan grafik penceresini inceleyin. Hangi çubuğun en yüksek olduğuna (Ankara) sadece saniyenin onda biri sürede karar verebildiğinizi fark edin!
3. Koda geri dönüp `sehir_toplamlari.plot(kind="bar")` satırını bulun.

**Soru:** Eğer yöneticiniz sizden çubuk (bar) grafik değil de **Pasta (Pie) Grafik** isteseydi, mantıksal olarak koddaki o `kind="bar"` kısmını ne olarak değiştirirdiniz? (Sadece mantıksal ve İngilizce tahmininizi yapmanız yeterlidir).
