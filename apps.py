import streamlit as st
from database import save_data, get_data, update_data, get_all_channels, delete_data, get_all_data
import pandas as pd
import numpy as np

# Fungsi untuk mengonversi nilai menjadi nilai sesuai dengan rangking
def convert_to_ranking(value, ranking_dict):
    if isinstance(value, str):  # Check if the value is a string
        return ranking_dict.get(value, None)
    elif isinstance(value, int):  # Check if the value is an integer
        return value
    else:
        return None

# Fungsi untuk menghitung TOPSIS
def calculate_topsis(df):
    # Tambahkan kode untuk menghitung TOPSIS di sini
    pass

# Sidebar
menu = st.sidebar.selectbox('Menu', ['Overview', 'Create', 'Read', 'Update', 'Delete', 'Ranking'])

if menu == 'Overview':
    st.title('Overview')
    # Tambahkan konten overview Anda di sini

elif menu == 'Create':
    st.title('Create')

    # Nama Channel
    nama_channel = st.text_input('Nama Channel', '')

    # Jumlah Subscriber
    jumlah_subscriber = st.radio('Jumlah Subscriber', ['<500.000', '600.000-1.000.000', '2.000.000–5.000.000', '6.000.000–9.000.000', '>10.000.000'])

    # Jadwal tayang perminggu
    jadwal_tayang = st.radio('Jadwal Tayang per Minggu', ['Jarang (1-4 kali per bulan)', '(1 kali per minggu)', '(2 kali per minggu)', '(>3 kali per minggu)'])

    # Kualitas konten
    kualitas_konten = st.radio('Kualitas Konten', ['Rendah', 'Menengah', 'Tinggi', 'Sangat Tinggi'])

    # Durasi Video
    durasi_video = st.radio('Durasi Video', ['Pendek (kurang dari 20 menit)', 'Sedang (30 menit – 1 jam)', 'Panjang (lebih dari 1 jam)'])

    # Interaksi dengan penonton
    interaksi_penonton = st.radio('Interaksi dengan Penonton', ['Rendah', 'Menengah', 'Tinggi'])

    if st.button('Submit'):
        # Mengonversi nilai input menjadi nilai sesuai dengan rangking
        jumlah_subscriber_rank = convert_to_ranking(jumlah_subscriber, {'<500.000': 1, '600.000-1.000.000': 2, '2.000.000–5.000.000': 3, '6.000.000–9.000.000': 4, '>10.000.000': 5})
        jadwal_tayang_rank = convert_to_ranking(jadwal_tayang, {'Jarang (1-4 kali per bulan)': 1, '(1 kali per minggu)': 2, '(2 kali per minggu)': 3, '(>3 kali per minggu)': 4})
        kualitas_konten_rank = convert_to_ranking(kualitas_konten, {'Rendah': 2, 'Menengah': 3, 'Tinggi': 4, 'Sangat Tinggi': 5})
        durasi_video_rank = convert_to_ranking(durasi_video, {'Pendek (kurang dari 20 menit)': 2, 'Sedang (30 menit – 1 jam)': 3, 'Panjang (lebih dari 1 jam)': 4})
        interaksi_penonton_rank = convert_to_ranking(interaksi_penonton, {'Rendah': 2, 'Menengah': 3, 'Tinggi': 4})

        # Menyimpan data ke dalam database
        save_data(nama_channel, jumlah_subscriber_rank, jadwal_tayang_rank, kualitas_konten_rank, durasi_video_rank, interaksi_penonton_rank)
        st.success('Data berhasil disimpan.')

elif menu == 'Read':
    st.title('Read')

    # Mengambil data dari database
    data = get_data()

    # Mengubah data menjadi DataFrame pandas
    df = pd.DataFrame(data, columns=['nama_channel', 'jumlah_subscriber', 'jadwal_tayang', 'kualitas_konten', 'durasi_video', 'interaksi_penonton'])

    # Menampilkan data dalam bentuk tabel
    st.table(df)

elif menu == 'Update':
    st.title('Update')

    # Mengambil semua nama channel dari database
    all_channels = get_all_channels()

    # Membuat dropdown untuk memilih nama channel
    selected_channel = st.selectbox('Pilih Channel', all_channels)

    # Jumlah Subscriber
    jumlah_subscriber = st.radio('Jumlah Subscriber', ['<500 ribu', '600 rb - 1 jt', '2 – 5 jt', '6 – 9 jt', '>10 juta'])

    # Jadwal tayang perminggu
    jadwal_tayang = st.radio('Jadwal Tayang per Minggu', ['Jarang (1-4 kali per bulan)', '(1 kali per minggu)', '(2 kali per minggu)', '(>3 kali per minggu)'])

    # Kualitas konten
    kualitas_konten = st.radio('Kualitas Konten', ['Rendah', 'Menengah', 'Tinggi', 'Sangat Tinggi'])

    # Durasi Video
    durasi_video = st.radio('Durasi Video', ['Pendek (kurang dari 20 menit)', 'Sedang (30 menit – 1 jam)', 'Panjang (lebih dari 1 jam)'])

    # Interaksi dengan penonton
    interaksi_penonton = st.radio('Interaksi dengan Penonton', ['Rendah', 'Menengah', 'Tinggi'])

    if st.button('Update'):
        update_data(selected_channel, jumlah_subscriber, jadwal_tayang, kualitas_konten, durasi_video, interaksi_penonton)
        st.success('Data berhasil diperbarui.')

