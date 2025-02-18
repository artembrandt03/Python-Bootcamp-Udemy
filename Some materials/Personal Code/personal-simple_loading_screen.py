import os
import time

for number in range (0, 501, 15):
    time.sleep(0.1)
    percentage = round(number*2/10)
    print(f"LOADING {percentage}%")
    input("Loading complete!")
    os.system("cls" if os.name == "nt" else "clear")