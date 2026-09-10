# Employee Attrition Analysis & Prediction Jaya Jaya Maju

## Deskripsi

Proyek ini bertujuan untuk menganalisis faktor-faktor yang berhubungan dengan employee attrition pada perusahaan Jaya Jaya Maju serta membangun sistem peringatan awal untuk membantu departemen Human Resources (HR) mengidentifikasi karyawan yang memiliki risiko attrition lebih tinggi.

Project mencakup proses **data understanding, data preparation, exploratory analysis, modeling, evaluation, dan dashboard**.

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan. Perusahaan menghadapi permasalahan employee attrition dengan tingkat attrition lebih dari 10%.

Departemen HR membutuhkan analisis untuk memahami faktor-faktor yang berhubungan dengan attrition serta dashboard yang dapat membantu monitoring kondisi karyawan.

### Problem Statement

1. Faktor apa saja yang berhubungan dengan tingginya employee attrition?
2. Kelompok karyawan seperti apa yang memiliki tingkat attrition relatif tinggi?
3. Bagaimana hasil analisis dapat digunakan untuk membantu HR menyusun strategi retensi?
4. Bagaimana model machine learning dapat digunakan sebagai early warning system untuk mengidentifikasi karyawan yang berpotensi mengalami attrition?

### Goals

1. Mengidentifikasi faktor-faktor yang berhubungan dengan employee attrition.
2. Menyediakan dashboard interaktif untuk membantu HR memonitor attrition.
3. Menghasilkan rekomendasi yang dapat ditindaklanjuti berdasarkan hasil analisis.
4. Membangun model machine learning untuk memprediksi potensi attrition.

## Dataset

Dataset terdiri dari **1.470 data karyawan dengan 35 variabel**.

Pada kolom `Attrition`, terdapat:

* **1.058 data** dengan label attrition.
* **412 data** dengan label `Attrition` yang kosong.

Data dengan target `Attrition` yang kosong tidak digunakan dalam proses analisis dan pemodelan karena status attrition sebenarnya tidak diketahui.

Setelah proses data preparation, digunakan **1.058 data karyawan** untuk analisis dan pemodelan.

## Data Preparation

Tahapan data preparation meliputi:

1. Menghapus baris dengan nilai `Attrition` yang kosong.
2. Menghapus kolom identifier dan kolom konstan yang tidak relevan untuk pemodelan:

   * `EmployeeId`
   * `EmployeeCount`
   * `Over18`
   * `StandardHours`
3. Memisahkan fitur dan target.
4. Membagi data menjadi training dan testing menggunakan stratified split dengan proporsi 80:20.
5. Melakukan One-Hot Encoding pada variabel kategorikal.
6. Melakukan standardisasi pada variabel numerik.

## Exploratory Data Analysis

Hasil analisis menunjukkan beberapa kelompok dengan tingkat attrition yang relatif tinggi:

| Faktor            | Kelompok              | Attrition Rate |
| ----------------- | --------------------- | -------------: |
| Overtime          | Yes                   |         31,92% |
| Job Role          | Sales Representative  |         43,10% |
| Job Role          | Laboratory Technician |         26,06% |
| Masa Kerja        | 0–2 tahun             |         29,96% |
| Pendapatan        | Q1 - Terendah         |         29,06% |
| Job Satisfaction  | Level 1               |         22,44% |
| Work-Life Balance | Level 1               |         32,14% |
| Department        | Sales                 |         20,69% |

Hasil tersebut digunakan sebagai dasar dalam penyusunan rekomendasi untuk HR.

## Dashboard

Dashboard dibuat menggunakan **Metabase** dan menyediakan visualisasi untuk membantu HR memahami kondisi attrition.

Dashboard mencakup:

* Total karyawan
* Jumlah karyawan yang keluar
* Attrition rate
* Attrition berdasarkan overtime
* Attrition berdasarkan job role
* Attrition berdasarkan masa kerja
* Attrition berdasarkan pendapatan
* Attrition berdasarkan job satisfaction
* Attrition berdasarkan work-life balance
* Attrition berdasarkan department
* Attrition berdasarkan kelompok usia

Dashboard juga menyediakan filter interaktif berdasarkan **Department, Job Role, dan Overtime**.

## Modeling

Tiga model dibandingkan:

1. Logistic Regression
2. Random Forest
3. Logistic Regression dengan `class_weight="balanced"`

Karena dataset memiliki ketidakseimbangan kelas, Recall menjadi salah satu metrik utama dalam pemilihan model.

### Hasil Evaluasi

| Model                          | Accuracy | Precision |     Recall | F1-Score | ROC-AUC |
| ------------------------------ | -------: | --------: | ---------: | -------: | ------: |
| Logistic Regression            |   88,21% |    72,00% |     50,00% |   59,02% |  82,23% |
| Random Forest                  |   84,91% |    83,33% |     13,89% |   23,81% |  80,13% |
| Logistic Regression (Balanced) |   73,11% |    36,00% | **75,00%** |   48,65% |  80,78% |

### Model Final

**Logistic Regression dengan `class_weight="balanced"` dipilih sebagai model final** karena menghasilkan Recall tertinggi sebesar **75%**.

Model mampu mengidentifikasi **27 dari 36 karyawan yang mengalami attrition** pada data pengujian.

Model digunakan sebagai **early warning system**, bukan sebagai dasar pengambilan keputusan HR secara otomatis.

## Action Items / Recommendations

Berdasarkan hasil analisis attrition, terdapat beberapa faktor yang memiliki hubungan dengan tingginya tingkat karyawan yang meninggalkan perusahaan. Beberapa rekomendasi yang dapat dilakukan oleh departemen Human Resources adalah sebagai berikut.

