**Link website**: https://stocktracker.adaptable.app/
<details>
<summary> TUGAS 2</summary>
# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- membuat direktori baru dapat menggunakan command prompt dengan mkdir / membuat folder langsung di laptop
- pada saat sudah cd ke directory StockTracker buat virtual environtment dengan menjalankan di command prompt
   python -m venv env
   env\Scripts\activate.bat
- menyiapkan dependencies , dengan membuat berkas requirements.txt dan menambahkan beberapa dependencies
- selanjutnya menjalankan virtual enviroment dengan mengawali perintah
   pip install -r requirements.txt
- buat proyek django dengan perintah 
   django-admin startproject StockTracker .
- menambahkan * di settings.py 
   ALLOWED_HOSTS = ["*"]
   menjalankan python manage.py runserver
- membuat repository github dengan nama Stock-Tracker dan menambahkan berkas .gitignore
- melakukan add , commit dan push 
- membuat deployment repository Stock-Tracker di Adaptable.io
- membuat aplikasi main dalam proyek Stock-Tracker , dengan menggunakan perintah 
   python manage.py startapp main
- merevisi code berikut di file settings.py
   INSTALLED_APPS = [
   ...,
   'main',
   ...
   ]
- Mengisi berkas HTML sesuai view yang diinginkan di butuhkan dengan membuat direktori baru bernama templates 
   dan mengisi file main.html
- mengubah berkas model sesuai di soal
- menjalankan perintah python manage.py makemigrations lalu python manage.py migrate
- mengintegrasikan komponen pada mvp dan memodifikasi templates
- mengonfigurasikan routing url dengan membuat berkas urls.py pada direktori main dan mengisi kode urls.py
- menambahkan unit test dengan mengisi berkas tests.py 
- mengisi readme sesuai dengan pertanyaan soal di vscode
- melakukan git add . , commit dan push

   

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   
![Bagan request client](INGLES.jpg)

# 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

- **alasan mengapa menggunakan virtual environtment**
penggunaan virtual environtment bertujuan untuk mengisolasi dan mengelola dependensi pada proyek serta untuk menghindari konflik antara paket Python yang berbeda dalam proyek yang berbeda berikut beberapa alasannya yang lebih spesifik :
   - Isolasi Depedensi : hal ini bertujuan agar berbagai proyek memiliki kemungkinan untuk menggunakan versi paket 
     yang berbeda dan tidak diinginkan adanya konflik diantara mereka.
   - Kebersihan : dapat dengan mudah menghapus atau mengganti dependensi proyek tanpa mempengaruhi sistem python 
     secara general.
   - Kemudahan mengelolo proyek : hal ini karena dapan dengan mudah untuk membuat mengaktifkan, dan menonaktifkan 
     lingkungan virtual, sehingga proyek tetap teratur dan bersih.

- **membuat aplikasi tanpa django virtual environtment**
   - pembuatan aplikasi tanpa menggunakan vitual environtment dapat dilakukan namun bukan praktik yang disarankan karena ada negatif sidenya.Berikut adalah negatif sidenya yaitu keterbatasan izin, penggunaan lingkungan global, pengembangan yang masih sederhana

# 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   
## MVC ( Model-View-Controller)
### Pengertian 
   suatu model yang seringkali digunakan oleh para pengembang software
### Komponen
- **Model**
berisi logika bisnis dan status data yang ada di dalam aplikasi.komponen ini bertugas untuk mendapatkan dan memanipulasi data, berkomunikasi dengan kontroller, berinteraksi dengan database, terkadang memperbarui tampilan dari aplikasi yang dikembangkan.
- **View**
komponen ini berhubungan dengan antarmuka pengguna yang terdiri dari HTML/CSS.XML. Komponen ini berkomunikasi dengan pengontrol dan terkadang berinteraksi dengan model.Viw berkerja sama dengan controller untuk menciptakan tampilan dinamis pada aplikasi yang dikembangkan.Tugas lain dari komponen ini untuk menyajikan data yang sesuai untuk pengguna.
- **Controller**
suatu aktivitas/fragmen yang berfungsi sebagai komunikator antara view dan model. Komponen ini membutuhkan suatu input pengguna dari layanan view/REST.Setelah itu, Permintaan "Get Data" diproses dari model dan diteruskan ke view untuk ditampilkan ke pengguna.
- **Perbedaan**
Dalam MVC, Controller berperan sebagai perantara antara Model dan View. View dan Model tidak mengetahui satu sama lain. Ini adalah pola desain yang paling umum dalam pengembangan web tradisional.
![Bagan Model View Controller](image.png)

