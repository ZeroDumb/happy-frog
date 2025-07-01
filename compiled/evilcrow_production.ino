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

  // Production code - main execution function
  // Wait for system to recognize the device
  DigiKeyboard.delay(2000);

  // EvilCrow-Cable Command: # 🖥️ Automated System Setup - Happy Frog Script

  // EvilCrow-Cable Command: # Real-world example: Automated system configuration and setup

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # Educational Purpose: Demonstrates practical HID automation for:

  // EvilCrow-Cable Command: # - System administration tasks

  // EvilCrow-Cable Command: # - Automated configuration

  // EvilCrow-Cable Command: # - IT support automation

  // EvilCrow-Cable Command: # - Educational demonstrations

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # ⚠️ IMPORTANT: Use only on systems you own or have explicit permission to configure

  // EvilCrow-Cable Command: # This script demonstrates legitimate automation techniques for educational purposes

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 1: INITIALIZATION AND SAFETY

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Enable safe mode for educational use

  // EvilCrow-Cable Command: SAFE_MODE ON
  // SAFE_MODE: Enabled safe mode restrictions
  bool safe_mode = true;

  // EvilCrow-Cable Command: # Set default delay for consistent timing

  // EvilCrow-Cable Command: DEFAULT_DELAY 500
  // DEFAULT_DELAY: Set default delay to 500ms between commands
  int default_delay = 500;  // Default delay in milliseconds

  // EvilCrow-Cable Command: # Log our actions for educational tracking

  // EvilCrow-Cable Command: LOG Starting automated system setup demonstration
  // LOG: Starting automated system setup demonstration
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Validate environment before proceeding

  // EvilCrow-Cable Command: VALIDATE system_ready
  // VALIDATE: Check environment condition 'system_ready'
  // Note: This is a placeholder for environment validation on EvilCrow-Cable
  // EvilCrow-Cable has limited validation capabilities due to memory constraints

  // EvilCrow-Cable Command: # Wait for system to recognize the device

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 2: SYSTEM INFORMATION GATHERING

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: LOG Gathering system information for educational purposes
  // LOG: Gathering system information for educational purposes
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Open System Information

  // EvilCrow-Cable Command: MOD r
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: STRING msinfo32
  DigiKeyboard.print("msinfo32");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 3000
  DigiKeyboard.delay(3000);  // EvilCrow-Cable delay: 3000ms

  // EvilCrow-Cable Command: # Wait for system info to load

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: # Take a screenshot (Windows + PrintScreen)

  // EvilCrow-Cable Command: MOD PRINTSCREEN
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_PRINTSCREEN);  // Press PRINTSCREEN

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: # Close system information

  // EvilCrow-Cable Command: MOD f4
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_F4);  // Press f4

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 3: NETWORK CONFIGURATION DEMO

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: LOG Demonstrating network configuration automation
  // LOG: Demonstrating network configuration automation
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Open Network Settings

  // EvilCrow-Cable Command: MOD r
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: STRING ncpa.cpl
  DigiKeyboard.print("ncpa.cpl");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: # Wait for network connections to load

  // EvilCrow-Cable Command: DELAY 1500
  DigiKeyboard.delay(1500);  // EvilCrow-Cable delay: 1500ms

  // EvilCrow-Cable Command: # Close network settings

  // EvilCrow-Cable Command: MOD f4
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_F4);  // Press f4

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 4: SYSTEM MAINTENANCE TASKS

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: LOG Demonstrating system maintenance automation
  // LOG: Demonstrating system maintenance automation
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Open Disk Cleanup

  // EvilCrow-Cable Command: MOD r
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: STRING cleanmgr
  DigiKeyboard.print("cleanmgr");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: # Wait for disk cleanup to initialize

  // EvilCrow-Cable Command: DELAY 1500
  DigiKeyboard.delay(1500);  // EvilCrow-Cable delay: 1500ms

  // EvilCrow-Cable Command: # Close disk cleanup (cancel the operation)

  // EvilCrow-Cable Command: ESCAPE
  DigiKeyboard.sendKeyPress(KEY_ESC);  // EvilCrow-Cable key press: ESCAPE

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 5: EDUCATIONAL DEMONSTRATION

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: LOG Creating educational demonstration document
  // LOG: Creating educational demonstration document
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Open Notepad for documentation

  // EvilCrow-Cable Command: MOD r
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: STRING notepad
  DigiKeyboard.print("notepad");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 1500
  DigiKeyboard.delay(1500);  // EvilCrow-Cable delay: 1500ms

  // EvilCrow-Cable Command: # Type educational content

  // EvilCrow-Cable Command: STRING ========================================
  DigiKeyboard.print("========================================");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Happy Frog - Automated System Setup Demo
  DigiKeyboard.print("Happy Frog - Automated System Setup Demo");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING ========================================
  DigiKeyboard.print("========================================");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING This demonstration shows how HID automation can be used for:
  DigiKeyboard.print("This demonstration shows how HID automation can be used for:");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - System administration tasks
  DigiKeyboard.print("- System administration tasks");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Automated configuration
  DigiKeyboard.print("- Automated configuration");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - IT support automation
  DigiKeyboard.print("- IT support automation");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Educational purposes
  DigiKeyboard.print("- Educational purposes");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Key Learning Points:
  DigiKeyboard.print("Key Learning Points:");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING 1. HID devices can automate repetitive tasks
  DigiKeyboard.print("1. HID devices can automate repetitive tasks");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING 2. Automation improves efficiency and consistency
  DigiKeyboard.print("2. Automation improves efficiency and consistency");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING 3. Understanding automation helps with defense
  DigiKeyboard.print("3. Understanding automation helps with defense");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING 4. Always use automation ethically and responsibly
  DigiKeyboard.print("4. Always use automation ethically and responsibly");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Security Implications:
  DigiKeyboard.print("Security Implications:");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Physical access can bypass many security measures
  DigiKeyboard.print("- Physical access can bypass many security measures");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - HID attacks work at the input level
  DigiKeyboard.print("- HID attacks work at the input level");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - This is why physical security is crucial
  DigiKeyboard.print("- This is why physical security is crucial");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Monitor for unexpected input devices
  DigiKeyboard.print("- Monitor for unexpected input devices");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Defensive Measures:
  DigiKeyboard.print("Defensive Measures:");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Disable USB ports when not in use
  DigiKeyboard.print("- Disable USB ports when not in use");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Use USB port locks
  DigiKeyboard.print("- Use USB port locks");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Monitor for unexpected input devices
  DigiKeyboard.print("- Monitor for unexpected input devices");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING - Implement input validation and rate limiting
  DigiKeyboard.print("- Implement input validation and rate limiting");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Remember: Knowledge is power, but with great power comes great responsibility!
  DigiKeyboard.print("Remember: Knowledge is power, but with great power comes great responsibility!");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING This demonstration was created with Happy Frog Script
  DigiKeyboard.print("This demonstration was created with Happy Frog Script");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Educational HID Emulation Framework
  DigiKeyboard.print("Educational HID Emulation Framework");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Date:
  DigiKeyboard.print("Date:");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # Insert current date (example)

  // EvilCrow-Cable Command: STRING 2024-01-15
  DigiKeyboard.print("2024-01-15");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING Time:
  DigiKeyboard.print("Time:");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # Insert current time (example)

  // EvilCrow-Cable Command: STRING 14:30:00
  DigiKeyboard.print("14:30:00");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 6: CLEANUP AND COMPLETION

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: LOG Completing automated system setup demonstration
  // LOG: Completing automated system setup demonstration
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Save the document

  // EvilCrow-Cable Command: CTRL s
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_CTRL);  // Press CTRL
  DigiKeyboard.sendKeyPress(KEY_S);  // Press s

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: # Type filename

  // EvilCrow-Cable Command: STRING happy_frog_demo_notes.txt
  DigiKeyboard.print("happy_frog_demo_notes.txt");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: # Close Notepad

  // EvilCrow-Cable Command: MOD f4
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_F4);  // Press f4

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 7: FINAL DEMONSTRATION

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: LOG Final demonstration: Opening the saved document
  // LOG: Final demonstration: Opening the saved document
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Open the saved document to verify

  // EvilCrow-Cable Command: MOD r
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: STRING notepad happy_frog_demo_notes.txt
  DigiKeyboard.print("notepad happy_frog_demo_notes.txt");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: # Wait a moment to show the document

  // EvilCrow-Cable Command: DELAY 3000
  DigiKeyboard.delay(3000);  // EvilCrow-Cable delay: 3000ms

  // EvilCrow-Cable Command: # Close the document

  // EvilCrow-Cable Command: MOD f4
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_F4);  // Press f4

  // EvilCrow-Cable Command: DELAY 500
  DigiKeyboard.delay(500);  // EvilCrow-Cable delay: 500ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 8: COMPLETION AND LOGGING

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: LOG Automated system setup demonstration completed successfully
  // LOG: Automated system setup demonstration completed successfully
  // Note: EvilCrow-Cable has limited serial output capabilities

  // EvilCrow-Cable Command: # Final educational message

  // EvilCrow-Cable Command: MOD r
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: STRING cmd
  DigiKeyboard.print("cmd");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 1500
  DigiKeyboard.delay(1500);  // EvilCrow-Cable delay: 1500ms

  // EvilCrow-Cable Command: # Type completion message

  // EvilCrow-Cable Command: STRING echo.
  DigiKeyboard.print("echo.");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo ========================================
  DigiKeyboard.print("echo ========================================");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo Happy Frog Demo Completed Successfully!
  DigiKeyboard.print("echo Happy Frog Demo Completed Successfully!");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo ========================================
  DigiKeyboard.print("echo ========================================");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo.
  DigiKeyboard.print("echo.");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo Educational demonstration completed.
  DigiKeyboard.print("echo Educational demonstration completed.");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo This shows legitimate uses of HID automation.
  DigiKeyboard.print("echo This shows legitimate uses of HID automation.");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo.
  DigiKeyboard.print("echo.");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo Key takeaways:
  DigiKeyboard.print("echo Key takeaways:");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo - HID automation can improve efficiency
  DigiKeyboard.print("echo - HID automation can improve efficiency");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo - Understanding automation helps with defense
  DigiKeyboard.print("echo - Understanding automation helps with defense");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo - Always use automation ethically
  DigiKeyboard.print("echo - Always use automation ethically");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo - Physical security is crucial
  DigiKeyboard.print("echo - Physical security is crucial");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo.
  DigiKeyboard.print("echo.");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo Remember: Use responsibly and ethically!
  DigiKeyboard.print("echo Remember: Use responsibly and ethically!");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING echo.
  DigiKeyboard.print("echo.");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: STRING pause
  DigiKeyboard.print("pause");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: # Wait for user acknowledgment

  // EvilCrow-Cable Command: DELAY 2000
  DigiKeyboard.delay(2000);  // EvilCrow-Cable delay: 2000ms

  // EvilCrow-Cable Command: # Close command prompt

  // EvilCrow-Cable Command: STRING exit
  DigiKeyboard.print("exit");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # EDUCATIONAL NOTES

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # This script demonstrates:

  // EvilCrow-Cable Command: # 1. Legitimate system administration automation

  // EvilCrow-Cable Command: # 2. Educational HID emulation concepts

  // EvilCrow-Cable Command: # 3. Safe and responsible automation practices

  // EvilCrow-Cable Command: # 4. Real-world applications of HID technology

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # Use cases for this type of automation:

  // EvilCrow-Cable Command: # - IT support automation

  // EvilCrow-Cable Command: # - System deployment scripts

  // EvilCrow-Cable Command: # - Educational demonstrations

  // EvilCrow-Cable Command: # - Security testing (with permission)

  // EvilCrow-Cable Command: # - Accessibility assistance

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # Remember: This is for educational purposes only.

  // EvilCrow-Cable Command: # Always obtain proper authorization before testing on any system.

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