elif menu == 'Delete':
    st.title('Delete')

    # Mengambil semua data dari database
    data = get_data()

    # Mengubah data menjadi DataFrame pandas
    df = pd.DataFrame(data, columns=['nama_channel', 'jumlah_subscriber', 'jadwal_tayang', 'kualitas_konten', 'durasi_video', 'interaksi_penonton'])
    # Menampilkan data dalam bentuk tabel dengan tombol delete
    for index, row in df.iterrows():
        st.write(row)
        if st.button('Delete', key=row['nama_channel']):
            delete_data(row['nama_channel'])
            st.success('Data berhasil dihapus.')


elif menu == 'Ranking':
    st.title('Ranking')

    # Mengambil semua data dari database
    all_data = get_all_data()

    # Mengubah data menjadi DataFrame pandas
    df = pd.DataFrame(all_data, columns=['id', 'nama_channel', 'jumlah_subscriber', 'jadwal_tayang', 'kualitas_konten', 'durasi_video', 'interaksi_penonton'])

    # Menampilkan data dalam bentuk tabel
    st.table(df)
    
    st.title('Menentukan rangking tiap alternatif')
    
    def calculate_ranking(df, column):
        # Mengambil data kolom
        data = df[column].values

        # Mengubah data menjadi numerik
        data = pd.to_numeric(data, errors='coerce')

        # Menghitung |x|
        x = np.sqrt(np.sum(np.square(data)))

        # Menghitung r_ij untuk setiap i
        r_ij = data / x

        return r_ij


    # Menghitung rangking untuk setiap kolom
    for column in df.columns:
        if column != 'nama_channel':  # Tidak menghitung rangking untuk kolom 'nama_channel'
            df[column] = calculate_ranking(df, column)

    # Menampilkan DataFrame
    st.table(df)
    
    st.title('Menghitung matriks keputusan ternormalisasi terbobot')
    
    # Bobot untuk setiap kriteria
    bobot = {
        'jumlah_subscriber': 5,
        'jadwal_tayang': 4,
        'kualitas_konten': 4,
        'durasi_video': 3,
        'interaksi_penonton': 3
    }

    # Menghitung Matriks Keputusan Ternormalisasi Terbobot
    for column in bobot.keys():
        df[column] = df[column] * bobot[column]

    # Menampilkan DataFrame
    st.table(df)
    
    
    st.title('Menghitung solusi ideal positif dan negatif')
    
    # Menghitung Solusi Ideal Positif (A+)
    a_plus = df.max(numeric_only=True)

    # Menghitung Solusi Ideal Negatif (A-)
    a_minus = df.min(numeric_only=True)
    
    # Membuat DataFrame baru untuk Solusi Ideal Positif (A+) dan Solusi Ideal Negatif (A-)
    ideal_solutions = pd.DataFrame({
        'A+ (Max)': a_plus,
        'A- (Min)': a_minus
    })

    # Menampilkan DataFrame
    st.table(ideal_solutions)
    
    st.title('Menghitung jarak antara nilai terbobot setiap alternatif dengan A+ dan A-')
    
    # Menghitung jarak antara nilai terbobot setiap alternatif dengan A+
    df['D+'] = np.sqrt(((df.drop(columns=['nama_channel']) - a_plus) ** 2).sum(axis=1))

    # Menghitung jarak antara nilai terbobot setiap alternatif dengan A-
    df['D-'] = np.sqrt(((df.drop(columns=['nama_channel']) - a_minus) ** 2).sum(axis=1))
    
    st.table(df)
    
    st.title('Menghitung kedekatan setiap alternatif terhadap solusi ideal (V)')
    
    # Menghitung kedekatan setiap alternatif terhadap solusi ideal (V)
    df['V'] = df['D-'] / (df['D+'] + df['D-'])
    
    st.table(df)
    
    st.title('Perangkingan')
    
    # Menentukan peringkat berdasarkan nilai V
    df['Ranking'] = df['V'].rank(method='min', ascending=False)
    # Mengurutkan DataFrame berdasarkan peringkat
    df_sorted = df.sort_values('Ranking')
    
    df_ranking = df_sorted[['nama_channel', 'Ranking']]
    df_ranking['Ranking'] = df_ranking['Ranking'].astype(int)
    
    st.table(df_ranking)
