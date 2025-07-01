/*
Happy Frog - EvilCrow-Cable Production Code
HID Emulation Script - Runs immediately on boot

Device: EvilCrow-Cable
Processor: ATtiny85
Framework: Arduino (EvilCrow-Cable)
Mode: Production (immediate execution)

⚠️ PRODUCTION MODE: This code runs immediately when device boots!
⚠️ Use only for authorized testing and educational purposes!
*/

#include "DigiKeyboard.h"  // EvilCrow-Cable keyboard library
#include <SoftwareSerial.h> // For WiFi module
#define WIFI_RX 2
#define WIFI_TX 3
SoftwareSerial wifiSerial(WIFI_RX, WIFI_TX); // RX, TX

void setup() {
  // Initialize EvilCrow-Cable for stealth HID emulation
  DigiKeyboard.update();
  wifiSerial.begin(115200); // Start WiFi serial
  DigiKeyboard.delay(1000);  // Stealth startup delay
}

void loop() {
  // Production mode - execute payload immediately
  executePayload();
  while(true) { ; }
}

void executePayload() {
  // Generated Happy Frog payload for EvilCrow-Cable

  // Production code - executes immediately on device boot/plug-in
  // ATTACKMODE detected - running payload automatically

  // Wait for system to recognize the device
  DigiKeyboard.delay(2000);

  // EvilCrow-Cable Command: # EvilCrow-Cable Android Attack Test

  // EvilCrow-Cable Command: # This payload uses EvilCrow-Cable to test Android device security

  // EvilCrow-Cable Command: # EvilCrow-Cable specific setup

  // EvilCrow-Cable Command: ATTACKMODE HID STORAGE
  // ATTACKMODE: Configured for HID emulation (HID STORAGE)
  // Note: This device is configured as a HID keyboard/mouse
  // Configuration: HID STORAGE

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: # Android navigation test

  // EvilCrow-Cable Command: ANDROID_HOME
  DigiKeyboard.sendKeyPress(KEY_ANDROID_HOME);  // EvilCrow-Cable key press: ANDROID_HOME

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: STRING EvilCrow-Cable Android Test
  DigiKeyboard.print("EvilCrow-Cable Android Test");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: # Android system controls

  // EvilCrow-Cable Command: ANDROID_VOLUME_UP
  DigiKeyboard.sendKeyPress(KEY_ANDROID_VOLUME_UP);  // EvilCrow-Cable key press: ANDROID_VOLUME_UP

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: ANDROID_VOLUME_DOWN
  DigiKeyboard.sendKeyPress(KEY_ANDROID_VOLUME_DOWN);  // EvilCrow-Cable key press: ANDROID_VOLUME_DOWN

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # Android app management

  // EvilCrow-Cable Command: ANDROID_OPEN_APP Settings
  DigiKeyboard.sendKeyPress(KEY_ANDROID_OPEN_APP);  // EvilCrow-Cable key press: ANDROID_OPEN_APP

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: ANDROID_BACK
  DigiKeyboard.sendKeyPress(KEY_ANDROID_BACK);  // EvilCrow-Cable key press: ANDROID_BACK

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # Android notifications

  // EvilCrow-Cable Command: ANDROID_NOTIFICATIONS
  DigiKeyboard.sendKeyPress(KEY_ANDROID_NOTIFICATIONS);  // EvilCrow-Cable key press: ANDROID_NOTIFICATIONS

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: ANDROID_BACK
  DigiKeyboard.sendKeyPress(KEY_ANDROID_BACK);  // EvilCrow-Cable key press: ANDROID_BACK

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # Android screenshot

  // EvilCrow-Cable Command: ANDROID_SCREENSHOT
  DigiKeyboard.sendKeyPress(KEY_ANDROID_SCREENSHOT);  // EvilCrow-Cable key press: ANDROID_SCREENSHOT

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: # Return to home

  // EvilCrow-Cable Command: ANDROID_HOME
  DigiKeyboard.sendKeyPress(KEY_ANDROID_HOME);  // EvilCrow-Cable key press: ANDROID_HOME

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: STRING EvilCrow-Cable test completed!
  DigiKeyboard.print("EvilCrow-Cable test completed!");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // End of Happy Frog payload
}

/*
End of Happy Frog Production Code for EvilCrow-Cable

Production Notes:
- This code runs immediately on device boot
- Optimized for WiFi-enabled BadUSB attacks
- Stealth design and compact form factor
- Use only for authorized testing and education

For more information, visit: https://github.com/ZeroDumb/happy-frog
*/