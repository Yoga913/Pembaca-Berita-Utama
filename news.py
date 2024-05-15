# berita teratas dari API NewsAPI dan membacakannya menggunakan pyttsx3, suatu pustaka Python untuk sintesis suara.
import requests # digunakan untuk membuat permintaan HTTP ke API NewsAPI.
import pyttsx3 # digunakan untuk sintesis suara.

url = ('https://newsapi.org/v2/top-headlines?'
       'country=id&'
       'apiKey=f38b26e86acb46c29058439829075408')
# URL yang menentukan endpoint API NewsAPI dan parameter yang diperlukan untuk mendapatkan berita teratas dari Indonesia (`country=id`).

engine = pyttsx3.init('espeak') # mengatur engine untuk menggunakan mesin teks-ke-suara eSpeak.
voices = engine.getProperty('voices') # Mendapatkan daftar suara yang tersedia dari engine pyttsx3.
speed = engine.setProperty("rate", 150) #  Menetapkan kecepatan bicara ke 150 kata per menit.
engine.setProperty('voice','voices[1].id') #  Mengatur suara yang digunakan oleh engine.

def get_news(): # definisi yang mendapatkan dan yang membaca berita
    headlines = [] # 
    response = requests.get(url) # Mengirimkan permintaan HTTP GET ke API NewsAPI dan menyimpan responsnya.
    results = response.json() # Mengurai respons JSON menjadi objek Python.
    #print(res.json())
    news = results["articles"] #  Mendapatkan daftar artikel berita dari respons.
    for article in news: # Iterasi melalui setiap artikel berita.
        headlines.append(article['title']) # Menambahkan judul artikel ke dalam daftar judul.
    for i in range(len(headlines)): # Iterasi melalui setiap judul artikel dan mencetaknya di konsol.
        print(i+1, headlines[i]) 
    engine.say(headlines) # Mengucapkan daftar judul artikel menggunakan sintesis suara.
    engine.runAndWait() # Menjalankan mesin sintesis suara untuk mengucapkan daftar judul artikel.
get_news()
