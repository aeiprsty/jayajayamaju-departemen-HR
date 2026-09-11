# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan. Perusahaan saat ini menghadapi permasalahan employee attrition dengan tingkat attrition lebih dari 10%.

Employee attrition menjadi permasalahan penting bagi perusahaan karena tingginya jumlah karyawan yang keluar dapat berdampak pada keberlangsungan operasional dan produktivitas perusahaan. Karyawan yang keluar perlu digantikan melalui proses rekrutmen dan onboarding, yang membutuhkan waktu, biaya, serta sumber daya. Selain itu, kehilangan karyawan yang berpengalaman dapat menyebabkan hilangnya pengetahuan dan pengalaman yang telah dimiliki oleh karyawan tersebut.

Bagi departemen Human Resources (HR), tantangan utamanya adalah memahami karakteristik dan kondisi karyawan yang berkaitan dengan tingginya attrition sehingga strategi retensi dapat dilakukan secara lebih tepat sasaran. Tanpa adanya analisis berbasis data, tindakan retensi berisiko dilakukan secara umum dan kurang sesuai dengan kelompok karyawan yang membutuhkan perhatian lebih.

Oleh karena itu, proyek ini dilakukan untuk menganalisis faktor-faktor yang berhubungan dengan employee attrition, menyajikan hasil analisis melalui business dashboard, serta membangun model machine learning sederhana yang dapat digunakan sebagai early warning system bagi HR.

### Permasalahan Bisnis

Jaya Jaya Maju menghadapi tingkat employee attrition yang telah melebihi 10%, sehingga perusahaan berisiko mengalami peningkatan biaya rekrutmen dan pelatihan, gangguan terhadap produktivitas, serta kehilangan pengalaman dan kompetensi karyawan.

Permasalahan yang perlu diselesaikan adalah:

1. Perusahaan belum memiliki gambaran berbasis data mengenai faktor-faktor yang berkaitan dengan tingginya employee attrition.
2. HR membutuhkan identifikasi kelompok karyawan dengan tingkat attrition yang relatif tinggi agar program retensi dapat diprioritaskan secara lebih tepat.
3. HR membutuhkan media monitoring yang dapat membantu melihat kondisi attrition berdasarkan berbagai karakteristik karyawan.
4. HR membutuhkan sistem peringatan awal untuk membantu mengidentifikasi karyawan yang memiliki risiko attrition lebih tinggi.

Jika permasalahan ini terus berlanjut tanpa adanya tindakan yang tepat, perusahaan berpotensi menghadapi peningkatan biaya penggantian karyawan, penurunan produktivitas, serta kesulitan dalam mempertahankan karyawan yang memiliki pengalaman dan kompetensi penting.

### Cakupan Proyek

Proyek ini mencakup:

1. Memahami karakteristik dataset employee attrition.
2. Melakukan data cleaning dan data preparation.
3. Melakukan exploratory data analysis untuk mengidentifikasi faktor yang berhubungan dengan attrition.
4. Membuat business dashboard menggunakan Metabase.
5. Membandingkan beberapa model machine learning untuk memprediksi employee attrition.
6. Memilih model berdasarkan metrik evaluasi yang relevan dengan kebutuhan early warning system.
7. Menyimpan model final untuk digunakan pada proses prediksi.
8. Membuat script `prediction.py` sebagai sistem prediksi sederhana.
9. Menyusun rekomendasi yang dapat digunakan HR sebagai dasar evaluasi strategi retensi.

### Persiapan

