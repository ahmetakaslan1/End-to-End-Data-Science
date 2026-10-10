# Ders 11: Makine Öğrenmesine İlk Adım (Yapay Zeka ile Tahmin)

Veriyi Pandas ile okumayı ve temizlemeyi harika bir şekilde öğrendin. Artık o tertemiz veriyi bir "beyne" (algoritmaya) verip ona bir şeyler öğretme vakti geldi.

Makine öğrenmesinde (Machine Learning - ML) temel mantık şudur: Algoritmaya geçmiş verileri verirsin, o bu verilerdeki gizli matematiksel örüntüleri öğrenir ve yeni bir durumla karşılaştığında ne olacağını **tahmin eder**. Bunun için Python'da **Scikit-Learn (sklearn)** kütüphanesini kullanırız.

### Veriyi Eğitmek (Basit Yöntem)
Veriyi ikiye ayırırız:
- **X (Özellikler):** İpuçları (Örn: Yaş, Sitede Geçirilen Süre).
- **y (Hedef):** Tahmin edeceğimiz sonuç (Örn: Harcama).
Ancak modeli eğitip direkt "şu kişiyi tahmin et" dediğimizde, bir mühendis olarak haklı bir şüpheye düşeriz: *"Bana bir sayı verdi ama ben buna inanmalı mıyım? Gerçekten doğru öğrendiğini nasıl bileceğim?"*

### Gerçek Senaryo: Modeli Sınava Sokmak (Train-Test Split)
Modelin ne kadar iyi öğrendiğini test etmek için verimizi %80 (Eğitim) ve %20 (Test) olarak ikiye böleriz:
1. **Eğitim (Train):** %80'lik kısmı modele veririz. Sadece bunlara çalışıp öğrenir.
2. **Test:** Kalan %20'lik kısmı modelden **saklarız**. Model eğitimi bitirdikten sonra, hiç görmediği bu %20'lik verinin özelliklerini (X) verip "Hadi bunların ne kadar harcayacağını tahmin et" deriz.
3. Biz zaten o %20'lik verinin gerçek cevaplarını (y) biliyoruz! Modelin verdiği tahminleri, gerçek cevaplarla kıyaslarız.

**Başarı Metriği (MAE):** Tahminler ile gerçekler arasındaki farka bakarız. Örneğin MAE (Mean Absolute Error) metriği bize şunu söyler: *"Senin modelin her tahmininde ortalama şu kadar TL yanılıyor."*

**Yüzdelik Başarı Oranı (R² Score):** Hata payını TL veya adet cinsinden bilmek iyidir ama "Model % kaç başarılı?" sorusunun cevabını vermek de yöneticiler için bir o kadar önemlidir. Regresyon (Tahmin) modellerinde bu başarı yüzdesi **R² Score (R-Kare Skoru)** ile hesaplanır ve `sklearn.metrics.r2_score` kütüphanesi kullanılarak elde edilir.

Bu klasörde:
1. `ml_verisi.csv`: İçinde 40 müşterinin matematiksel mantığa oturtulmuş daha gerçekçi verisi olan dosya.
2. `ilk_model.py`: Hem basit tahminin yapıldığı hem de sonrasında **Eğitim/Test** ayırımının yapılarak modelin başarı oranının (hata payının) ölçüldüğü gerçekçi Python kodu.

### Görev
1. Terminalden `ilk_model.py` dosyasını çalıştırın.
2. Ekrana basılan "Tahminler vs Gerçekler" kısmını incele. Model, gerçekte 340 TL harcayan birini tahminen ne kadar harcar diye bulmuş?
3. En alttaki Ortalama Hata Payına bakarak, modelimizin ne kadar güvenilir olduğunu değerlendir.

---

### ⚠️ Önemli Not: Hangi Metriği Ne Zaman Kullanırız? (R² vs Diğerleri)
"Neden başarıyı ölçmek için R² Score veya MAE kullandık? Her zaman bunları mı kullanacağız?" 
**Hayır.** Makine öğrenmesinde *neyi tahmin ettiğine göre* kullanacağın başarı cetveli değişir:

1. **Regresyon (Sayısal Tahmin):** Eğer tahmin etmeye çalıştığın şey **sayısal bir değerse** (Örn: Kaç TL harcar? Evin fiyatı nedir? Kaç yaşında?), buna *Regresyon* denir. Sayısal farkları (hataları) ölçmek için **MAE, MSE veya R² Score** kullanmak *zorundayız*. Şu anki projemizde Harcama (TL) tahmin ettiğimiz için R² kullandık.
2. **Sınıflandırma (Kategorik Tahmin):** Eğer tahmin etmeye çalıştığın şey **kategorik bir değerse** (Örn: Bu mail Spam mi değil mi? Bu müşteri ürünü alır mı almaz mı? Hangi kategoriyi sever?), buna *Sınıflandırma (Classification)* denir. Sınıflandırmada hata payı hesaplanmaz, "Kaç soruya doğru cevap verdin?" mantığıyla **Accuracy (Doğruluk Oranı %)** isimli bambaşka metrikler kullanılır.

Bunların çeşitlerini ve Sınıflandırma algoritmalarını ilerleyen derslerde çok daha net göreceğiz!

### Modeli Kaydetmek (Export) ve Kendi Tahminini Yapmak
Modeli başarıyla eğittikten (Train) sonra, o öğrenilmiş matematiksel beynin kaybolmasını istemeyiz. Bunun için modeli bir dosyaya kaydederiz (Export). Python'da bu işlem için `joblib` kütüphanesi kullanılır. Modeli `.joblib` uzantılı bir dosya olarak kaydettiğimizde, ileride sadece bu dosyayı okuyup (Import), baştan eğitim (fit) yapmaya gerek duymadan doğrudan `kendi_verim = pd.DataFrame(...)` mantığıyla `.predict()` fonksiyonunu kullanarak yepyeni müşteriler için tahminler yapabiliriz.