### 1. Mengevaluasi beban kerja dan overtime

Karyawan yang melakukan overtime memiliki attrition rate sebesar **31,92%**, lebih tinggi dibandingkan karyawan yang tidak melakukan overtime sebesar **10,79%**.

**Action:**

* Melakukan evaluasi distribusi beban kerja pada tim dengan tingkat overtime tinggi.
* Meninjau kebutuhan penambahan tenaga kerja atau redistribusi pekerjaan.
* Melakukan monitoring overtime secara berkala untuk mengidentifikasi tim yang mengalami beban kerja berlebih.

### 2. Memperkuat program retensi pada karyawan baru

Karyawan dengan masa kerja **0–2 tahun** memiliki attrition rate sebesar **29,96%**, menjadi kelompok masa kerja dengan tingkat attrition tertinggi.

**Action:**

* Memperkuat program onboarding dan mentoring bagi karyawan baru.
* Melakukan check-in secara berkala selama tahun pertama dan kedua.
* Menyediakan jalur pengembangan karier yang lebih jelas sejak awal masa kerja.

### 3. Melakukan evaluasi kompensasi pada kelompok pendapatan rendah

Kelompok pendapatan terendah (Q1) memiliki attrition rate sebesar **29,06%**, sedangkan kelompok pendapatan tertinggi (Q4) sebesar **9,81%**.

**Action:**

* Melakukan benchmarking kompensasi terhadap posisi yang sejenis.
* Mengevaluasi struktur kenaikan gaji dan peluang peningkatan pendapatan.
* Mengidentifikasi posisi dengan kompensasi relatif rendah tetapi memiliki tingkat attrition tinggi.

### 4. Menyusun strategi retensi berdasarkan job role

Beberapa job role memiliki attrition rate yang relatif tinggi, terutama **Sales Representative (43,10%)** dan **Laboratory Technician (26,06%)**.

**Action:**

* Melakukan evaluasi beban kerja dan kondisi kerja pada role dengan attrition tinggi.
* Mengidentifikasi hambatan yang dihadapi karyawan melalui employee feedback atau exit interview.
* Menyediakan program pengembangan kompetensi dan career path yang relevan dengan masing-masing role.

### 5. Meningkatkan employee satisfaction dan work-life balance

Karyawan dengan tingkat **Job Satisfaction 1** memiliki attrition rate sebesar **22,44%**, sedangkan karyawan dengan Work-Life Balance level 1 memiliki attrition rate sebesar **32,14%**.

**Action:**

* Melakukan employee pulse survey secara berkala.
* Mengidentifikasi faktor utama yang menyebabkan rendahnya kepuasan kerja.
* Mengevaluasi fleksibilitas kerja dan distribusi beban kerja.
* Menindaklanjuti hasil survei dengan program perbaikan yang terukur.

### Pemanfaatan Model Prediksi

Model Logistic Regression dengan `class_weight="balanced"` dapat digunakan sebagai **early warning system** untuk membantu HR mengidentifikasi karyawan yang memiliki probabilitas attrition lebih tinggi.

Model menghasilkan **Recall sebesar 75%**, sehingga mampu mengidentifikasi 27 dari 36 karyawan yang mengalami attrition pada data pengujian.

Namun, hasil prediksi **tidak digunakan sebagai dasar pengambilan keputusan secara otomatis**. Prediksi perlu digunakan sebagai bahan pertimbangan awal dan dikombinasikan dengan evaluasi kondisi karyawan oleh pihak HR.

### Prioritas Implementasi

Berdasarkan hasil analisis, prioritas awal yang dapat dilakukan adalah:

1. **Evaluasi overtime dan beban kerja**
2. **Program retensi karyawan dengan masa kerja 0–2 tahun**
3. **Evaluasi kompensasi kelompok pendapatan rendah**
4. **Strategi retensi pada job role dengan attrition tinggi**
5. **Peningkatan job satisfaction dan work-life balance**

## Deployment

Model yang telah dilatih disimpan dalam:

```text
model/model.pkl
```

Prediksi dapat dilakukan menggunakan:

```text
prediction.py
```

Contoh menjalankan program:

```bash
python prediction.py
```

Program menerima data satu karyawan dan menghasilkan:

* `prediction`: prediksi attrition (`0` atau `1`)
* `probability`: probabilitas karyawan mengalami attrition

## Struktur Project

```text
jayajayamaju-departemen-HR/
├── model/
│   └── model.pkl
├── employee_attrition.db
├── employee_data.csv
├── metabase.db.mv.db
├── notebook.ipynb
├── pppiiiy_dicoding-dashboard.png
├── prediction.py
├── README.md
└── requirements.txt
```

## Teknologi yang Digunakan

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* SQLite
* Metabase
* Docker

## Cara Menjalankan

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Menjalankan prediction

Pastikan file model tersedia di:

```text
model/model.pkl
```

Kemudian jalankan:

```bash
python prediction.py
```

### 3. Dashboard

Untuk mengakses dashboard, gunakan kredensial berikut:
- **Username:** `root@mail.com`
- **Password:** `root123`

File database Metabase disertakan dalam submission.

## Catatan

Hasil analisis menunjukkan hubungan antara karakteristik karyawan dan attrition, tetapi **tidak dapat diinterpretasikan sebagai hubungan sebab-akibat**.

Prediksi model juga tidak dimaksudkan untuk mengambil keputusan otomatis terhadap karyawan. Hasil prediksi perlu dikombinasikan dengan evaluasi dan pertimbangan dari pihak HR.