## MVT (Model-View-Template)
### Pengertian
memiliki kemiripan dengan Model-View-Controller (MVC), MVT memiliki beberapa perbedaan konseptual.
### Komponen
- **Model**
memiliki kemiripan dengan model dalam pola Model-View- Controller, bertanggungjawab untuk mengelola data aplikasi, termasuk struktur basis data, validasi data, dan operasi yang berkaitan dengan data.
- **View**
mirip dengan View dalam MVC, bertnggung jawab untuk menampilkan data kepada pengguna.
- **Template**
mengatur bagaimana data dari model disajikan dalam View.
- **Perbedaan**
MVT adalah pola desain yang lebih umum digunakan dalam kerangka kerja Django untuk pengembangan web    dengan bahasa pemrograman Python.Perbedaan utama adalah penggunaan Template sebagai pengganti Controller.

## MVVM (Model-View-ViewModel)
### Pengertian 
merupakan gabungan dari MVC dan MVP. MVVM awalnya digunakan di dalam windows Presentation Foundation  (WPF) dan Silverlight, yang secara resmi diumumkan pada tahun 2005 oleh John Grossman dalam sebuah posting blog tentang Avalon. Pola yang digunakan berdasarkan gabungan dari MVC dan MVP mencoba untuk lebih jelas dalam memisahkan pengembangan UI dari logika bisnis dan perilaku dalam aplikasi.
### Komponen 
- **Model**
Model yang digunakan mirip dengan model pada MVC, dimana model tersebut terdiri dari data dasar yang digunakan untuk menjalankan perangkat lunak.
- **View**
View digunakan sebagai antarmuka grafis antara pengguna dan pola desain, serta menampilkan output dari data yang telah diproses. View yang digunakan MVVM mirip dengan View yang digunakan dalam MVC.
- **ViewModel**
suatu abtraksi dari View, lalu di sisi yang lain, sebagai penyedia pembungkus data model untuk ditautkan. ViewModel terdiri dari Model yang diubah menjadi View, dan berisi perintah yang dapat digunakan oleh View untuk mempengaruhi Model.
- **Perbedaan** 
MVVM memisahkan tugas Controller dalam MVX dengan menggunakan ViewModel. Hal ini lebih umum digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile atau desktop, dan membantu memisahkan logika bisnis dari tampilan degan lebih baik.


### Kesimpulan
Perbedaan utama antara ketiganya adalah bagaimana masing masing model mengatur aliran data dan tindakan dalam aplikasi.
</details> 

<details>
<summary> TUGAS 3</summary>

# 1. Apa perbedaan antara form POST dan form GET dalam Django?
## Metode Pengiriman Data
- **Form POST**
Data dikirim sebagai bagian dari tubuh permintaan HTTP. Data ini tidak terlihat dalam URL dan biasanya digunakan untuk mengirim data sensitif seperti kata sandi atau data yang panjang.
- **Form GET**
Data dikirimkan sebagai parameter yang terlihat dalam URL.Ini biasanya digunakan untuk mengambil data dari server dengan cara yang bersifat idempoten.
## Tampilan data pada URL
- **Form POST**
Data tidak terlihat pada URL sehingga lebih aman dan tidak terbaca oleh pengguna yang melihat histori peramban atau log server.
- **Form GET**
Data terlihat pada URL dan dapat terlihat oleh siapa saja yang melihat URL.
## Jumlah data yang bisa dikirim
- **Form POST**
Dapat mengirimkan jumlah data yang lebih besar deng form POST karena data dikirim sebagai bagian dari tubuh permintaan HTTP.
- **Form GET**
Terdapat batasan pada jumlah data yang dapat dikirimkan dengn form GET karena data harus ditambahkan ke dalam URL. 
## Keamanan
- **Form POST**
Lebih aman untuk mengirim data sensitif karena data tidak terlihat pada URL dan tidak terjadi pencurian data melalui URL
- **Form GET**
Lebih tidak aman untuk data sensitif karena data terlihat pada URL dan dapat dengan mudah diakses oleh pihak ketiga


