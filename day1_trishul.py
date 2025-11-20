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

# More battles coming – stay in this file and keep adding below
