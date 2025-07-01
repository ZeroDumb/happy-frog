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

  // Production code - main execution function
  // Wait for system to recognize the device
  delay(2000);

  // Leonardo Command: # Happy Frog Script - Hello World

  // Leonardo Command: # Simple educational example demonstrating basic automation

  // Leonardo Command: #

  // Leonardo Command: # Educational Purpose: Shows how to create a simple automation script

  // Leonardo Command: # that types text and performs basic keyboard operations

  // Leonardo Command: # Wait for system to recognize the device

  // Leonardo Command: DELAY 1000
  delay(1000);  // Leonardo delay: 1000ms

  // Leonardo Command: #ATTACKMODE HID STORAGE

  // Leonardo Command: # Open notepad

  // Leonardo Command: MOD r
  // Leonardo optimized modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('R');  // Press r
  Keyboard.release('R');  // Release r
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Leonardo Command: STRING notepad
  Keyboard.print("notepad");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: # Type a greeting message

  // Leonardo Command: STRING Hello, World! This is Happy Frog Script in action!
  Keyboard.print("Hello, World! This is Happy Frog Script in action!");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: # Wait a moment

  // Leonardo Command: DELAY 500
  delay(500);  // Leonardo delay: 500ms

  // Leonardo Command: # Type another message

  // Leonardo Command: STRING This demonstrates basic text input automation.
  Keyboard.print("This demonstrates basic text input automation.");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: # Wait and type more

  // Leonardo Command: DELAY 500
  delay(500);  // Leonardo delay: 500ms

  // Leonardo Command: STRING Happy Frog Script makes automation simple and educational!
  Keyboard.print("Happy Frog Script makes automation simple and educational!");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

  // Leonardo Command: # Final message

  // Leonardo Command: DELAY 500
  delay(500);  // Leonardo delay: 500ms

  // Leonardo Command: STRING Remember: Use automation responsibly and ethically!
  Keyboard.print("Remember: Use automation responsibly and ethically!");  // Leonardo string input

  // Leonardo Command: ENTER
  Keyboard.press(KEY_RETURN);  // Leonardo key press: ENTER
  Keyboard.release(KEY_RETURN);  // Leonardo key release: ENTER

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