**Sumber data:** [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Dataset yang digunakan terdiri dari **1.470 baris dan 35 variabel**. Pada kolom `Attrition`, terdapat 1.058 baris yang memiliki label dan 412 baris dengan label kosong.

Data dengan nilai `Attrition` kosong tidak digunakan dalam proses analisis dan pemodelan karena status attrition sebenarnya tidak diketahui. Dengan demikian, proses analisis dan pemodelan dilakukan menggunakan **1.058 data karyawan berlabel**.

#### Setup Environment

Proyek ini dikembangkan menggunakan:

* Python: **[Python 3.11.9 `python --version`]**
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib

#### 1. Membuat Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

Aktifkan virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Jika menggunakan Command Prompt:

```cmd
.venv\Scripts\activate
```

Pastikan environment telah aktif sebelum melanjutkan ke tahap berikutnya.

#### 2. Install Dependency

Setelah virtual environment aktif, jalankan:

```bash
pip install -r requirements.txt
```

#### 3. Menjalankan Notebook

Notebook berisi seluruh proses data science mulai dari data understanding, data preparation, exploratory analysis, modeling, hingga evaluation.

Jalankan Jupyter Notebook menggunakan:

```bash
jupyter notebook
```

Kemudian buka:

```text
notebook.ipynb
```

#### 4. Menjalankan Dashboard Metabase

Dashboard dibuat menggunakan Metabase dan database SQLite.

Pastikan Docker Desktop sudah berjalan, kemudian jalankan:

```powershell
docker run -d -p 3000:3000 --name metabase -v "D:\submission:/data" metabase/metabase
```

Sesuaikan path `D:\submission` dengan lokasi folder project pada komputer yang digunakan.

Setelah container berjalan, buka:

```text
http://localhost:3000
```

Gunakan kredensial Metabase berikut:
- Username: root@mail.com
- Password: root123

Database yang digunakan oleh dashboard adalah:

```text
data/employee_attrition.db
```

Pada koneksi SQLite di Metabase, gunakan path:

```text
/data/data/employee_attrition.db
```

File database internal Metabase yang telah dikonfigurasi disertakan dalam submission:

```text
metabase.db.mv.db
```

#### 5. Menjalankan Sistem Prediksi

Model final disimpan pada:

```text
model/model.pkl
```

Script prediksi terdapat pada:

```text
prediction.py
```

Setelah virtual environment aktif dan dependency ter-install, jalankan:

```bash
python prediction.py
```

Script akan menggunakan contoh data karyawan yang telah didefinisikan di dalam file dan menghasilkan:

```text
Prediksi Attrition: 1
Probabilitas Attrition: 99.75%
```

## Business Dashboard

Business dashboard dibuat menggunakan **Metabase** untuk membantu departemen HR memonitor employee attrition berdasarkan berbagai karakteristik karyawan.

Dashboard menyediakan tiga KPI utama:

* Total karyawan
* Jumlah karyawan yang keluar
* Attrition rate

Dashboard juga menyediakan visualisasi:

* Attrition berdasarkan Overtime
* Attrition berdasarkan Job Role
* Attrition berdasarkan Masa Kerja
* Attrition berdasarkan Pendapatan
* Attrition berdasarkan Job Satisfaction
* Attrition berdasarkan Work-Life Balance
* Attrition berdasarkan Department
* Attrition berdasarkan Kelompok Usia

Dashboard dilengkapi dengan filter interaktif berdasarkan:

* Department
* Job Role
* Overtime

Filter digunakan untuk membantu HR melakukan eksplorasi kondisi attrition berdasarkan kelompok karyawan tertentu.

### Insight Utama Dashboard

Beberapa temuan utama dari dashboard adalah:

| Faktor            | Kelompok              | Attrition Rate |
| ----------------- | --------------------- | -------------: |
| Job Role          | Sales Representative  |         43,10% |
| Overtime          | Yes                   |         31,92% |
| Work-Life Balance | Level 1               |         32,14% |
| Masa Kerja        | 0–2 tahun             |         29,96% |
| Pendapatan        | Q1 - Terendah         |         29,06% |
| Job Role          | Laboratory Technician |         26,06% |
| Job Satisfaction  | Level 1               |         22,44% |
| Department        | Sales                 |         20,69% |

Dashboard juga dilengkapi dengan file database Metabase:

```text
metabase.db.mv.db
```

## Conclusion

Berdasarkan 1.058 data karyawan yang memiliki label `Attrition`, terdapat **179 karyawan yang mengalami attrition** dengan attrition rate sebesar **16,92%**. Angka tersebut berada di atas tingkat attrition 10% yang menjadi permasalahan perusahaan.

Hasil exploratory data analysis menunjukkan beberapa kelompok yang memiliki attrition rate relatif tinggi. Karyawan yang melakukan overtime memiliki attrition rate sebesar **31,92%**, dibandingkan 10,79% pada karyawan yang tidak melakukan overtime.

Dari sisi masa kerja, karyawan dengan masa kerja 0–2 tahun memiliki attrition rate sebesar **29,96%**. Kelompok pendapatan terendah juga memiliki attrition rate lebih tinggi, yaitu **29,06%**, dibandingkan 9,81% pada kelompok pendapatan tertinggi.

Berdasarkan job role, **Sales Representative** memiliki attrition rate tertinggi sebesar **43,10%**, diikuti oleh **Laboratory Technician** sebesar **26,06%**. Dari sisi kepuasan dan keseimbangan kerja, karyawan dengan Job Satisfaction level 1 memiliki attrition rate sebesar **22,44%**, sedangkan Work-Life Balance level 1 mencapai **32,14%**.

Untuk kebutuhan prediksi, tiga model dibandingkan, yaitu Logistic Regression, Random Forest, dan Logistic Regression dengan `class_weight="balanced"`.

| Model                          | Accuracy | Precision |     Recall | F1-Score | ROC-AUC |
| ------------------------------ | -------: | --------: | ---------: | -------: | ------: |
| Logistic Regression            |   88,21% |    72,00% |     50,00% |   59,02% |  82,23% |
| Random Forest                  |   84,91% |    83,33% |     13,89% |   23,81% |  80,13% |
| Logistic Regression (Balanced) |   73,11% |    36,00% | **75,00%** |   48,65% |  80,78% |

**Logistic Regression dengan `class_weight="balanced"` dipilih sebagai model final** karena menghasilkan Recall tertinggi sebesar **75,00%**. Pada data pengujian, model berhasil mengidentifikasi **27 dari 36 karyawan yang mengalami attrition**.

Model digunakan sebagai **early warning system** untuk membantu HR menentukan karyawan yang memerlukan perhatian lebih lanjut. Hasil prediksi tidak digunakan sebagai dasar pengambilan keputusan secara otomatis dan perlu dikombinasikan dengan evaluasi serta konteks dari pihak HR.

### Rekomendasi Action Items

1. **Mengevaluasi Overtime dan Beban Kerja**
   HR perlu melakukan monitoring overtime secara berkala dan mengevaluasi distribusi beban kerja pada tim dengan tingkat overtime tinggi. Jika diperlukan, perusahaan dapat melakukan redistribusi pekerjaan atau meninjau kebutuhan tenaga kerja.

2. **Memperkuat Program Retensi Karyawan Baru**
   Karena kelompok dengan masa kerja 0–2 tahun memiliki attrition rate sebesar 29,96%, perusahaan dapat memperkuat onboarding, mentoring, check-in berkala, serta memberikan informasi career path sejak awal masa kerja.

3. **Melakukan Evaluasi Kompensasi**
   Kelompok pendapatan terendah memiliki attrition rate sebesar 29,06%. HR dapat melakukan benchmarking kompensasi, mengevaluasi struktur kenaikan gaji, serta mengidentifikasi posisi yang memiliki kompensasi relatif rendah dan attrition tinggi.

4. **Menyusun Strategi Retensi berdasarkan Job Role**
   Sales Representative dan Laboratory Technician memiliki attrition rate relatif tinggi. HR dapat melakukan evaluasi beban kerja, kondisi kerja, career path, serta mengumpulkan employee feedback dan exit interview untuk memahami permasalahan yang lebih spesifik pada masing-masing role.

5. **Meningkatkan Job Satisfaction dan Work-life Balance**
   HR dapat melakukan employee pulse survey secara berkala, mengidentifikasi penyebab rendahnya kepuasan kerja, serta mengevaluasi fleksibilitas dan distribusi beban kerja.

6. **Menggunakan Model sebagai Early Warning System**
   Model dapat dijalankan secara berkala untuk membantu HR mengidentifikasi karyawan yang memiliki probabilitas attrition lebih tinggi. Hasil prediksi perlu digunakan sebagai bahan evaluasi awal, bukan sebagai keputusan otomatis terhadap karyawan.
