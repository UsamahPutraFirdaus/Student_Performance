# Menyelesaikan Permasalahan Institusi Pendidikan

# Business Understanding

Jaya Jaya Institut merupakan salah satu lembaga pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah berhasil mencetak banyak lulusan yang berkualitas dan memiliki reputasi yang sangat baik di dunia kerja maupun di kalangan akademisi. Reputasi tersebut menjadi salah satu kebanggaan utama bagi Jaya Jaya Institut.

Namun, di balik pencapaian tersebut, terdapat permasalahan serius yang turut menjadi perhatian, yaitu tingginya jumlah mahasiswa yang tidak berhasil menyelesaikan pendidikan mereka atau mengalami dropout. Fenomena ini tentu menjadi tantangan besar bagi institusi pendidikan karena berdampak langsung terhadap citra, kualitas, dan efektivitas penyelenggaraan pendidikan itu sendiri.

Menyadari hal tersebut, pihak Jaya Jaya Institut memiliki komitmen untuk menekan angka dropout dengan melakukan tindakan preventif. Salah satu langkah strategis yang ingin diambil adalah dengan mengidentifikasi secara dini para mahasiswa yang memiliki potensi untuk mengalami dropout. Dengan deteksi sejak awal ini, institusi berharap dapat memberikan bimbingan, dukungan, dan intervensi yang tepat sehingga para mahasiswa tersebut dapat tetap melanjutkan dan menyelesaikan pendidikan mereka dengan baik.

## Business Problem
1. Tingginya Tingkat Dropout Mahasiswa
   - Dampak:
     - Penurunan reputasi institusi.
     - Menurunnya kepercayaan calon mahasiswa dan orang tua.
  
2. Tidak Adanya Sistem Deteksi Dini Mahasiswa Berisiko Dropout
   - Dampak:
     - Upaya pencegahan tidak terarah dan kurang efektif.
     - Biaya pembinaan menjadi lebih besar karena tidak tepat sasaran.

## Project Scope
- **Dashboard Analytics** : Membuat dashboard analytics untuk memvisualisasikan performa mahasiswa untuk mendeteksi faktor-faktor yang bisa menunjukkan potensi risiko drop-out.
- **Model Machine Learning** : Membangun model machine learning yang akan digunakan untuk memprediksi mahasiswa `Graduate` atau `Dropout`
- **Sistem Prediksi** : Membangun sistem prediksi berbasis Streamlit yang akan digunakan oleh Admin Kampus atau Dosen untuk mendeteksi mahasiswa yang berisiko `Dropout`, sehingga pihak kampus bisa memberikan pembinaan tepat sasaran