# 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
## Struktur dan Notasi
- **XML**
memiliki sintaks yang lebih kaku dan kompleks dibandingkan JSON dan HTML. XML biasanya digunakan untuk pertukaran data yang terstruktur dengan tipe data yang didefinisikan sendiri.
- **JSON**
memiliki format yang lebih ringan dan mudah dibaca dengan menggunakan pasangan nama/kunci dan nilai.
- **HTML**
Bahasa markup khusus untuk membuat dokumen web dan digunakan untuk merancang tampilan serta struktur web, bukan untuk pertukaran data mentah
## Tujuan Utama
- **XML**
Digunakan untuk pertukaran data terstruktur yang kompleks antara sistem yang berbeda.
- **JSON**
Digunakan untuk pertukaran data ringan, terutama dalam konteks pengembangan web dan API.
- **HTML**
Digunakan untuk membuat tampilan halaman web dan mengatur tampilan konten.
## Flexibility
- **XML**
Lebih fleksibel dalam hal mendefinisikan struktur data yang kustom. Anda dapat membuat skema XML sesuai dengan kebutuhan Anda.
- **JSON**
Lebih sederhana dalam hal struktur dan lebih cocok untuk data yang berurutan atau hirarkis, seperti daftar atau objek bersarang.
- **HTML**
Lebih terbatas pada tampilan halaman web, dengan struktur yang telah ditentukan seperti elemen <div>, <p>, atau <table>.
## Mendukung tipe data
- **XML**
Dukungan yang lebih baik untuk tipe data yang kompleks melalui skema XML.
- **JSON**
Mendukung tipe data yang sederhana seperti string, angka, boolean, array dan objek.
- **HTML**
Tidak dirancang untuk menyimpan data dalam tipe data yang berarti karena digunakan untuk merancang tampilan web.

# 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Memiliki format yang ringan dan mudah dibaca oleh manusia dengan cara menggabungkan pasangan nama/kunci dan nilai yang sederhana dalam struktur yang intuitif.
- sangat mudah di integrasikan denga kode JavaScript.
- Dapat dengan mudha mengonversi data JSON kedalam objek atau struktur data yang sesuai degan bahasa pemrograman yang digunakan server atau klien.
- memiliki format terbuka dan tidak memiliki ketergantungan pada platform tertentu.
- mendukung tipe data yang umum digunakan.
- JSON dapat digunakan untuk mengirim berbagai jenis konten
- Dapat digunakan untuk mengirim data dari server ke klien begitupun sebaliknya.
- memiliki format yang cocok untuk digunakan dalam API REST.
# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Menjalankan virtual environtment
- mengubah path pada StockTracker di file urls.py menjadi 
urlpatterns = [
path('', include('main.urls')),
path('admin/', admin.site.urls),
]
- membuat folder templates dan membuat file base.html dan di isi
- mengubah 'DIRS': [BASE_DIR / 'templates'], pada subdirektori stocktracker di setting.py
- membuat berkas baru degan nama forms.py dan menyesuaikan strukturnya
- pada berkas views.py di folder main import 
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse

