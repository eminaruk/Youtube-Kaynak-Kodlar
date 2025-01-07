# Ultralytics ile Boş Park Yeri Tespiti Uygulaması

<h2>Video</h2>
https://www.youtube.com/watch?v=c7A8A7NJrac

******************************************************************************
Bu proje, Ultralytics'in `solutions` kütüphanesi kullanılarak boş park yeri te
spiti yapan bir video işleme uygulamasıdır. 
`yolo11n.pt` modeli ile nesne sayımı gerçekleştirilmiştir. 

## Özellikler
- Videodan gelen karelerde nesne tespiti ve sayımı.
- Kullanıcının belirttiği bölgeye göre sayım yapabilme.
- Sayım verilerini video çıktısına kaydetme.

## Gereksinimler
- Python 3.7 veya üstü
- Numpy
- Ultralytics kütüphanesi


## Kurulum

1. Gerekli kütüphaneleri yükleyin:
   pip install ultralytics numpy==1.26.4

2. Proje dosyasını bilgisayarınıza indirin.

## Kullanım

1. Proje klasöründe bir video dosyası (örneğin `araba.mp4`) bulunmalıdır.
2. Uygulamayı çalıştırın:
   python main.py
3. İşlem tamamlandıktan sonra, tespit edilen nesnelerle birlikte işlenmiş video dosyası `nesne_sayma_ciktisi.avi` olarak kaydedilecektir.

## Kod Parçacığı İçeriği

Ana Mantık:
- `cizgi_konumlari`: Nesnelerin hangi bölgede sayılacağını belirtir.
- `solutions.ObjectCounter`: Ultralytics modelini kullanarak nesne sayımı gerçekleştirir.
- `cv2.VideoWriter`: İşlenmiş video çıktısını kaydeder.


