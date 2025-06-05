import datetime
import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
import io

buffer = io.BytesIO()

def data_preprocessing(data_input, single_data, n):
    df = pd.read_csv('student_data_final.csv')
    df = df.drop(columns=['Status'], axis=1)
    df = pd.concat([data_input, df])
    df = StandardScaler().fit_transform(df)

    if single_data:
        return df[[n]]
    else:
        return df[0 : n]

def model_predict(df):
    model = joblib.load('model_rf.joblib')
    return model.predict(df)

def color_mapping(value):
    color = 'green' if value == 'Graduate' else 'red'
    return f'color: {color}'

def main():
    st.title('Student Performance Prediction - Jaya Jaya Institute')

    gender_mapping = {
        'Male': 1,
        'Female': 0
    }

    marital_status_mapping = {
        'Single': 1,
        'Married': 2,
        'Widower': 3,
        'Divorced': 4,
        'Facto Union': 5,
        'Legally Seperated': 6
    }

    application_mapping = {
        '1st Phase - General Contingent': 1,
        '1st Phase - Special Contingent (Azores Island)': 5,
        '1st Phase - Special Contingent (Madeira Island)': 16,
        '2nd Phase - General Contingent': 17,
        '3rd Phase - General Contingent': 18,
        'Ordinance No. 612/93': 2,
        'Ordinance No. 854-B/99': 10,
        'Ordinance No. 533-A/99, Item B2 (Different Plan)': 26,
        'Ordinance No. 533-A/99, Item B3 (Other Institution)': 27,
        'International Student (Bachelor)': 15,
        'Over 23 Years Old': 39,
        'Transfer': 42,
        'Change of Course': 43,
        'Holders of Other Higher Courses': 7,
        'Short Cycle Diploma Holders': 53,
        'Technological Specialization Diploma Holders': 44,
        'Change of Institution/Course': 51,
        'Change of Institution/Course (International)': 57,
    }

    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)

        # BLOK 1: Informasi Umum
        st.subheader('📋 Informasi Umum Mahasiswa')
        col_gender, col_age, col_marital = st.columns([2, 2, 3])
        with col_gender:
            gender = st.radio('Jenis Kelamin', options=['Male', 'Female'],
                help='Jenis kelamin mahasiswa')
        with col_age:
            age = st.number_input('Usia Saat Pendaftaran', min_value=18, max_value=70,
                help='Usia mahasiswa saat mendaftar')
        with col_marital:
            marital_status = st.selectbox('Status Pernikahan', ('Single', 'Married',
                'Widower', 'Divorced', 'Facto Union', 'Legally Seperated'),
                help='Status pernikahan mahasiswa')

        st.divider()

        # BLOK 2: Pendaftaran dan Nilai Masuk
        st.subheader('📝 Informasi Pendaftaran')
        col_application, col_prev_grade, col_admission_grade = st.columns([3, 1.65, 1.1])
        with col_application:
            application_mode = st.selectbox('Metode Pendaftaran', list(application_mapping.keys()),
                help='Metode pendaftaran yang digunakan oleh mahasiswa')
        with col_prev_grade:
            prev_qualification_grade = st.number_input('Nilai Kualifikasi Sebelumnya',
                help='Nilai kualifikasi pendidikan sebelumnya (0-200)', min_value=0, max_value=200)
        with col_admission_grade:
            admission_grade = st.number_input('Nilai Penerimaan',
                help='Nilai penerimaan mahasiswa (0-200)', min_value=0, max_value=200)

        st.divider()

        # BLOK 3: Kondisi Keuangan dan Sosial
        st.subheader('💰 Kondisi Keuangan & Sosial')
        col_scholarship, col_tuition = st.columns(2)
        with col_scholarship:
            scholarship_holder = 1 if st.checkbox(
                'Beasiswa', help='Apakah mahasiswa menerima beasiswa') else 0
        with col_tuition:
            tuition_fees = 1 if st.checkbox(
                'Uang Kuliah Lunas', help='Apakah uang kuliah mahasiswa sudah dibayar lunas') else 0

        col_displaced, col_debtor = st.columns(2)
        with col_displaced:
            displaced = 1 if st.checkbox(
                'Terdampak', help='Apakah mahasiswa adalah orang yang terdampak (displaced)') else 0
        with col_debtor:
            debtor = 1 if st.checkbox(
                'Memiliki Tunggakan', help='Apakah mahasiswa memiliki tunggakan') else 0

        st.divider()

        # BLOK 4: Aktivitas Akademik
        st.subheader('📚 Aktivitas Akademik')
        col_1_enroll, col_2_enroll, col_2_eval = st.columns([1, 1, 1.2])
        with col_1_enroll:
            curricular_units_1st_sem_enrolled = st.number_input(
                'Mata Kuliah Semester 1 Diambil', min_value=0, max_value=26,
                help='Jumlah mata kuliah yang diambil mahasiswa pada semester 1 (0-26)')
        with col_2_enroll:
            curricular_units_2nd_sem_enrolled = st.number_input(
                'Mata Kuliah Semester 2 Diambil', min_value=0, max_value=23,
                help='Jumlah mata kuliah yang diambil mahasiswa pada semester 2 (0-23)')
        with col_2_eval:
            curricular_units_2nd_sem_evaluations = st.number_input(
                'Evaluasi Semester 2', min_value=0, max_value=33,
                help='Jumlah evaluasi mata kuliah pada semester 2 (0-33)')

        col_1_approved, col_2_approved, col_2_noeval = st.columns([1, 1, 1.2])
        with col_1_approved:
            curricular_units_1st_sem_approved = st.number_input(
                'Lulus Semester 1', min_value=0, max_value=26,
                help='Jumlah mata kuliah yang lulus pada semester 1 (0-26)')
        with col_2_approved:
            curricular_units_2nd_sem_approved = st.number_input(
                'Lulus Semester 2', min_value=0, max_value=20,
                help='Jumlah mata kuliah yang lulus pada semester 2 (0-20)')
        with col_2_noeval:
            curricular_units_2nd_sem_without_evaluations = st.number_input(
                'Tidak Dievaluasi Semester 2', min_value=0, max_value=12,
                help='Jumlah mata kuliah yang tidak dievaluasi pada semester 2 (0-12)')

        col_1_grade, col_2_grade, col_2_empty = st.columns([1, 1, 1.2])
        with col_1_grade:
            curricular_units_1st_sem_grade = st.number_input(
                'Rata-rata Nilai Semester 1', min_value=0, max_value=20,
                help='Nilai rata-rata mata kuliah semester 1 (0-20)')
        with col_2_grade:
            curricular_units_2nd_sem_grade = st.number_input(
                'Rata-rata Nilai Semester 2', min_value=0, max_value=20,
                help='Nilai rata-rata mata kuliah semester 2 (0-20)')

        st.markdown('</div>', unsafe_allow_html=True)


    gender = gender_mapping.get(gender)
    marital_status = marital_status_mapping.get(marital_status)
    application_mode = application_mapping.get(application_mode)

    data = [[marital_status, application_mode, prev_qualification_grade,
            admission_grade, displaced, debtor, tuition_fees,
            gender, scholarship_holder, age,
            curricular_units_1st_sem_enrolled,
            curricular_units_1st_sem_approved, curricular_units_1st_sem_grade,
            curricular_units_2nd_sem_enrolled,
            curricular_units_2nd_sem_evaluations,
            curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade,
            curricular_units_2nd_sem_without_evaluations]]

    df = pd.DataFrame(data, columns=[
        'Marital_status', 'Application_mode', 'Previous_qualification_grade',
        'Admission_grade', 'Displaced', 'Debtor', 'Tuition_fees_up_to_date',
        'Gender', 'Scholarship_holder', 'Age_at_enrollment',
        'Curricular_units_1st_sem_enrolled',
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
        'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations',
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
        'Curricular_units_2nd_sem_without_evaluations'])

    @st.dialog('Hasil Prediksi')
    def prediction(output):
        if output == 1:
            st.success('Prediksi Status Mahasiswa: **Lulus (Graduate)**')
        else:
            st.error('Prediksi Status Mahasiswa: **Dropout (Keluar)**')

    if st.button('✨ Prediksi'):
        data_input = data_preprocessing(df, True, 0)
        output = model_predict(data_input)
        prediction(output)

        st.write('')
        st.write('')

        name = "Usamah Putra Firdaus"
        copyright = 'Hak Cipta © 2025 ' + name
        st.caption(copyright)

if __name__ == '__main__':
    main()
