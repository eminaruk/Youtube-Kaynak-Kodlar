import cv2

from ultralytics import solutions

kayit = cv2.VideoCapture("araba.mp4")
assert kayit.isOpened(), "Dosyaya erişilemiyor veya dosya bulunamadı."
genislik, yukseklik, fps = (int(kayit.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Bölge noktalarını tanımla
cizgi_konumlari = [(0, yukseklik-200), (genislik, yukseklik-200)]  # Çizgi sayımı için
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  # Dikdörtgen bölge sayımı için
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360), (20, 400)]  # Çokgen bölge sayımı için

# Video yazıcı
video_yazici = cv2.VideoWriter("nesne_sayma_ciktisi.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (genislik, yukseklik))

# Nesne Sayacı başlat
sayac = solutions.ObjectCounter(
    show=True,  # Çıktıyı göster
    region=cizgi_konumlari,  # Bölge noktalarını geçir
    model="yolo11n.pt",  # Nesne sayımı için YOLO11 OBB modelini kullanmak için model="yolo11n-obb.pt".
    # classes=[0, 2],  # COCO önceden eğitilmiş modeli ile belirli sınıfları saymak istiyorsanız, örneğin kişi ve araba.
    show_in=True,  # Giriş sayımlarını göster
    # show_out=True,  # Çıkış sayımlarını göster
    line_width=3,  # Sınır kutuları ve metin gösterimi için çizgi genişliğini ayarla
)

# Videoyu işle
while kayit.isOpened():
    durum, kare = kayit.read()
    if not durum:
        print("Video bitti.")
        break
    
    kare = sayac.count(kare)
    video_yazici.write(kare)

kayit.release()
video_yazici.release()
cv2.destroyAllWindows()