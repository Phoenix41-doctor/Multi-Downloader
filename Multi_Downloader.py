import os
import time
import yt_dlp
import subprocess
from datetime import datetime

# Warna terminal
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
C = '\033[96m'
W = '\033[0m'

# Output & log
output_dir = os.path.expanduser("~/storage/shared/Video Multi Platform")
log_file = os.path.join(output_dir, "download_log.txt")
os.makedirs(output_dir, exist_ok=True)

# Banner
def banner():
    os.system("clear")
    print(f"""{B}
  __     ___      _             _          _   _             
  \ \   / (_) ___| | _____ _ __(_)______ _| |_(_) ___  _ __  
   \ \ / /| |/ __| |/ / _ \ '__| |_  / _` | __| |/ _ \| '_ \ 
    \ V / | | (__|   <  __/ |  | |/ / (_| | |_| | (_) | | | |
     \_/  |_|\___|_|\_\___|_|  |_/___\__,_|\__|_|\___/|_| |_| 
      {Y}Multi Downloader by: Andry Siagian{W}
""")

# Animasi loading
def loading(text, sec=2):
    print(C + text, end="")
    for _ in range(sec * 2):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(W)

# Tulis ke log
def write_log(msg):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

# Cek update yt-dlp
def check_update():
    print(f"{Y}[•] Mengecek pembaruan yt-dlp...{W}")
    try:
        subprocess.run(["yt-dlp", "-U"], check=True)
    except Exception as e:
        print(f"{R}Gagal update yt-dlp: {e}{W}")

# Tampilkan info video
def preview_info(url):
    try:
        ydl_opts = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title')
            duration = info.get('duration', 0)
            uploader = info.get('uploader', 'Unknown')
            print(f"\n{Y}Informasi Video:{W}")
            print(f"{C}Judul    :{W} {title}")
            print(f"{C}Durasi   :{W} {round(duration/60, 2)} menit")
            print(f"{C}Uploader :{W} {uploader}")
            return title
    except Exception as e:
        print(f"{R}Gagal mengambil info video: {e}{W}")
        return f"video_{int(time.time())}"

# Download video/audio
def download_content(url, quality, is_audio=False, custom_name=None):
    judul_video = preview_info(url)
    file_name = f"{judul_video}.mp4" if not is_audio else f"{judul_video}.mp3"

    if custom_name:
        file_name = f"{custom_name}.mp4" if not is_audio else f"{custom_name}.mp3"

    file_name = file_name.replace(" ", "_").replace("/", "_")
    save_path = os.path.join(output_dir, file_name)

    format_selector = {
        "1": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
        "2": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "3": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "4": "best",
    }

    ydl_opts = {
        'outtmpl': save_path,
        'quiet': True,
        'merge_output_format': 'mp4',
        'format': 'bestaudio/best' if is_audio else format_selector.get(quality, 'best'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }] if is_audio else [],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            loading("Mengunduh")
            ydl.download([url])
        print(f"{G}Sukses: {save_path}{W}")
        write_log(f"{'AUDIO' if is_audio else 'VIDEO'} - {save_path}")
    except Exception as e:
        print(f"{R}Error: {e}{W}")

# Menu riwayat
def lihat_riwayat():
    print(f"\n{Y}=== Riwayat Download ==={W}")
    if not os.path.exists(log_file):
        print(f"{R}Belum ada riwayat.{W}")
        return
    with open(log_file, "r") as f:
        for line in f.readlines()[-10:]:  # tampilkan 10 terakhir
            print(f"{C}{line.strip()}{W}")

    hapus = input(f"\n{R}Hapus semua riwayat? (y/n): {W}").lower()
    if hapus == "y":
        open(log_file, "w").close()
        print(f"{G}Riwayat dihapus.{W}")

# Menu utama
def menu():
    banner()
    check_update()

    while True:
        print(f"""\n{Y}Pilih opsi:{W}
{G}[1]{W} Download Video
{G}[2]{W} Download Audio (MP3)
{G}[3]{W} Lihat Riwayat Download
{G}[4]{W} Keluar""")

        pilihan = input(f"\n{C}>> {W}").strip()

        if pilihan == "1" or pilihan == "2":
            url = input(f"{Y}Masukkan link:{W} ").strip()
            custom = input(f"{C}Ingin rename file? (y/n): {W}").lower()
            custom_name = input("Nama file (tanpa ekstensi): ").strip().replace(" ", "_") if custom == "y" else None

            print(f"""\n{Y}Pilih kualitas video:{W}
{G}[1]{W} {C}2K / 4K{W} {Y}(jika tersedia){W}
{G}[2]{W} {C}1080p{W}
{G}[3]{W} {C}720p{W}
{G}[4]{W} {C}Otomatis terbaik{W}""")
            quality = input(f"\n{C}>> {W}").strip()
            download_content(url, quality, is_audio=(pilihan == "2"), custom_name=custom_name)

        elif pilihan == "3":
            lihat_riwayat()
        elif pilihan == "4":
            print(f"{G}Sampai jumpa!{W}")
            break
        else:
            print(f"{R}Pilihan tidak valid.{W}")

# Jalankan
if __name__ == "__main__":
    menu()
