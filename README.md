# Sistem Pakar Gangguan Postur Tubuh

## 📋 Deskripsi Proyek

**sistem_pakar-gangguan_tubuh** adalah aplikasi web interaktif yang dirancang untuk mendiagnosa berbagai gangguan postur tubuh menggunakan pendekatan **Sistem Pakar (Expert System)**. Aplikasi ini membantu pengguna mengidentifikasi kondisi postur mereka berdasarkan gejala yang dialami.

### Penyakit yang Dapat Didiagnosa

1. **Lordosis** - Lengkungan tulang belakang ke dalam secara berlebihan di area pinggang
2. **Kifosis** - Postur tubuh membungkuk dengan lengkungan tulang belakang ke arah luar
3. **Skoliosis** - Lengkungan tulang belakang abnormal ke samping
4. **Forward Head Posture (FHP)** - Postur kepala yang cenderung condong ke depan
5. **Flat Back Syndrome (FBS)** - Kehilangan lengkungan normal tulang belakang bagian bawah

---

## 🏗️ Struktur Proyek

```
sistem_pakar-gangguan_tubuh/
├── app.py                 # Flask application utama
├── metode.py             # Business logic sistem pakar (inferensi)
├── templates/            # Folder template HTML
│   ├── index.html        # Halaman utama/selamat datang
│   ├── diagnosa.html     # Halaman diagnosa interaktif
│   ├── pencegahan.html   # Halaman pencegahan & tips
│   └── layout.html       # Template dasar (base template)
└── README.md             # File dokumentasi ini
```

---

## 🔧 Teknologi yang Digunakan

| Komponen | Teknologi |
|----------|-----------|
| **Backend** | Flask (Python Web Framework) |
| **Frontend** | HTML5, Bootstrap CSS |
| **Mesin Inferensi** | Rule-Based Forward Chaining |
| **Database** | Knowledge Base (Dictionary) |

---

## 📚 Komponen Utama

### 1. **app.py** - Flask Application
Berisi routing utama aplikasi dengan 3 endpoint:

| Route | Method | Fungsi |
|-------|--------|--------|
| `/` | GET | Menampilkan halaman utama dengan penjelasan penyakit |
| `/diagnosa` | GET, POST | Menampilkan form diagnosa & memproses hasil |
| `/pencegahan` | GET | Menampilkan tips pencegahan gangguan postur |

### 2. **metode.py** - Knowledge Base & Inference Engine

#### Komponen Utama:
- **gejala_list** (18 gejala) - Daftar semua gejala yang mungkin dialami
- **penyakit** (5 penyakit) - Database penyakit yang dapat didiagnosa
- **aturan** (8 aturan) - Rule-based knowledge menggunakan teknik **Forward Chaining**
- **fungsi inferensi()** - Mesin inferensi untuk mencocokkan gejala dengan aturan

#### Contoh Aturan Inferensi:
```python
# Jika pengguna memiliki semua gejala berikut → Lordosis
(["G01", "G02", "G03", "G04"], "P01")

# Jika pengguna memiliki semua gejala berikut → Kifosis  
(["G05", "G06", "G07", "G08", "G09"], "P02")
```

### 3. **Templates HTML**

#### layout.html
- Template dasar dengan Bootstrap styling
- Navigation bar dan layout responsif

#### index.html
- Halaman selamat datang
- Penjelasan detail setiap penyakit dengan informasi medis
- Link ke dokter (Alodokter) untuk informasi lebih lanjut

#### diagnosa.html
- Form checklist interaktif dengan 18 gejala
- Tombol submit untuk memproses diagnosa
- Menampilkan hasil diagnosis yang relevan

#### pencegahan.html
- Tips dan trik pencegahan gangguan postur
- Panduan gaya hidup sehat

---

## 📊 Analisis Sistem Pakar

### Tipe Sistem Pakar
**Rule-Based Expert System** dengan pendekatan **Forward Chaining**

### Fitur Utama
✅ Knowledge base terstruktur dengan 18 gejala dan 5 penyakit  
✅ 8 aturan inferensi untuk diagnosis akurat  
✅ Interface web user-friendly dengan Bootstrap  
✅ Proses diagnosa real-time  
✅ Informasi pencegahan dan tips kesehatan  

### Mekanisme Kerja
1. Pengguna memilih gejala yang dialami di halaman diagnosa
2. Data gejala dikirim ke backend via POST request
3. Fungsi `inferensi()` mencocokkan gejala dengan aturan yang ada
4. Sistem mengembalikan hasil diagnosis (penyakit yang cocok)
5. Hasil ditampilkan kembali ke frontend

---

## 🚀 Cara Menjalankan

### Prerequisites
```bash
Python 3.6+
pip (Python package manager)
```

### Instalasi & Setup

