import time
import random
import pyautogui
import csv


music1 = []
music2 = []
music3 = []

with open('song/本草纲目.csv', 'r') as f:
    read = list(csv.reader(f))
    for row in range(len(read)):
        if row % 3 == 0:
            music1 += read[row]
        elif row % 3 == 1:
            music2 += read[row]
        elif row % 3 == 2:
            music3 += read[row]

print(music1)
print(music2)
print(music3)

for ch in music1:
    random_x = random.randint(-5, 5)
    random_y = random.randint(-5, 5)
    random_step = float(format(random.uniform(-0.003, 0.003), '.3f'))
    if ch == '1':
        pyautogui.click(x=575 + random_x, y=375 + random_y, button='left')
    elif ch == '2':
        pyautogui.click(x=646 + random_x, y=375 + random_y, button='left')
    elif ch == '3':
        pyautogui.click(x=719 + random_x, y=375 + random_y, button='left')
    elif ch == '4':
        pyautogui.click(x=791 + random_x, y=375 + random_y, button='left')
    elif ch == '5':
        pyautogui.click(x=863 + random_x, y=375 + random_y, button='left')
    elif ch == '6':
        pyautogui.click(x=575 + random_x, y=446 + random_y, button='left')
    elif ch == '7':
        pyautogui.click(x=646 + random_x, y=446 + random_y, button='left')
    elif ch == '-1':
        pyautogui.click(x=719 + random_x, y=446 + random_y, button='left')
    elif ch == '-2':
        pyautogui.click(x=791 + random_x, y=446 + random_y, button='left')
    elif ch == '-3':
        pyautogui.click(x=863 + random_x, y=446 + random_y, button='left')
    elif ch == '-4':
        pyautogui.click(x=575 + random_x, y=517 + random_y, button='left')
    elif ch == '-5':
        pyautogui.click(x=646 + random_x, y=517 + random_y, button='left')
    elif ch == '-6':
        pyautogui.click(x=719 + random_x, y=517 + random_y, button='left')
    elif ch == '-7':
        pyautogui.click(x=791 + random_x, y=517 + random_y, button='left')
    elif ch == '--1':
        pyautogui.click(x=863 + random_x, y=517 + random_y, button='left')
    time.sleep(0.15 + random_step)