dan menambah fungsi create_product yang menerima parameter request
- mengubah fungsi show_main pada berkas views.py dengan menambahkan products = Product.objects.all() dan 'products': products di dalam context pada fungsi 
- menambahkan import fungsi create product pada urls.py di folder main
- menambahkan path url ke urlpatterns pada urls.py di main
- buat berkas baru create_product.html pada direktori main/templates dan mengisi kode sesuai dengan keinginan soal
- menambahkan kode {% block content %} pada main.html
- mengembalikan data dalam bentuk xml dengan mengimport httpResponse dan Serialize pada views.py dan membuat fungsi sho_xml dengan parameter request dan menambahkan return function
- mengimport fungsi yang sudah di buat pada urls.py di folder main dan menambahkan path url kedalam urlpatterns
- mengembalikan data dalam bentuk json dengn membuat fungsi show_json yang menerima parameter request en menyimpan variabel di data , setelah otu tambahkan return function berupa httpResponse dan mengimport show_json pada urls.py di folder main , setelah itu path juga ditambahkan
- mengembalikan data berdasarkan id dalam bentuk XML dan JSON dengan cara membuat fungsi show_xml_by_id dan show_json_by_id pafa views.py di folder main , setelah itu membuat variabel fungsi dengan menyimpan hasil query dengan id tertentu. setelah itu menambahkan return function berupa HttpResponse yang berisi padara data hasil query yang sudah diserialisasi dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).
- mengimport fungsi yang tadi di buat di file urls.py pada folder main dan menambahkan path url ke dalam urlpatterns.
- melakukan deployment
# 5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![json-id hasil akses](json-id.jpeg)
![json hasil akses](json.jpeg)
![xml-id hasil akses](xml-id.jpeg)
![xml hasil akses](xml.jpeg)
![localhost hasil akses](localhost.jpeg)
</details> 

<details>
<summary> TUGAS 4 </summary>

