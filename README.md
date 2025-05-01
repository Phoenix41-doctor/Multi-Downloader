===========================================  
     Multi Downloader by Andry Siagian  
===========================================  

Deskripsi:  
-----------  
Multi Downloader adalah tool Python berbasis CLI yang dapat digunakan untuk mengunduh video/audio dari berbagai platform seperti:  
- YouTube  
- TikTok  
- Instagram  
- Facebook  

Dengan fitur unggulan seperti pemilihan kualitas, unduhan MP3, auto rename, riwayat, dan interface interaktif.  

===========================================  
Fitur:  
-------  
- Pilih resolusi video: 2K, 1080p, 720p  
- Download audio (MP3)  
- Otomatis memberi nama file sesuai judul video  
- Riwayat unduhan + auto delete log  
- Update otomatis yt-dlp  
- Menu CLI interaktif  

===========================================  
Cara Instalasi (di Termux):  
-----------------------------  
1. Update & install paket dasar  
   pkg update && pkg upgrade  
   pkg install git python ffmpeg -y  

2. Clone repository (ganti dengan milikmu!)  
   git clone https://github.com/Phoenix41-doctor/Pengunduh-Multiguna.git  
   cd Pengunduh-Multiguna  

3. Install dependensi Python  
   pip install -r requirements.txt  

4. Jalankan tool:  
   python Multi_Downloader.py  

===========================================  
Catatan Tambahan:  
------------------  
- Tool ini berbasis `yt-dlp`, jadi pastikan jaringan internet aktif saat pertama kali digunakan.  
- Gunakan Termux versi terbaru untuk performa terbaik.  
- Jika terjadi error terkait SSL atau koneksi, coba install:  
   pip install --upgrade certifi  

===========================================  
Kontak & Kredit:  
----------------  
Developer: Andry Siagian  
GitHub: https://github.com/Phoenix41-doctor  

Terima kasih telah menggunakan Multi Downloader!
