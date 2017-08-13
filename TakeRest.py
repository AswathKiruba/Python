import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while (break_count<3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=2_pG4zHhzRQ&list=PLEFF01B3CBDC5C601")
    break_count = break_count+1