# 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
## Pengertian 
- form ini digunakan untuk membuat formulir pendaftan atau registrasi pengguna dalam aplikasi web yang dibangun dengan Django. Form ini telah disertakan dalam modul "django.contrib.auth.forms" dan dirancang khusus untuk membuat pengguna baru dengan informasi seperti username, password, dan email. Dengan menggunakan "UserCreationForm" , kita dapat mengintegrasikan sistem otentikasi pengguna yang kuat dan aman ke dalam aplikasi web tanpa harus menulis kode pendaftaran pengguna dari awal
## Kelebihan :
- **Sederhana dan cepat**
Mudah digunakan tanpa penulisan kode pendaftaran manual.
- **keamanan Terintegrasi**
Menerapkan keamanan otentikasi dan proteksi sesi bawaan Django.
- **kustomisasi mudah**
Biisa disesuaikan dengan tambahan bidang atau validasi khusus.
## Kekurangan :
- **Tidak sesuai semua kasus**
Tidak cocok untuk aplikasi dengan pendaftaran kustom atau kompleks.
- **Terbatas dalam Fungsi**
Fokus pada informasi dasar pengguna seperti username dan kata sandi.
- **Tampilan mungkin perlu disesuaikan**
Tampilan default mungkin tidak sesuai dengan aplikasi.
# 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- **Autentikasi**
- Proses verifikasi identitas pengguna
- Langkah pertama yang harus diambil oleh aplikasi web saat pengguna mencoba masuk. Ini memastikan bahwa hanya pengguna yang sah yang memiliki akses ke akun dan data mereka.
- Django menyediakan sistem autentikasi bawaan yang dapat digunakan untuk mengelola otentikasi pengguna dengan aman, termasuk manajemen sesi, penyimpanan kata sandi yang di-hash, dan fitur keamanan lainnya.  
- **Otorisasi**
- Proses menentukan apa yang dapat dilakukan pengguna setelah mereka berhasil diautentikasi
- Otorisasi memastikan bahwa pengguna hanya dapat mengakses sumber daya atau fungsi yang sesuai dengan peran atau izin mereka dalam sistem.
- Django menyediakan sistem otorisasi yang memungkinkan anda untuk mengatur peran penting pengguna dan mengontrol akses mereka ke tampilan atau objek dalam aplikasi anda.
- **Mengapa keduanya penting**
- melindungi akun dan mengatur akses.
- mengendalikan akses data berdasarkan peran.
- mematuhi regulasi privasi
- mengelola izin pengguna agar lebih efisien
# 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
- **pengertian**
Sepotong data kecil yang disimpan di sisi klien saat pengguna berinteraksi dengan sebuah situs web. Cookies digunakan untuk menyimpan informasi tertentu yang dapat diakses oleh server web saat pengguna kembali ke situs tersebut. Hal ini memungkinkan pengembang web untuk melacak informasi seperti preferensi pengguna, status login , dan data sesi.
- **cara Django menggunakan cookies untuk mengelola sesi pengguna**
- Aktifkan sistem sesi : mengaktifkan sistem sesi dalam berkas settings.py 
- Penyimpanan Data Sesi : Saat pengguna berinteraksi dengan aplikasi sehingga dapat menyimpan data sesi pengguna dengan mengaitkannya dengan kunci tertentu dalam objek sesi Django.
- Penyimpanan dalam Cookie : setelah mengonfirmasi penyimpanan sesi sebagai cookie, Django akan secara otomatis mengambil data sesi yang sesuai dan mengirimannya sebagai cookie ke peramban pengguna . Cookie sering berisi ID sesi yang digunakan oleh Django untuk mengidentifikasi sesi pengguna.
- Mengambil Data Sesuai Kunci : Setiap kali pengguna mengirimkan permintaan berikutnya , cookie yang mengandung ID sesi akan dikirimkan ke server Django. Django akan menggunakan ID sesi ini untuk mengambil data sesi yang sesuai dan membuatnya tersedia dalam tampilan dan logika aplikasi anda.
- Menggunakan Data Sesuai kebutuhan : dengan menggunakan data sesi ini unutk mengelola status login, menyimpanan preferensi pengguna, atau menyimpan informasi penting lainnya selama sesi pengguna berlangsung
# 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
keamanan penggunaan cookies tergantung pada bagaimana kita mengimplementasikan dan apa yang di simpan dalam cookies.
**Risiko potensial yang perlu harus diwaspai**
- Pencurian Data
Cookies adalah data yang disimpan di sisi klien ( Browser pengguna). Jika menyimpan data sensitif, seperti token otentikasi atau kata sandi yang tidak di-hash dengan benar, maka ada risiko penjurian data jika cookies diretas atau dicuri.
- Man-in-the-Middle Attacks
Jika koneksi antara pengguna dan server tidak dienkripsi dengan baik, cookies dapat rentan terhadap serangan man-in-the-middle. Penyerang dapat mencuri cookies saat data dikirimkan antara pengguna dan server.
- Cookie Spoofing 
Penyerang dapat mencoba memanipulasi atau meretas cookies untuk mengakses akun pengguna tanpa izin.
- Cross-Site Scripting (XSS)
Jika aplikasi anda rentan terhadap serangan XSS, penyerang dapat mencuri cookies pengguna atau menjalankan kode berbahaya di browser pengguna.
# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**Membuat Fungsi dan Form Register**
- membuat virtual environtment , lalu membuat fungsi register di views.py pada subdirektori main
- menambahkan redirect , UserCreationForm, messages
- membuat dan mengisi regiter.html pada folder main/templates
- mengimport fungsi urls.py pada subdirektori main dan menambahkan path url ke urlspatterns
**Membuat Fungsi Login**
- membuat fungsi dengan nama login_user yang menerima paraemeter user di views.py pada subdirektori main dan menambahkan import authenticate dan login
- membuat dan mengisi berkas login.html pada folder main/templates
- mengimport  fungsi login_user di urls.py pada subdirektori main dan tambahkan path url ke urlpatterns
**Membuat Fungsi Logout**
- membuat dengan nama logout_user dengan parameter request di views.py pada subdirektori main dan menambahkan import di logout
- menambahkan <a href="{% url 'main:logout' %}"> setelah add new product main.html di folder main/templates
- mengimport fungsi logout_user urls.py main , path url urlpatterns
**Meretstriksi akses halaman main**
- menambahkan import login required di file views.py pada subdirektori main
- menambahkan kode @login_required(login_url='/login')  diatas fungsi show_main
**Menggunakan data dari cookies**
- mengimport HttpResponseRedirect, reverse, dan datetime di file views.py di subdirektori main.
- merevisi fungsi login user dan logout user
- menambah kode 'last_login': request.COOKIES['last_login'] di variabel context
- <h5>Sesi terakhir login: {{ last_login }}</h5> di main.html
**Menghubungkan Model Product dengan user**
- mengimpor user pada models.py subdirektori main
-  menambahkan model product  user = models.ForeignKey(User, on_delete=models.CASCADE)
-  merevisi code pada fungsi create_product di file views.py di subdirektori main dan merevisi fungsi show_main
-  melakukan python manage.py makemigrations dan python manage.py migrate
- menambahkan 2 user dan 3 product
</details> 

