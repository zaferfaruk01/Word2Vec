import gensim

import pandas as pd
from nltk.tokenize import word_tokenize

#DATA SET OKUMA (CSV) KISMI

df = pd.read_csv("urldata2.csv")

all_words = []
for sent in df["cumle_icerigi"]:
    all_words.append(word_tokenize(str(sent)))    

#all_words veri kümesinden 200 kelime vektörü boyutunda,
#mevcut ve tahmin edilen kelime arasındaki maksimum mesafe 10
#2 den daha düşük frekanstaki kelimeler yok sayılır.
#Skip-gram yönetemi ile eğitildiği için 1 değeri kullanılır.(CBOW=0)

model = gensim.models.Word2Vec(all_words, size=200, window=10, min_count=2, workers=10, sg=1)

#Verilen kelime ile benzerlik sonucunu bularak ekrana yazdıran fonksiyon.

def benzerlik_sonucu_yazdir(word):
    
    try:
        result_list = model.most_similar(word, topn=5)
        print("{} {}" .format(word, "kelimesi için benzerlik ölçümü: \n"))
        for i in result_list:
            print(i)
    except:
        print("{} {}" .format(word, "kelimesi için sonuç bulunamadı!"))

#kelimeler listesiki veriler ile benzerlik ölçümü yapılıyor.
kelimeler= ["dolar","covid","ceza","insan","ülke"]
for k in kelimeler:

    temp=k
    benzerlik_sonucu_yazdir(temp)
    print("\n**********************************\n")
    #print(type(k))
    

#Toplam Kelime Sayısının Hesaplanması.
bos_list=[]
liste = df['kelime_sayısı']

sum = 0
for i in liste:
    sum += int(i)

print(sum)















