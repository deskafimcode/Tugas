import requests
from bs4 import BeautifulSoup
import csv
import json

# 1. REQUEST - kirim request ke website
url = "http://143.198.223.28:5000/secret-data"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    print("Mengirim request ke PokemonDB")
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    print(f"Response: {response.status_code} OK\n")

    # 2. PARSING - ubah HTML jadi objek BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', id='pokedex')

    if not table:
        print("Tabel 'pokedex' tidak ditemukan, struktur web mungkin berubah.")
        exit()

    # 3. EKSTRAKSI - ambil data dari setiap baris tabel
    rows = table.find('tbody').find_all('tr')
    pokemon_data = []

    for row in rows:
        cols = row.find_all('td')
        name = cols[1].find('a').text
        types = ", ".join([t.text for t in cols[2].find_all('a')])
        total_stat = int(cols[3].text)

        pokemon_data.append({
            "Nama": name,
            "Tipe": types,
            "Total_Stat": total_stat
        })
        print(f"  Diekstrak: {name}")

    if not pokemon_data:
        print("Tidak ada data yang berhasil diekstrak.")
        exit()

    # 4. EXPORT - simpan ke CSV dan JSON
    with open('L0224014_AlvianDamarBudhiHernowo_H2.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Nama", "Tipe", "Total_Stat"])
        writer.writeheader()
        writer.writerows(pokemon_data)
    print("\nDisimpan ke: L0224014_AlvianDamarBudhiHernowo_H2.csv")

    with open('L0224014_AlvianDamarBudhiHernowo_H2.json', 'w', encoding='utf-8') as f:
        json.dump(pokemon_data, f, indent=4)
    print("Disimpan ke: L0224014_AlvianDamarBudhiHernowo_H2.json")

except requests.exceptions.RequestException as e:
    print(f"Gagal request: {e}")
except Exception as e:
    print(f"Error: {e}")
    
    
# Langkah Langkah Menemukan Hidden URL

# 1 Buka Laman http://143.198.223.28:5000/
# 2 klik kanan pada dashboard lalu klik inspect
# 3 Buka bagian Network lalu klik Tombol EasterEgg (berupa tombol berbentuk lingkaran berisi tanda tanya) pada bagian pojok kana bawah web
# 4 Pada bagian Network akan muncul baris bernama `probe` lalu klik kiri 1 kali pada baris tersebut
# 5 Hidden url akan muncul pada bagian headers dari `probe` pada baris X-Lab Chunk