1. **Clone atau download project**
   ```bash
   cd "d:\sistem_pakar-gangguan_tubuh"
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

4. **Akses di browser**
   ```
   http://localhost:5000
   ```

---

## 📖 Panduan Penggunaan

### 1. Halaman Utama (Home)
- Baca penjelasan tentang berbagai gangguan postur
- Klik tombol "Diagnosa sekarang!" untuk mulai

### 2. Halaman Diagnosa
- Pilih semua gejala yang Anda alami dari daftar checkbox
- Klik tombol "Diagnosa" untuk melihat hasil
- Hasil akan menampilkan penyakit yang teridentifikasi berdasarkan gejala pilihan

### 3. Halaman Pencegahan
- Baca tips dan panduan pencegahan gangguan postur
- Pelajari tips hidup sehat untuk menjaga postur tubuh

---

## 📈 Daftar Gejala (Symptoms)

| Kode | Gejala |
|------|--------|
| G01 | Nyeri punggung bagian bawah |
| G02 | Kepala, leher, perut, dan bagian pinggul tampak lebih maju |
| G03 | Kesulitan menempelkan area punggung pada tempat tidur atau lantai |
| G04 | Postur tubuh membusung |
| G05 | Kepala terlihat lebih condong ke depan |
| G06 | Tubuh menjadi bungkuk |
| G07 | Ada seperti punuk di bagian punggung atas |
| G08 | Tulang punggung terasa kaku dan otot belakang paha kencang |
| G09 | Perbedaan tinggi bahu kanan dan kiri |
| G10 | Tubuh cenderung condong ke satu sisi |
| G11 | Salah satu kaki lebih panjang saat berdiri tegak |
| G12 | Tinggi pinggang tidak rata |
| G13 | Kepala tidak sejajar dengan bahu |
| G14 | Nyeri leher dan bahu |
| G15 | Leher terasa kaku dan tegang |
| G16 | Kesulitan dalam berdiri tegak |
| G17 | Masalah dengan keseimbangan saat berdiri atau duduk |
| G18 | Postur tubuh condong ke depan |

---

## 🎯 Skenario Pengujian (Test Cases)

### Test Case 1: Diagnosis Lordosis
**Input:** G01, G02, G03, G04  
**Output:** Lordosis ✅

### Test Case 2: Diagnosis Kifosis
**Input:** G05, G06, G07, G08, G09  
**Output:** Kifosis ✅

### Test Case 3: Diagnosis Skoliosis
**Input:** G09, G10, G11, G12  
**Output:** Skoliosis ✅

### Test Case 4: Diagnosis FHP
**Input:** G05, G13, G14, G15  
**Output:** Forward Head Posture (FHP) ✅

### Test Case 5: Diagnosis FBS
**Input:** G01, G16, G17  
**Output:** Flat Back Syndrome (FBS) ✅

---

## ⚠️ Keterbatasan & Catatan Penting

⚠️ **Disclaimer:** Aplikasi ini adalah **sistem pakar edukasi** dan BUKAN pengganti diagnosis medis profesional  
⚠️ Hasil diagnosis hanya berdasarkan gejala yang dipilih pengguna  
⚠️ Untuk diagnosis akurat, konsultasikan dengan tenaga medis profesional  
⚠️ Knowledge base dapat diperluas dengan aturan dan gejala tambahan  

---

## 🔮 Pengembangan Lebih Lanjut

Berikut saran untuk meningkatkan sistem:

1. **Database Integration**
   - Implementasi database (SQL) untuk menyimpan history diagnosa
   - Tracking data pengguna untuk analisis statistik

2. **Machine Learning**
   - Tambahkan probabilitas ke setiap aturan
   - Implementasi certainty factors untuk diagnosis lebih akurat
   - Training model dari data diagnosis sebelumnya

3. **User Experience**
   - Tambahkan grafik/visualisasi hasil diagnosis
   - Implementasi user authentication dan login
   - Export hasil diagnosis ke PDF

4. **Backend Enhancement**
   - REST API untuk integrasi dengan aplikasi lain
   - Caching untuk performa lebih baik
   - Logging system untuk monitoring

5. **Content**
   - Tambahkan video tutorial tentang gejala
   - Integrasi dengan konsultasi dokter online
   - Panduan latihan/senam untuk setiap kondisi

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan UTS (Ujian Tengah Semester) Sistem Pakar.

---

## 👨‍💼 Tim Pengembang

- **Program Studi:** Teknologi Informasi
- **Semester:** 4
- **Mata Kuliah:** Sistem Pakar

---

## 📞 Support & Troubleshooting

### Error: ModuleNotFoundError: No module named 'flask'
```bash
pip install flask
```

### Port 5000 sudah terpakai
Ubah port di app.py:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Ganti ke port lain
```

### Aplikasi tidak bisa diakses di localhost
- Pastikan Flask sedang running (lihat console)
- Akses http://127.0.0.1:5000 atau http://localhost:5000

---

## 📚 Referensi

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Alodokter - Lordosis](https://www.alodokter.com/lordosis)
- [Alodokter - Kyphosis](https://www.alodokter.com/kyphosis)
- [Expert Systems - Wikipedia](https://en.wikipedia.org/wiki/Expert_system)

---

**Terakhir diupdate:** April 2026  
**Status:** ✅ Aktif & Berfungsi Baik
