import time
import pyautogui
import pyperclip

# Countdown: click inside the VM terminal during this time
for i in range(5):
    print(f"Typing in {5 - i}...")
    time.sleep(1)

text = pyperclip.paste()
text = text.replace("\r\n", "\n")  # Windows line endings would press Enter twice

pyautogui.write(text, interval=0.02)
print("Done.")
