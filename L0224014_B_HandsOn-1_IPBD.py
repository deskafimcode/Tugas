from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Tabel Mahasiswa",version="1.0")

tabel_mahasiswa = {}

class mahasiswa (BaseModel):
    nim : str
    nama : str
    kelas : str
    
@app.get("/")
def cek_server():
    return{
        "message" : "Server Sudah Berjalan"
    }
    
@app.post("/tambah_mahasiswa")
def tambah_mahasiswa(mahasigma : mahasiswa):
    if mahasigma.nim not in tabel_mahasiswa :
        tabel_mahasiswa[mahasigma.nim] = mahasigma
        return {
            "message" : "Data berhasil ditambahkan",
            "data" : mahasigma
        }
    else :
        return {
            "message" : "Nim sudah ada, silahkan gunakan nim lain",
            "data" : mahasigma,
            "data server" : tabel_mahasiswa[mahasigma.nim]
        }
        
@app.get("/tampilkan_mahasiswa")
def tampil_mahasiswa():
    return tabel_mahasiswa

@app.put("/edit_mahasiswa")
def edit_mahasiswa(mahasigma: mahasiswa):
    if mahasigma.nim in tabel_mahasiswa :
        mahasigma_lama = tabel_mahasiswa[mahasigma.nim]
        tabel_mahasiswa[mahasigma.nim] = mahasigma
        return {"message": "Data diubah!", "data lama": mahasigma_lama, "data baru" : mahasigma}
    else :
        return {"message": "Tidak ada data tersebut di dalam Tabel mahasiswa", "data": mahasigma}
    
@app.delete("/hapus_mahasiswa")
def hapus_mahasiswa(nim : str):
    if nim in tabel_mahasiswa :
        mahasigma = tabel_mahasiswa[nim]
        del tabel_mahasiswa[nim]
        return {"message": "Data dihapus!", "data": mahasigma}
    else :
        return {"message": "Tidak ada nim tersebut di dalam Tabel mahasiswa", "nim": nim}