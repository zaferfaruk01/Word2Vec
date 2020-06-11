# Word2Vec
Train a gensim word2vec model on news data.

# Oluşturduğum haber derlemi ve Gensim kütüphanesini kullanarak bir Word2Vec modeli oluşturma.

## Bir derlem (corpus) oluşturma

Derlem oluşturma işlemi **web_scraping .py** adlı dosyada bulunmaktadır.
 
[Web scraping nedir? ]( https://github.com/zaferfaruk01/web-scraping-).

- "https://sondakika.haberler.com" haber sitesinde bulunan güncel türkçe haber metinlerini kullanarak bir derlem (corpus)
oluşturmak için Web scraping işlemi ile yalnızca haberin ana metnini alıcağız.
- Sayfanın metin içeriğinde temizleme ya da düzeltme amaçlı olarak gerekli işlemleri yaparız.
- Her bir haber metnini cümle bazlı olarak bölümleriz.(yani sentence segmentation işlemi uygularız,nltk ya da uygun başka bir kütüphane kullanabilirsiniz)
- Derlem dosyasındaki alan isimleri ve sırası aşağıdaki gibidir:
  1.	url: haber metninin alındığı sayfanın tam adresi
  2.	segment_no: bir metinde yapılan cümle bazlı bölümleme sonunda, ilgili cümlenin kaçıncı segment olduğu
  3.	cumle_icerigi: cümlenin metin içeriği
  4.	sözcük_sayisi: cümlede bulunan sözcük sayısı

## Word2Vec modeli oluşturma

- Oluşturduğumuz **urldata2.csv** haber derlemini ve Gensim kütüphanesini kullanarak Word2Vec modeli oluşturduk.
- Bu model üzerinde benzerlik ölümleri gerçekleştirdim.
-	Benzerlik ölçümleri için kullandığım sorgular ve elde ettiğiniz sonuçlar:

###### Sorgular

```python
#kelimeler listesiki veriler ile benzerlik ölçümü yapılıyor.
kelimeler= ["dolar","covid","ceza","insan","ülke"]
for k in kelimeler:

    temp=k
    benzerlik_sonucu_yazdir(temp)
    print("\n**********************************\n")
    #print(type(k))
    
```
###### Sonuçlar

dolar kelimesi için benzerlik ölçümü: 

('Sağlık', 0.9997574090957642)        
('nde', 0.9997353553771973)
('güvenlik', 0.9997352957725525)
('ardından', 0.9997302889823914)
('dedi', 0.9997203946113586)

**********************************

covid kelimesi için sonuç bulunamadı!

**********************************

ceza kelimesi için sonuç bulunamadı!

**********************************

insan kelimesi için benzerlik ölçümü: 

('Türkiye', 0.9994175434112549)
('sıradaki', 0.9994075298309326)
('un', 0.999382734298706)
('bulunan', 0.9993813633918762)
('çıkan', 0.9993777871131897)

**********************************

ülke kelimesi için benzerlik ölçümü:

('aldığı', 0.9985852241516113)
('Günü', 0.9985677003860474)
('eden', 0.9985652565956116)
('belirterek', 0.9985647201538086)
('yasağı', 0.9985615015029907)

**********************************

17287

