import random
import time
import os

print("💪 Inget ya kemungkinan cuma 0.01%! Semoga hoki!\n")

nama_ssr = input("Masukkan nama SSR impianmu: ")

counter = 0
pity_limit = random.randint(3, 1) 

while True:
    input(f"🎰 Yakin lanjut?({counter}/{pity_limit})... ")
    counter += 1

    chance = random.uniform(0, 100)

    if chance <= 0.01 or counter >= pity_limit:
        print(f"💐 Kamu nggak mimpi kok! Selamat, King! Dapet dia 👑 ({nama_ssr})!\n")
        
        os.system("mpv 'saveinsta.cc_320kbps-yung-kai-blue-official-audio.mp3' &")
        break
    else:
        print(f"💩 Awokawok ampas! Coba lagi ({counter}/{pity_limit})\n")
        time.sleep(1)