<details>
<summary> TUGAS 5 </summary>

# Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
- **Universal Selector (*)** 
Menggambarkan semua elemen dalam halaman HTML. Sebaiknya digunakan dengan sangat hati-hati, karena dapat memengaruhi semua elemen di halaman. Umumnya digunakan untuk menetapkan properti default di seluruh halaman.
- **Type Selector (element)**
Menggambarkan semua elemen dengan jenis tertentu. Cocok digunakan ketika Anda ingin menerapkan gaya tertentu pada semua elemen dari jenis yang sama (misalnya, semua <h1>).
- **Class Selector (.class)**
Menggambarkan elemen yang memiliki atribut class tertentu. Berguna untuk menetapkan gaya pada beberapa elemen yang memiliki class yang sama.
- **ID Selector (#id)**
Menggambarkan elemen dengan atribut id tertentu. Harus digunakan dengan unik, karena id harus unik dalam satu halaman. Cocok untuk menargetkan elemen tertentu.
- **Descendant Selector (ancestor descendant)**
Menggambarkan elemen yang merupakan turunan dari elemen lain. Berguna untuk menetapkan gaya kepada elemen dalam konteks tertentu.
- **Child Selector (parent > child)**
Menggambarkan elemen yang adalah anak langsung dari elemen lain. Berguna untuk menargetkan elemen yang merupakan anak langsung dari elemen tertentu.

# Jelaskan HTML5 Tag yang kamu ketahui.
- **<header>**
Digunakan untuk menentukan bagian atas (header) dari sebuah dokumen atau bagian dari sebuah halaman web.
- **<nav>** 
Menggambarkan bagian navigasi dari sebuah halaman web.
- **<main>**
Menandakan konten utama dalam sebuah halaman web.
- **<section>**
Digunakan untuk mengelompokkan konten yang terkait dalam sebuah halaman.
- **<article>**
Menggambarkan konten independen yang dapat berdiri sendiri, seperti artikel berita.
- **<aside>**
Menggambarkan konten yang terkait dengan konten sekitarnya, seperti sidebar.
- **<footer>**
Digunakan untuk menentukan bagian bawah (footer) dari sebuah dokumen atau bagian dari sebuah halaman web.

# Jelaskan perbedaan antara margin dan padding.
- **Margin**
Margin adalah ruang di sekitar elemen HTML. Ini menciptakan jarak antara elemen dan elemen lain di luarnya. Margin tidak memiliki warna latar belakang dan biasanya digunakan untuk mengatur jarak antara elemen-elemen.
- **Padding**
Padding adalah ruang di dalam elemen HTML, antara batas elemen dan kontennya sendiri. Padding biasanya memiliki warna latar belakang yang sama dengan elemen itu sendiri dan digunakan untuk mengatur jarak antara konten dan batas elemen.

# Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? 

## Perbedaan antara CSS Framework Tailwind dan Bootstrap

**Tailwind CSS**

Pendekatan utility-first, yang berarti Anda membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah ada.
Fleksibel dan memungkinkan penyesuaian yang tinggi.
Tidak memiliki desain visual bawaan, memberikan kebebasan lebih besar dalam desain.
Cocok untuk proyek-proyek yang membutuhkan desain yang sangat kustom dan kecil dalam hal ukuran file CSS.

**Bootstrap**

Lebih memiliki desain visual bawaan dengan gaya UI yang sudah ditentukan.
Memiliki komponen-komponen UI yang siap digunakan.
Cocok untuk proyek dengan waktu pengembangan yang singkat dan memerlukan desain yang konsisten.
Lebih mudah digunakan bagi pengembang pemula.

## Kapan Menggunakan Bootstrap atau Tailwind
**Gunakan Bootstrap** jika Anda ingin cepat membangun situs dengan desain yang konsisten dan tidak memiliki banyak waktu untuk menyesuaikan tampilan.
**Gunakan Tailwind CSS** jika Anda ingin tingkat kontrol yang tinggi atas desain dan siap untuk menghabiskan waktu lebih dalam menyesuaikan tampilan Anda. Cocok untuk proyek- proyek yang membutuhkan desain yang sangat kustom.
</details>



