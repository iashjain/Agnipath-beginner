# day1_trishul.py
# Day 1 – Flow Control & Loops Conquered ⚔️⚡
# Project Agnipath v3.0 | Warrior: iashjain

from datetime import datetime
import time
import os

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

print("🔥 DAY 1: TRISHUL FORGED IN CODE 🔥\n")

# ===== 1. HAR HAR MAHADEV VALIDATOR =====
num = int(input("Enter a positive integer for divine judgement: "))
print()

if num % 3 == 0 and num % 5 == 0:
    print("Har Har Mahadev ⚡ Jai Bhavani ⚔️")
elif num % 3 == 0:
    print("Har Har Mahadev ⚡")
elif num % 5 == 0:
    print("Jai Bhavani ⚔️")
else:
    print(f"Mortal number: {num}")

print("\n" + "="*40 + "\n")

#More battles coming – stay in this file and keep adding below

# day1_trishul.py
# Day 1 – Flow Control & Loops Conquered ⚔️⚡
# Project Agnipath v3.0 | Warrior: iashjain
# Date: 20 Nov 2025

from datetime import datetime
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("🔥 DAY 1: TRISHUL FORGED IN CODE 🔥\n")

# ===== 1. HAR HAR MAHADEV VALIDATOR =====
try:
    num = int(input("Enter a positive integer for divine judgement: "))
    print()
    if num <= 0:
        print("Only positive mortals allowed!")
    elif num % 3 == 0 and num % 5 == 0:
        print("Har Har Mahadev ⚡ Jai Bhavani ⚔️")
    elif num % 3 == 0:
        print("Har Har Mahadev ⚡")
    elif num % 5 == 0:
        print("Jai Bhavani ⚔️")
    else:
        print(f"Mortal number: {num}")
except ValueError:
    print("Numbers only, warrior!")

print("\n" + "="*50)

# ===== 2. TRISHUL PATTERN GENERATOR =====
try:
    N = int(input("\nEnter height N (1-20) for sacred Trishul: "))
    if not (1 <= N <= 20):
        raise ValueError
    height = 2 * N + 1
    for i in range(height):
        if i < N or i >= N + 1:
            print("⚡".center(20))
        else:
            print("⚡⚡⚡⚡⚡".center(20))
except:
    print("Invalid N – defaulting to N=3")
    N = 3
    for i in range(7):
        print("⚡" if i != 3 else " ⚡⚡⚡⚡⚡ ")

print("\n" + "="*50)

# ===== 3. DAMARU INFINITE LOOP =====
print("\nDamaru meditation started – Hara Hara Mahadev 🕉️")
print("Press 'q' + Enter to stop\n")
start = time.time()
try:
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"Hara Hara Mahadev 🕉️  | {now}")
        time.sleep(3)
        if input() == 'q':
            break
except:
    pass
print("Damaru silenced. Peace attained.")

print("\n" + "="*50)

# ===== 4. AGNIPATH STRENGTH COUNTER =====
print("\n🔥 Agnipath Strength Forge 🔥")
while True:
    try:
        pushups = int(input("How many push-ups today, warrior? "))
        if pushups >= 108:
            print("Jai Shri Ram 🔥 108 complete. You are forged in fire.")
            break
        else:
            print(f"{pushups} is good… but 108 is divine. Again!")
    except:
        print("Enter a number!")

# ===== FINAL WAR CRY =====
print(f"\nDay 1 conquered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Har Har Mahadev ⚡ Jai Bhavani ⚔️ Hare Krishna 🕉️")
