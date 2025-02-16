import random
import time

print("💪 inget ya kemungkinan cuma dpt 0.001% moga hoki !\n")

nama_ssr = input("Masukkan nama SSR impianmu: ")

counter = 0
pity_limit = 5

while True:
    input("🎰 yakin lanjut!!...")
    counter += 1

    chance = random.uniform(0, 100)

    if chance <= 0.01 or counter >= pity_limit:
        print(f"💐kamu gak mimpi kok selamat king({nama_ssr})!\n")
        break
    else:
        print(f"💩 awokawok ampas (coba lagi-{counter})\n")
        time.sleep(1) 
