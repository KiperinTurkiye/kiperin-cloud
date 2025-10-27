import qrcode
import os

def create_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR kodu '{file_name}' dosyasına oluşturuldu.")

if __name__ == "__main__":
    base_url = "https://www.kiperincloud.com/card/"
    
    # Personel listesi
    personel = [
        ("batuhanpektas", "Batuhan Pektaş"),
        ("busrakoz", "Büşra Köz"),
        ("cemrenurerdal", "Cemranur Erdal"),
        ("hasansamuk", "Hasan Samuk"),
        ("tolgapektas", "Tolga Pektaş")
    ]
    
    # qrs klasörü ve alt klasörlerini oluştur
    os.makedirs("qrs/en", exist_ok=True)
    os.makedirs("qrs/tr", exist_ok=True)
    
    # Her personel için TR ve EN QR kodları oluştur
    for url_name, display_name in personel:
        # EN QR
        en_url = f"{base_url}{url_name}/en/"
        en_file = os.path.join("qrs/en", f"{url_name}.png")
        create_qr_code(en_url, en_file)
        
        # TR QR
        tr_url = f"{base_url}{url_name}/tr/"
        tr_file = os.path.join("qrs/tr", f"{url_name}.png")
        create_qr_code(tr_url, tr_file)
    
    print("\nTüm QR kodları başarıyla oluşturuldu!")