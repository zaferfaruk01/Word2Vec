# Word2Vec
Train a gensim word2vec model on news data.

# Creating a Word2Vec model using the news corpus and Gensim library I created

## Creating a corpus

The creating corpus process is located in the file named ** web scraping .by **.
 
[What is web scraping? ]( https://github.com/zaferfaruk01/web-scraping-).

- In order to create a corpus using the current Turkish news texts on "https://sondakika.haberler.com" , we will only get the main text of the news with Web scraping.
- We take the necessary process for cleaning or correction in the text content of the page.
- We divide each news text on a sentence basis.(sentence segmentation,You can use nltk or another library)
- The names and order of the fields in the corpus file are as follows:
  1.	url: The full address of the page from which the news text was received.
  2.	segment_no: What segment is the sentence
  3.	cumle_icerigi: Text content of the sentence
  4.	sözcük_sayisi: Number of words in the sentence

## Create a Word2Vec model

- We created the Word2Vec model using the ** url data2.csv ** news corpus we created and then Gensim library.
- I made similarity measurements on this model.
-	The queries I use for similarity measurements and the results we get:

###### Queries

```python
#kelimeler listesiki veriler ile benzerlik ölçümü yapılıyor.
kelimeler= ["dolar","covid","ceza","insan","ülke"]
for k in kelimeler:

    temp=k
    benzerlik_sonucu_yazdir(temp)
    print("\n**********************************\n")
    #print(type(k))
    
```
###### Results

dolar kelimesi için benzerlik ölçümü: 
<br>
('Sağlık', 0.9997574090957642)
<br>
('nde', 0.9997353553771973)
<br>
('güvenlik', 0.9997352957725525)
<br>
('ardından', 0.9997302889823914)
<br>
('dedi', 0.9997203946113586)
<br>
**********************************

covid kelimesi için sonuç bulunamadı!
<br>

**********************************

ceza kelimesi için sonuç bulunamadı!
<br>

**********************************

insan kelimesi için benzerlik ölçümü: 
<br>
('Türkiye', 0.9994175434112549)
<br>
('sıradaki', 0.9994075298309326)
<br>
('un', 0.999382734298706)
<br>
('bulunan', 0.9993813633918762)
<br>
('çıkan', 0.9993777871131897)
<br>
**********************************

ülke kelimesi için benzerlik ölçümü:
<br>
('aldığı', 0.9985852241516113)
<br>
('Günü', 0.9985677003860474)
<br>
('eden', 0.9985652565956116)
<br>
('belirterek', 0.9985647201538086)
<br>
('yasağı', 0.9985615015029907)
<br>
**********************************

17287

