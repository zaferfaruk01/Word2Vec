#Veri İşlemleri İçin
import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize,regexp_tokenize
from nltk.corpus import stopwords
import re
import nltk

#Veri Çekme İşlemleri İçin
import requests
from bs4 import BeautifulSoup
from IPython.display import clear_output

#GENEL TANIMLAMALAR
site =requests.get("https://sondakika.haberler.com")
jobs = site.content
soup = BeautifulSoup(jobs,"html.parser")

all_jobs =soup.find_all("div",{"class":"hblnContent"})
all_jobs2 =soup.find_all("a",{"class":"hblnTitle"})
    

urls = []
sonuclist = []

#HABER İÇERİĞİ ALININA FONKSİYON

def haber_icerigi_al(haber_url):
    haber_site =requests.get(haber_url)
    jobs = haber_site.content
    soup = BeautifulSoup(jobs,"html.parser")

    #Div etiketinin altındaki p etiketleri bulur
    icerik = soup.findAll("div", class_="hbptContent haber_metni")[0].findAll('p')
    
    ana_icerik = ""
    #Her p etiketini tek bir yerde toplama işlemi.
    for i in range(len(icerik)):
        ana_icerik += icerik[i].get_text()
    
    #VERİ TEMİZLEME
    ana_icerik_stopwords = ""
    stop_words = stopwords.words('turkish')
    for w in word_tokenize(ana_icerik):
        if w not in stop_words:            
            ana_icerik_stopwords += (" "+w)
    
    
    sentences = nltk.sent_tokenize(ana_icerik_stopwords)
    
    cleaned_sentences = []
    for sent in range(len(sentences)):
    
        text = sentences[sent]
        text = re.sub("\W+"," ",text)    
        text = re.sub("[0-9]+"," ",text)
        text = re.sub("\s\w\s", " ", text)
        text = re.sub("^\s", "", text)
        text = re.sub("\s$", "", text)
        text = re.sub("\s+"," ",text)
       
        text = text.strip()

        cleaned_sentences.append(text)
        
    return cleaned_sentences

#url,segment_no,kelime_sayısı ve haber içeriği alınıyor.

for job in all_jobs:   
    
    a_href = job.find_all('a', href=True)
    a_href_list = list(a_href)
    
    for a in a_href_list:
        urls.append(a['href'])
        temp=haber_icerigi_al(a['href'])
        for sent in temp:
            kelime_sayısı = len(word_tokenize(sent))
            sonuclist.append((a['href'],temp.index(sent),sent,kelime_sayısı))
        
#DATA SET OLUŞTURMA (CSV) KISMI

urldata = pd.DataFrame(sonuclist)
urldata.columns = ["url","segment_no","cumle_icerigi","kelime_sayısı"]
urldata.head()
urldata.to_csv('urldata2.csv')

