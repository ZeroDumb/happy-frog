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

  // Production code - main execution function
  // Wait for system to recognize the device
  delay(2000);

  // Teensy 4.0 Command: # Happy Frog Script - Hello World

  // Teensy 4.0 Command: # Simple educational example demonstrating basic automation

  // Teensy 4.0 Command: #

  // Teensy 4.0 Command: # Educational Purpose: Shows how to create a simple automation script

  // Teensy 4.0 Command: # that types text and performs basic keyboard operations

  // Teensy 4.0 Command: # Wait for system to recognize the device

  // Teensy 4.0 Command: DELAY 1000
  delay(1000);  // Teensy 4.0 optimized delay: 1000ms

  // Teensy 4.0 Command: #ATTACKMODE HID STORAGE

  // Teensy 4.0 Command: # Open notepad

  // Teensy 4.0 Command: MOD r
  // Teensy 4.0 high-performance modifier combo
  Keyboard.press(KEY_LEFT_GUI);  // Press MOD
  Keyboard.press('R');  // Press r
  Keyboard.release('R');  // Release r
  Keyboard.release(KEY_LEFT_GUI);  // Release MOD

  // Teensy 4.0 Command: STRING notepad
  Keyboard.print("notepad");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: # Type a greeting message

  // Teensy 4.0 Command: STRING Hello, World! This is Happy Frog Script in action!
  Keyboard.print("Hello, World! This is Happy Frog Script in action!");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: # Wait a moment

  // Teensy 4.0 Command: DELAY 500
  delay(500);  // Teensy 4.0 optimized delay: 500ms

  // Teensy 4.0 Command: # Type another message

  // Teensy 4.0 Command: STRING This demonstrates basic text input automation.
  Keyboard.print("This demonstrates basic text input automation.");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: # Wait and type more

  // Teensy 4.0 Command: DELAY 500
  delay(500);  // Teensy 4.0 optimized delay: 500ms

  // Teensy 4.0 Command: STRING Happy Frog Script makes automation simple and educational!
  Keyboard.print("Happy Frog Script makes automation simple and educational!");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

  // Teensy 4.0 Command: # Final message

  // Teensy 4.0 Command: DELAY 500
  delay(500);  // Teensy 4.0 optimized delay: 500ms

  // Teensy 4.0 Command: STRING Remember: Use automation responsibly and ethically!
  Keyboard.print("Remember: Use automation responsibly and ethically!");  // Teensy 4.0 high-performance string input

  // Teensy 4.0 Command: ENTER
  Keyboard.press(KEY_RETURN);  // Teensy 4.0 key press: ENTER
  Keyboard.release(KEY_RETURN);  // Teensy 4.0 key release: ENTER

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