## Preparation
### Data Source
Sumber Data : [Student Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

### Setup Environment
1. Clone this Repository
   ```
   git clone https://github.com/UsamahPutraFirdaus/Student_Performance
   ```
2. Create Python Virtual Environment
   ```
   virtualenv venv
   ```
3. Activate the Environment
   ```
   venv\Scripts\activate
   ```
4. Install All the Requirements Inside "requirements.txt"
   ```
   pip install -r requirements.txt
   ```

## Business Dashboard
[Jaya Jaya Institute Dashboard] dibuat secara optimal untuk menyediakan insight bagi para pengajar dan pihak internal institusi mengenai tingkat siswa dropout yang mencapai lebih dari 30%.

![img alt](https://github.com/UsamahPutraFirdaus/Student_Performance/blob/main/Usamah%20Putra%20Firdaus_Dashboard.png?raw=true)

Berikut adalah interpretasi dari hasil Dashboard yang telah dibuat:
1. Status
   - 40.9% telah lulus (Graduate)
   - 32.1% dropout
   - 17.0% masih aktif (Enrolled)

   Persentase dropout cukup tinggi (lebih dari 30%), ini menunjukkan adanya isu serius terkait keberlangsungan studi mahasiswa.

2. Gender
   - 64.9% mahasiswa adalah perempuan (2686)
   - 35.2% adalah laki-laki (1556)

   Mayoritas mahasiswa adalah perempuan.

3. Status by Gender
   - Perempuan lebih banyak yang lulus (1.661) dibanding laki-laki (548)
   - Jumlah dropout antara perempuan (720) dan laki-laki (701)
   - Jumlah mahasiswa aktif: perempuan (487) lebih banyak dari laki-laki (307)

   Meskipun jumlah mahasiswa perempuan lebih banyak secara keseluruhan, persentase mahasiswa laki-laki yang dropout jauh lebih tinggi (sekitar 45.1%) dibanding perempuan (26.8%). Ini menunjukkan bahwa mahasiswa laki-laki memiliki risiko dropout yang lebih tinggi.

4. Age at Enrolment
   - Usia paling umum saat pendaftaran adalah 18 dan 19 tahun
   - Setelah usia 20, jumlah mahasiswa menurun drastis

   Hal ini mungkin disebabkan umur 18-19 tahun, mereka baru lulus SMA kemudian langsung mendaftar Kuliah sehingga umur pendaftar paling banyak pada umur 18-19
    
5. Status by Scholarship
   - Mahasiswa berbeasiswa memiliki angka kelulusan yang tinggi (835 vs 1.374 tanpa beasiswa)
   - Jumlah dropout tanpa beasiswa jauh lebih tinggi (1.287) dibanding penerima beasiswa (134)

   Beasiswa tampaknya berperan penting dalam meningkatkan peluang kelulusan dan mengurangi dropout.

6. Status by Debtor
   - Mahasiswa tanpa utang mendominasi kelulusan (2.108)
   - Mahasiswa berutang memiliki dropout yang lebih tinggi (312 vs 1.109 yang tidak berutang)
   - Mahasiswa aktif juga didominasi oleh yang tidak berutang

   Secara jumlah, memang lebih banyak mahasiswa tanpa utang yang dropout (karena populasi mereka lebih besar), Namun, secara persentase, mahasiswa dengan utang memiliki tingkat dropout yang jauh lebih tinggi (62%) dibandingkan yang tidak berutang (28.3%).

7. Status by Course
   - Jurusan Nursing (Keperawatan) memiliki jumlah lulusan tertinggi (548)
   - Jurusan Manajemen menunjukkan dropout yang cukup tinggi

   Jurusan berpengaruh terhadap tingkat kelulusan dan dropout, bisa dianalisis lebih lanjut untuk mengetahui penyebab perbedaan ini.

### Machine Learning Prediction System
Untuk membantu institusi dalam memprediksi kemungkinan siswa mengalami dropout serta mencegahnya sejak dini, telah dikembangkan sebuah sistem prediksi. Sistem ini dibangun menggunakan Streamlit, dan untuk menjalankannya secara lokal, cukup gunakan perintah berikut di Terminal.

```
streamlit run streamlit_app.py
```

Dan untuk menghentikan program aplikasi Streamlit dapat melalui `ctrl + c`.

Sistem Prediksi juga dapat diakses secara online melalui link [berikut ini](https://studentperformanceprediction-usamahptrf.streamlit.app/)

## Conclusion
1. **Tingkat Dropout Masih Tinggi dan Perlu Perhatian Khusus** : Sekitar 32.1% mahasiswa mengalami dropout, yang merupakan angka cukup besar bagi institusi pendidikan, Ini menandakan perlunya strategi intervensi dini untuk mencegah peningkatan angka putus studi.
2. **Mahasiswa dengan Utang dan Tanpa Beasiswa Lebih Rentan Dropout** : Mahasiswa dengan utang memiliki tingkat dropout tertinggi (sekitar 62%) dibandingkan yang tidak berutang (28.3%), serta mahasiswa tanpa beasiswa menyumbang jumlah dropout jauh lebih besar dibanding penerima beasiswa. Artinya, faktor ekonomi sangat berpengaruh terhadap keberlangsungan studi mahasiswa.
3. **Mahasiswa Laki-Laki Lebih Berisiko Dropout Dibanding Perempuan** : Walaupun jumlah perempuan lebih banyak, persentase dropout laki-laki lebih tinggi (45.1%) dibanding perempuan (26.8%). Ini menunjukkan perlunya pendekatan khusus berbasis gender dalam bimbingan akademik dan psikososial.

## Recommended Action Items
1. **Terapkan Sistem Prediksi Dropout Berbasis Data**

   Implementasikan model machine learning untuk mendeteksi secara dini mahasiswa yang berisiko tinggi dropout. Integrasikan sistem ini dengan platform akademik internal agar dosen dan staf dapat melihat peringatan dini.

2. **Sediakan Program Dukungan Finansial yang Lebih Luas**

   Perluas akses terhadap beasiswa dan bantuan keuangan, terutama bagi mahasiswa yang berasal dari latar belakang ekonomi lemah atau memiliki utang pendidikan. Serta evaluasi dan monitor secara berkala dampak dari beasiswa terhadap performa akademik.

3. **Luncurkan Program Pendampingan Khusus untuk Mahasiswa Laki-Laki**

   Karena tingkat dropout laki-laki lebih tinggi, institusi dapat membuat program mentoring atau konseling khusus berbasis gender. Libatkan alumni laki-laki sukses sebagai pembimbing untuk meningkatkan motivasi dan keterikatan mahasiswa.

4. **Tindak Lanjut Proaktif oleh Tim Akademik dan Bimbingan**

   Bentuk tim monitoring akademik yang secara rutin meninjau data performa dan kehadiran mahasiswa. Lakukan pendekatan personal kepada mahasiswa berisiko, misalnya melalui sesi konseling atau bimbingan akademik tambahan.

5. **Evaluasi dan Optimalkan Kurikulum Jurusan dengan Dropout Tinggi**

   Lakukan audit akademik pada jurusan yang mencatat tingkat dropout tertinggi. Identifikasi beban studi, relevansi materi, atau metode pengajaran yang mungkin menjadi penyebab, lalu lakukan penyesuaian.
