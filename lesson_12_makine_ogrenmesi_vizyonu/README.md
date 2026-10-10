# Ders 12: Gerçek Hayatta Makine Öğrenmesi (Bir Veri Bilimcinin Vizyonu)

> [!CAUTION]
> **DİKKATLE OKUNMALI:** Bir sonraki koda geçmeden önce bu dokümanı mutlaka okuyun! Buradaki bakış açısını anlamak, "sadece kod yazan biri" ile "gerçek bir veri bilimci" arasındaki farkı belirler.

Bir önceki derste (Ders 11) bir model eğittik ve **%99.46** gibi devasa bir başarı (R² Skoru) elde ettik. Yapay zeka bize çok ufak bir yanılma payıyla harika tahminler sundu. Ancak gerçek dünya, bizim hazırladığımız bu 40 satırlık veri seti kadar kusursuz ve pembe değildir! 

İleride dâhil olacağınız büyük projelerde, piyasadaki gerçek sorunları çözerken karşılaşacağınız acı ama bir o kadar da öğretici gerçekler şunlardır:

### 1. %99 Başarı Oranı Gerçek Hayatta Bir "Uyarı" İşaretidir! (Overfitting)
Gerçek insan davranışları (harcamalar, satın almalar, tıklamalar) hiçbir zaman `(Yaş * 4) + (Dakika * 8) = Harcama` gibi pürüzsüz ve kesin bir matematiksel formüle oturmaz. İnsan doğası kaotiktir. 
Gerçek projelerde **%75 - %85** arası bir başarı oranı çoğu zaman "Çok başarılı" kabul edilir. Eğer modeliniz %99 başarılı çıkıyorsa sevinmek yerine şüphelenmelisiniz. Çünkü modeliniz büyük ihtimalle veriyi "öğrenmemiş", **"ezberlemiştir" (Buna Overfitting - Aşırı Öğrenme denir).** 
- **Ezberleyen Model (Overfitting):** Eğitim verisini (Geçmişi) bir sözlük gibi ezberler. Sınavda (Test aşamasında) veya canlıya alındığında daha önce HİÇ görmediği yepyeni bir durumla karşılaşınca tamamen çuvallar ve yanlış karar verir.
- **Gerçekten Öğrenen Model:** Genel mantığı ve gidişatı anlar. Verideki birebir aynı rakamı tutturamasa bile (az önceki 15 TL'lik yanılma payı gibi), hiç bilmediği bir durumda bile mantıklı ve güvenli bir limanda kalır.

### 2. "Linear Regression" Her Derde Deva Değildir (Yanlış Model Seçimi)
Bizim senaryomuzda "Yaş ve sitede kalma süresi arttıkça, harcama da dümdüz bir şekilde artar" gibi basit (doğrusal) bir mantık kurduğumuz için `LinearRegression` algoritması bunu şıp diye çözdü. 
Fakat gerçek hayatta işler karışıktır. Örneğin; yaş 20'den 40'a çıkarken harcama artıyor, ama 40'tan 60'a giderken emeklilikten dolayı tekrar düşüyorsa (eğrisel/dalgalı bir ilişki varsa), `LinearRegression` bu mantığı ASLA anlayamaz ve hata payı devasa olur. Böyle durumlarda **Decision Trees (Karar Ağaçları), Random Forest veya XGBoost** gibi çok daha zeki, karmaşık kuralları anlayabilen algoritmalar seçmek zorunda kalırız. Doğru veriye doğru modeli seçmek işin kalbidir.

### 3. Kirli Veri (Dirty Data) Gerçeği
Bizim kullandığımız veri tertemizdi. Sadece bir iki satırda yaş eksikti, onu da hemen ortalamayla doldurduk. Şirketlerdeki dev veritabanları ise tam bir kaostur:
- Müşteri yaşı yerine sisteme yanlışlıkla "Asdasd" yazılmış olabilir.
- Harcama tutarı "-5000 TL" gibi imkansız bir eksi değere sahip olabilir.
- Aynı kişinin ismi bir tabloda "Ahmet", diğer tabloda "Ahmt" diye geçebilir.

> [!IMPORTANT]
> **Altın Kural:** Bir veri bilimcinin mesaisinin %80'i yapay zeka modeli eğitmek değil, bu devasa ve kirli veriyi temizlemek, düzenlemek ve mantıklı hale getirmektir. Sisteme çöp veri girerse, yapay zekadan çöp tahmin çıkar. *(Garbage in, garbage out).*

### Özetle;
Makine öğrenmesi bir sihir değildir; tamamen içine koyduğunuz verinin kalitesine, temizliğine ve seçtiğiniz algoritmanın verinin doğasına uygun olup olmamasına bağlı bir istatistik motorudur. 

Bu vizyonu ve dikkat edilmesi gerekenleri aklımızın bir köşesine yazdıysak, şimdi o temizlediğimiz ve yapay zekadan geçirdiğimiz tahminleri **gerçek bir sisteme (Backend/PostgreSQL)** bağlamak üzere **Ders 13'e** geçebiliriz!
