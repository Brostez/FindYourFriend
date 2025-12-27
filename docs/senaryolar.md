\# Find Your Friend - Yazılım Modelleme Senaryoları



\## 1. Gereksinim Senaryosu (Requirement Scenario)

Üniversite kampüslerinde öğrenciler, spor takımı kurmak veya oyun oynamak gibi anlık sosyal ihtiyaçlarını karşılamakta zorluk çekmektedir. Mevcut platformlar (Twitter, Instagram) hiper-lokal ve anlık eşleşmelerde yetersiz kalmakta, ayrıca güvenlik sorunları barındırmaktadır.

\*\*Gereksinimler:\*\*

\* Sistem, sadece kurumsal üniversite e-postası (@mersin.edu.tr) ile kayıt kabul etmelidir.

\* Kullanıcılar harita üzerinde anlık konumlarına etkinlik "pin"i bırakabilmelidir.

\* Yakındaki diğer öğrenciler bu çağrıları görüp "Katıl" isteği gönderebilmelidir.

\* Aktivite sonrası kullanıcılar birbirini puanlayarak "Güven Skoru" oluşturmalıdır.



\## 2. Use Case (Kullanım Durumu)

\*\*Aktör:\*\* Üniversite Öğrencisi

\*\*Temel Akış:\*\*

1\. \*\*Giriş Yap:\*\* Öğrenci, okul maili ile sisteme giriş yapar.

2\. \*\*Çağrı Oluştur:\*\* "Futbol" veya "Satranç" kategorisini seçer, haritada konum işaretler.

3\. \*\*Eşleşme:\*\* Başka bir öğrenci haritadaki pini görür ve "Katıl" der.

4\. \*\*Onaylama:\*\* Çağrı sahibi isteği onaylar, sohbet başlar.

5\. \*\*Puanlama:\*\* Buluşma sonrası taraflar birbirine puan verir.



\## 3. Ana Senaryo (Main Scenario - Happy Path)

1\. \*\*Başlangıç:\*\* Kullanıcı uygulamayı açar.

2\. \*\*Doğrulama:\*\* Sistem `@mersin.edu.tr` uzantısını kontrol eder ve girişe izin verir.

3\. \*\*Aksiyon:\*\* Kullanıcı kütüphane önünde "Satranç Partneri Aranıyor" ilanı açar.

4\. \*\*Tepki:\*\* 500 metre yakındaki başka bir kullanıcı bildirimi görür.

5\. \*\*Sonuç:\*\* İkinci kullanıcı ilana tıklar, eşleşme sağlanır ve konum bilgisi paylaşılır.

