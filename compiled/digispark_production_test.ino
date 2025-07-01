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

  // Production code - main execution function
  // Wait for system to recognize the device
  DigiKeyboard.delay(2000);

  // DigiSpark Command: # Happy Frog Script - Hello World

  // DigiSpark Command: # Simple educational example demonstrating basic automation

  // DigiSpark Command: #

  // DigiSpark Command: # Educational Purpose: Shows how to create a simple automation script

  // DigiSpark Command: # that types text and performs basic keyboard operations

  // DigiSpark Command: # Wait for system to recognize the device

  // DigiSpark Command: DELAY 1000
  DigiKeyboard.delay(1000);  // DigiSpark delay: 1000ms

  // DigiSpark Command: #ATTACKMODE HID STORAGE

  // DigiSpark Command: # Open notepad

  // DigiSpark Command: MOD r
  // DigiSpark compact modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // DigiSpark Command: STRING notepad
  DigiKeyboard.print("notepad");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: # Type a greeting message

  // DigiSpark Command: STRING Hello, World! This is Happy Frog Script in action!
  DigiKeyboard.print("Hello, World! This is Happy Frog Script in action!");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: # Wait a moment

  // DigiSpark Command: DELAY 500
  DigiKeyboard.delay(500);  // DigiSpark delay: 500ms

  // DigiSpark Command: # Type another message

  // DigiSpark Command: STRING This demonstrates basic text input automation.
  DigiKeyboard.print("This demonstrates basic text input automation.");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: # Wait and type more

  // DigiSpark Command: DELAY 500
  DigiKeyboard.delay(500);  // DigiSpark delay: 500ms

  // DigiSpark Command: STRING Happy Frog Script makes automation simple and educational!
  DigiKeyboard.print("Happy Frog Script makes automation simple and educational!");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

  // DigiSpark Command: # Final message

  // DigiSpark Command: DELAY 500
  DigiKeyboard.delay(500);  // DigiSpark delay: 500ms

  // DigiSpark Command: STRING Remember: Use automation responsibly and ethically!
  DigiKeyboard.print("Remember: Use automation responsibly and ethically!");  // DigiSpark string input

  // DigiSpark Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // DigiSpark key press: ENTER

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