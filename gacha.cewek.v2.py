import random
import time
import os
import sys
import pyfiglet
from colorama import Fore, Style, init

# Inisialisasi colorama
init()

# Animasi ASCII GACHA warna hijau
big_text = pyfiglet.figlet_format("GACHA")
green_text = Fore.GREEN + Style.BRIGHT + big_text + Style.RESET_ALL

for char in green_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)

# Nama author
print(Fore.YELLOW + "Author:irham walzoo" + Style.RESET_ALL)

# Program utama
print(Fore.MAGENTA + "💪 Inget ya kemungkinan cuma 0.01%! Semoga hoki!\n" + Style.RESET_ALL)

nama_ssr = input(Fore.MAGENTA + "Masukkan nama SSR impianmu: " + Style.RESET_ALL)

counter = 0
pity_limit = random.randint(3, 5)

while True:
    input(Fore.MAGENTA + f"🎰 Yakin lanjut?({counter}/{pity_limit})... " + Style.RESET_ALL)
    counter += 1

    chance = random.uniform(0, 100)

    if chance <= 0.01 or counter >= pity_limit:
        print(Fore.MAGENTA + f"💐 Kamu nggak mimpi kok! Selamat! Dapet dia 👑 ({nama_ssr})!\n" + Style.RESET_ALL)
        
        os.system("mpv 'saveinsta.cc_320kbps-yung-kai-blue-official-audio.mp3' &")
        break
    else:
        print(Fore.MAGENTA + f"💩 Awokawok ampas! Coba lagi ({counter}/{pity_limit})\n" + Style.RESET_ALL)
        time.sleep(1)
