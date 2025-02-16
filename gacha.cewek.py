import random
import time

print("💪 gacha terus bree nanti jga hoki kok!\n")

nama_ssr = input("Masukkan nama SSR impianmu: ")

counter = 0
pity_limit = 5

while True:
    input("🎰 gacha lagi alias depo lagi!!...")
    counter += 1

    chance = random.uniform(0, 100)

    if chance <= 0.01 or counter >= pity_limit:
        print(f"🔥 KING elu udh dpt dia🥹 MAXWIN ({nama_ssr})!\n")
        break
    else:
        print(f"💩 awokawok ampas (Percobaan ke-{counter})\n")
        time.sleep(1) 
