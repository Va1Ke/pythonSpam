import pyautogui, time
time.sleep(5)
for i in range(1,2000):
    pyautogui.typewrite("+")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.click(button='left')