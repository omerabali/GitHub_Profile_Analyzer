🔍 GitHub Profil Analiz ve Arama Aracı

Bu proje, Python Flask çatısı kullanılarak geliştirilmiş, GitHub kullanıcı profillerini ve genel kullanıcı aramasını gerçekleştiren basit ama şık bir web uygulamasıdır. Kullanıcıların profil bilgilerini (takipçi sayısı, repolar, bio vb.) hızlıca analiz etmesine olanak tanır.

🌟 Özellikler

Profil Görüntüleme: Belirtilen bir GitHub kullanıcı adının detaylı profil bilgilerini (avatar, biyografi, konum, repo sayısı, takipçi sayısı) gösterir.

Kullanıcı Arama: GitHub'ın arama API'sini kullanarak kullanıcı adlarına veya kelimelere göre arama yapar ve sonuçları listeler.

Teknolojiler: Flask, Requests kütüphanesi ve modern, koyu tema (GitHub Dark Mode benzeri) için Bootstrap ve özel CSS kullanılmıştır.

Tek Sayfa Uygulaması: Tüm fonksiyonellik tek bir Python dosyası içinde yönetilir.

🛠️ Kurulum ve Çalıştırma

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edin.

Ön Koşullar

Python 3.x

pip (Python paket yöneticisi)

Adımlar

Depoyu Klonlayın:

git clone [https://github.com/omerabali]
cd github-profil-analiz-araci


Gerekli Kütüphaneleri Kurun:
Projenin bağımlılıkları olan Flask ve requests kütüphanelerini kurun.

pip install Flask requests


Uygulamayı Çalıştırın:

python app.py


Erişim:
Tarayıcınızda http://127.0.0.1:5000 adresine giderek uygulamayı kullanmaya başlayabilirsiniz.

⚙️ Kullanılan Teknolojiler

Backend: Python, Flask

API: GitHub REST API

Frontend: HTML5, CSS3, Bootstrap 5 (Sadece stil için)
