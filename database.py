import mysql.connector

# Fungsi untuk mengonversi nilai menjadi nilai sesuai dengan rangking
def convert_to_ranking(value, ranking_dict):
    if isinstance(value, str):  # Check if the value is a string
        return ranking_dict.get(value, None)
    elif isinstance(value, int):  # Check if the value is an integer
        return value
    else:
        return None


# Fungsi untuk menyimpan data ke dalam database
def save_data(nama_channel, jumlah_subscriber, jadwal_tayang, kualitas_konten, durasi_video, interaksi_penonton):
    # Membuat koneksi
 
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='spk')


    # Membuat cursor
    cursor = cnx.cursor()

    # Menyiapkan query SQL
    query = ("INSERT INTO channel "
             "(nama_channel, jumlah_subscriber, jadwal_tayang, kualitas_konten, durasi_video, interaksi_penonton) "
             "VALUES (%s, %s, %s, %s, %s, %s)")

    # Membuat dictionary untuk mapping nilai ke rangking
    ranking_dict = {
        'jumlah_subscriber': {'<500.000': 1, '600.000-1.000.000': 2, '2.000.000–5.000.000': 3, '6.000.000–9.000.000': 4, '>10.000.000': 5},
        'jadwal_tayang': {'Jarang (1-4 kali per bulan)': 1, '(1 kali per minggu)': 2, '(2 kali per minggu)': 3, '(>3 kali per minggu)': 4},
        'kualitas_konten': {'Rendah': 2, 'Menengah': 3, 'Tinggi': 4, 'Sangat Tinggi': 5},
        'durasi_video': {'Pendek (kurang dari 20 menit)': 2, 'Sedang (30 menit – 1 jam)': 3, 'Panjang (lebih dari 1 jam)': 4},
        'interaksi_penonton': {'Rendah': 2, 'Menengah': 3, 'Tinggi': 4}
    }

    # Mengonversi nilai string menjadi nilai berdasarkan rangking
    jumlah_subscriber_rank = convert_to_ranking(jumlah_subscriber, ranking_dict['jumlah_subscriber'])
    jadwal_tayang_rank = convert_to_ranking(jadwal_tayang, ranking_dict['jadwal_tayang'])
    kualitas_konten_rank = convert_to_ranking(kualitas_konten, ranking_dict['kualitas_konten'])
    durasi_video_rank = convert_to_ranking(durasi_video, ranking_dict['durasi_video'])
    interaksi_penonton_rank = convert_to_ranking(interaksi_penonton, ranking_dict['interaksi_penonton'])

    # Menjalankan query SQL
    cursor.execute(query, (nama_channel, jumlah_subscriber_rank, jadwal_tayang_rank, kualitas_konten_rank, durasi_video_rank, interaksi_penonton_rank))

    # Commit perubahan
    cnx.commit()

    # Menutup cursor dan koneksi
    cursor.close()
    cnx.close()
    
def get_data():
    # Membuat koneksi
    cnx = mysql.connector.connect(user='root', 
                                  password='',
                                  host='localhost',
                                  database='spk')

    # Membuat cursor
    cursor = cnx.cursor()

    # Menyiapkan query SQL
    query = ("SELECT nama_channel, jumlah_subscriber, jadwal_tayang, kualitas_konten, durasi_video, interaksi_penonton FROM channel")

    # Menjalankan query SQL
    cursor.execute(query)

    # Mengambil semua baris dari hasil query
    rows = cursor.fetchall()

    # Menutup cursor dan koneksi
    cursor.close()
    cnx.close()

    return rows

def update_data(nama_channel, jumlah_subscriber, jadwal_tayang, kualitas_konten, durasi_video, interaksi_penonton):
    # Membuat koneksi
    cnx = mysql.connector.connect(user='root', 
                                  password='',
                                  host='localhost',
                                  database='spk')

    # Membuat cursor
    cursor = cnx.cursor()

    # Menyiapkan query SQL
    query = ("UPDATE channel SET jumlah_subscriber = %s, jadwal_tayang = %s, kualitas_konten = %s, durasi_video = %s, interaksi_penonton = %s WHERE nama_channel = %s")

    # Menjalankan query SQL
    cursor.execute(query, (jumlah_subscriber, jadwal_tayang, kualitas_konten, durasi_video, interaksi_penonton, nama_channel))

    # Commit perubahan
    cnx.commit()

    # Menutup cursor dan koneksi
    cursor.close()
    cnx.close()
    
def get_all_channels():
    # Membuat koneksi
    cnx = mysql.connector.connect(user='root', 
                                  password='',
                                  host='localhost',
                                  database='spk')

    # Membuat cursor
    cursor = cnx.cursor()

    # Menyiapkan query SQL
    query = ("SELECT nama_channel FROM channel")

    # Menjalankan query SQL
    cursor.execute(query)

    # Mengambil semua baris dari hasil query
    rows = cursor.fetchall()

    # Menutup cursor dan koneksi
    cursor.close()
    cnx.close()

    # Mengembalikan semua nama channel
    return [row[0] for row in rows]

def delete_data(nama_channel):
    # Membuat koneksi
    cnx = mysql.connector.connect(user='root', 
                                  password='',
                                  host='localhost',
                                  database='spk')

    # Membuat cursor
    cursor = cnx.cursor()

    # Menyiapkan query SQL
    query = ("DELETE FROM channel WHERE nama_channel = %s")

    # Menjalankan query SQL
    cursor.execute(query, (nama_channel,))

    # Commit perubahan
    cnx.commit()

    # Menutup cursor dan koneksi
    cursor.close()
    cnx.close()
    
def get_all_data():
    # Membuat koneksi
    cnx = mysql.connector.connect(user='root',
                                  password='',
                                  host='localhost',
                                  database='spk')

    # Membuat cursor
    cursor = cnx.cursor()

    # Menyiapkan query SQL
    query = ("SELECT * FROM channel")

    # Menjalankan query SQL
    cursor.execute(query)

    # Mengambil semua baris dari hasil query
    rows = cursor.fetchall()

    # Menutup cursor dan koneksi
    cursor.close()
    cnx.close()

    # Mengembalikan semua data
    return rows



