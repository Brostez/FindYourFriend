from flask import Flask, jsonify, request
import datetime

# Find Your Friend - Backend Simülasyonu
# Bu kod, projenin temel senaryolarını (Giriş, Etkinlik, Eşleşme) modeller.

app = Flask(__name__)

# Geçici Veritabanı (Bellekte tutulur)
events = []  # Etkinliklerin tutulduğu liste

@app.route('/')
def home():
    return jsonify({
        "Proje": "Find Your Friend",
        "Durum": "Sunucu Calisiyor",
        "Versiyon": "1.0.0 Prototype"
    })

# SENARYO 1: Güvenli Giriş (Sadece mersin.edu.tr)
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    
    # Modelleme Mantığı: Uzantı kontrolü
    if email and email.endswith('@mersin.edu.tr'):
        return jsonify({
            "mesaj": "Giris Basarili! Hos geldin.",
            "kullanici": email,
            "onay": True
        }), 200
    else:
        return jsonify({
            "mesaj": "Giris Reddedildi. Sadece kurumsal e-posta ile girilebilir.",
            "onay": False
        }), 403

# SENARYO 2: Etkinlik Çağrısı Oluşturma (Pin Bırakma)
@app.route('/api/create_event', methods=['POST'])
def create_event():
    data = request.get_json()
    
    new_event = {
        "id": len(events) + 1,
        "kullanici": data.get('kullanici'),
        "aktivite": data.get('aktivite'),  # Örn: Satranç, Futbol
        "konum": data.get('konum'),        # Örn: Kütüphane Önü
        "zaman": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    events.append(new_event)
    return jsonify({"mesaj": "Etkinlik Haritaya Eklendi!", "detay": new_event}), 201

# SENARYO 3: Etkinlikleri Listeleme (Eşleşme Ekranı)
@app.route('/api/list_events', methods=['GET'])
def list_events():
    return jsonify({
        "aktif_etkinlikler": events,
        "toplam_sayi": len(events)
    })

if __name__ == '__main__':
    print("Find Your Friend Sunucusu Baslatiliyor...")
    # Port 5000'de çalışır
    app.run(debug=True)