# 🐸 Happy Frog

**"One Small Step for HID. One Giant Leap for Keyboard Chaos."** (Now PIP available, see below for further instructions)

Welcome to **Happy Frog** — your new favorite educational mayhem engine disguised as an HID emulation framework. You've heard of rubber duckies. You've seen people pretend to be keyboards. But have you ever watched a frog automate your operating system and ask *"Why are you like this?"* while doing it?

Didn't think so.

![IMG_3281](https://github.com/user-attachments/assets/f023bf60-4578-4d83-843b-cc087e973889)


##  What Even Is This?

This is not a toy. Unless you play in cybersecurity labs for fun (we do). Happy Frog is your customizable, open-source playground for learning how **automated input attacks** work — ethically, responsibly, and with just enough flair to make your sysadmin sweat. It's ducky script, reimagined. Simpler, safer, more sarcastic.

Oh, and **no binaries**. You want sketchy obfuscated payloads? Go look somewhere else. Here, everything's open, readable, and educational. Like a frog in a chemistry lab with safety goggles and way too much caffeine.

##  The Obligatory Legal Glare

This project is for **educational purposes only**. You may:

👉 Train  
👉 Simulate (in approved labs)  
👉 Learn responsibly  
👉 Get smarter

You may not:

🚫 Use this to be a jerk  
🚫 Hack without permission  
🚫 Ruin someone's day  
🚫 Blame us when you ignore this section

> You are responsible for your usage. Like a grown-up. Or at least a well-supervised minor.

## Current known issues and progress
- some of the device specific encoders need updating to handle attack and production ready builds
  for imediate use cases, you can skip using -d and just run encode for .py output while I work
  on the others
- fixed: some logic is failing to parse reliably, should be fixed within the next couple releases
- most tested and reliable device right now is the xiao rp2040

##  Why Happy Frog Exists

- Because people learn better with humor and hands-on tools  
- Because HID emulation is cooler than memorizing ports  
- Because scripting should feel like frog jumps, not wading through molasses  
- Because automation shouldn't be a proprietary black box  
- Because you deserve tools that explain *why*, not just *what*

##  The Frog Language

Happy Frog Script™ (trademark pending, not really) is:

- Familiar if you've used DuckyScript  
- Friendlier because we believe in helpful errors  
- Fancier with loops, logic, and safe mode
- Actually works (unlike some other frameworks we won't name)

It's compatible, convertible, and extensively commented. Your other scripts won't cry during migration.

##  Features & Commands

You get all the usual suspects — `STRING`, `ENTER`, `CTRL`, `MOD`, `DELAY`, `REPEAT` — but also:

- `IF`, `ELSE`, `WHILE` for conditional logic
- `LOG` for educational commentary  
- `VALIDATE` for environment checks  
- `SAFE_MODE` so you don't nuke your real OS  
- `RANDOM_DELAY` for that oh-so-human typing slop

It's everything you wanted in duckyland, except now the duck is a frog with a PhD in chaos theory.

### Supported Commands

#### Basic Input & Navigation
- **Basic Input**: `STRING`, `ENTER`, `SPACE`, `TAB`, `BACKSPACE`, `DELETE`
- **Navigation**: `UP`, `DOWN`, `LEFT`, `RIGHT`, `HOME`, `END`, `PAGE_UP`, `PAGE_DOWN`
- **Function Keys**: `F1` through `F12`
- **Modifiers**: `CTRL`, `SHIFT`, `ALT`, `MOD` (Windows/Command key)
- **Combos**: `MOD r`, `CTRL ALT DEL`, `SHIFT F1`

#### Timing & Control
- **Delays**: `DELAY` for precise timing control
- **Default Delays**: `DEFAULT_DELAY` or `DEFAULTDELAY` for global timing
- **Random Delays**: `RANDOM_DELAY min max` for human-like behavior
- **Pause**: `PAUSE` or `BREAK` for execution control
- **Repeat**: `REPEAT n` to repeat previous commands

#### Advanced Features (Happy Frog Exclusive)
- **Conditional Logic**: `IF condition`, `ELSE`, `ENDIF`
- **Loops**: `WHILE condition`, `ENDWHILE`
- **Logging**: `LOG message` for debugging and education
- **Validation**: `VALIDATE condition` for environment checks
- **Safe Mode**: `SAFE_MODE ON/OFF` for controlled execution

#### Documentation
- **Comments**: `#` and `REM` for documentation

##  Sample Sorcery

Here's a taste of what your script might look like if your frog spent a semester at Hogwarts:

```txt
# This is Happy Frog casting Hello World
SAFE_MODE ON
DEFAULT_DELAY 500
LOG Preparing automation spell...
STRING Hello, World!
ENTER
IF system_windows
  STRING Notepad time
  MOD r
  STRING notepad
  ENTER
ENDIF
```

Yes, it works. Yes, it's hilarious. Yes, it's educational.

### More Examples

#### Basic Example
```txt
# Happy Frog Script - Hello World
# Educational example demonstrating basic automation

DELAY 1000
STRING Hello, World! This is Happy Frog Script in action!
ENTER
DELAY 500
STRING This demonstrates basic text input automation.
ENTER
```

#### Advanced Example with Conditional Logic

- ATTACKMODE in your initial script can be #out or ommited to make the resulting code not auto run on boot

```txt
# Advanced Happy Frog Script - Demonstrating exclusive features

# Set default delay for all commands
DEFAULT_DELAY 500

# Enable safe mode for educational use
SAFE_MODE ON

# Log our actions for debugging
LOG Starting advanced automation sequence

# Human-like random delays
RANDOM_DELAY 200 800

# Conditional execution
IF system_windows
STRING Windows system detected
ELSE
STRING Non-Windows system detected
ENDIF

# Loop execution
WHILE counter < 3
STRING Loop iteration
ENTER
RANDOM_DELAY 100 300
ENDWHILE

# Advanced modifier combo
ATTACKMODE
MOD r
DELAY 500
STRING notepad
ENTER

# Log completion
LOG Advanced automation sequence completed
```

#### Ducky Script Conversion Example
```txt
# Original Ducky Script
REM Open Run dialog
WINDOWS r
DELAY 1000
STRING cmd
ENTER

# Converts to Happy Frog Script:
# Open Run dialog
MOD r
DELAY 1000
STRING cmd
ENTER
```

##  Installation & Setup

### Quick Start with Pip

The easiest way to get started with Happy Frog is via pip:

```bash
# Install the latest version from PyPI
pip install happy-frog

# Verify installation
happy-frog --help
```

### Development Installation

For developers and contributors:

```bash
# Clone the repository
git clone https://github.com/ZeroDumb/happy-frog.git
cd happy-frog

# Install in development mode
pip install -e .

# Or install dependencies directly
pip install -r requirements.txt
```

### Hardware Setup

Grab a Xiao RP2040 or any of the other microcontrollers listed in our device support. Install CircuitPython. Write your payload. Run the scripts. Don't overthink it.



##  Usage

### Command Line Interface

The CLI is actually useful (shocking, we know):
- use -p or --production for run ready code
- ommit --production results in educational comments and main() requirements to execute

```bash
# Parse a Happy Frog Script file (see what the frog is thinking)
happy-frog parse payloads/hello_world.txt

# Encode to CircuitPython (turn thoughts into reality)
happy-frog encode payloads/demo_automation.txt -o compiled/output.py --production

# Convert Ducky Script to Happy Frog Script (migration magic)
happy-frog convert ducky_script.txt

# Validate a script (make sure it's not going to break everything)
happy-frog validate payloads/demo_automation.txt

# Verbose output (for when you want to see everything)
happy-frog encode payloads/demo_automation.txt -o compiled/output.py --verbose

# Select specific device (because not all frogs are the same)
happy-frog encode payloads/demo_automation.txt --device xiao_rp2040 -o compiled/output.py
```

### What Each Command Actually Does

- **`parse`**: Reads your script and tells you what it's going to do (without actually doing it)
- **`encode`**: Converts your script into actual CircuitPython code that runs on hardware
- **`validate`**: Checks if your script is safe and won't break things (mostly)
- **`convert`**: Transforms old Ducky Script into modern Happy Frog Script

### Python API

For developers who want to integrate Happy Frog into their projects:

```python
from happy_frog_parser import HappyFrogParser, CircuitPythonEncoder
from devices import DeviceManager
from payloads import load_payload, list_payloads

# Parse a script
parser = HappyFrogParser()
script = parser.parse_file("my_script.txt")

# Generate device code
encoder = CircuitPythonEncoder()
code = encoder.encode(script, "output.py")

# Use device-specific encoders
device_manager = DeviceManager()
code = device_manager.encode_script(script, "xiao_rp2040", "output.py")

# Access built-in payloads
print(list_payloads())
payload_content = load_payload("hello_world.txt")
```

##  Device Support

Happy Frog supports multiple microcontrollers because we're not picky about hardware:

### Supported Devices
- **Seeed Xiao RP2040** - Primary development platform (the one we actually test on)
- **Raspberry Pi Pico** - Popular alternative (because everyone has one)
- **Arduino Leonardo** - Classic choice (for the traditionalists)
- **Teensy 4.0** - High-performance option (for the speed demons)
- **DigiSpark** - Compact and affordable (for the budget-conscious)
- **ESP32** - WiFi-enabled automation (for the wireless wizards)
- **EvilCrow-Cable** - Specialized hardware (for the advanced users)

Each device has its own encoder that generates optimized code. Because one size doesn't fit all in the microcontroller world.

##  Use Cases & Why You'd Want This

### For Educators & Students
- **Cybersecurity Labs**: Teach HID emulation concepts safely
- **Programming Education**: Learn automation and scripting
- **Hardware Projects**: Understand microcontroller programming
- **Security Awareness**: Demonstrate physical security risks

### For Developers & Researchers
- **Automation Testing**: Create automated input scenarios
- **Security Research**: Study HID-based attack vectors
- **Prototype Development**: Rapidly test automation ideas
- **Integration Projects**: Build HID automation into larger systems

### For System Administrators
- **Automated Setup**: Script system configuration tasks
- **Testing Procedures**: Validate security controls
- **Documentation**: Create reproducible automation examples
- **Training**: Demonstrate security concepts to teams

### For Makers & Hobbyists
- **DIY Projects**: Build custom automation devices
- **Learning Electronics**: Understand microcontroller programming
- **Creative Automation**: Build unique input devices
- **Educational Demonstrations**: Show how automation works

### Real-World Examples
```bash
# Educational: Create a simple automation demo
happy-frog encode payloads/hello_world.txt --device xiao_rp2040

# Research: Convert existing Ducky Scripts for analysis
happy-frog convert legacy_ducky_script.txt

# Development: Validate automation scripts before deployment
happy-frog validate my_automation_script.txt

# Testing: Generate device-specific code for different platforms
happy-frog encode my_script.txt --device arduino_leonardo -o arduino_output.ino
```

##  Documentation

- [Hello Happy Frog](docs/HELLO_HAPPY_FROG.md) - Beginner-friendly guide (actually beginner-friendly)
- [Usage Guide](docs/usage.md) - Detailed usage instructions (with examples that work)
- [Microcontroller Setup](docs/microcontrollers.md) - Hardware setup guide (because hardware is hard)
- [Educational Examples](payloads/) - Sample scripts with explanations (that actually run)
- [How We Are Different](docs/How_We_Are_Different.md) - What sets Happy Frog apart (besides the frog theme)

##  Safety Rules

- Test in a **virtual machine** or burn your own device (we're not kidding)
- Backup your stuff or... burn your own device (seriously, backup your stuff)
- Don't run unknown scripts like a rookie... or burn your own device (see the pattern?)
- Leave the frog alone when it says "No" (it knows things)
- Remember, don't be dumb (this is the most important rule)

##  Who Is This For?

- **Tinkerers** - People who like to break things (responsibly)
- **Educators** - People who teach others to break things (responsibly)
- **Students** - People learning to break things (responsibly)
- **Ethical hackers** - People who break things for good reasons
- **Anyone who wants to *understand* input emulation** - Not just run sketchy scripts from 2017

##  What's Actually Working

- ✅ Script parsing and validation
- ✅ CircuitPython code generation
- ✅ Multi-device support (7+ devices)
- ✅ Ducky Script conversion
- ✅ CLI with helpful error messages
- ✅ Educational examples that actually work
- ✅ Safety features and warnings
- ✅ Comprehensive testing (because we're professionals)
- ✅ Pip package distribution
- ✅ Python API for integration
- ✅ Device-specific optimizations

##  Known Issues

- Sometimes the frog gets confused (we're working on it)
- Hardware compatibility varies (because hardware is weird)
- Documentation might be sarcastic (this is a feature, not a bug)

## ☕ Support the Project

Want to support future chaos?  
- [X - @zerodumb_dev](https://x.com/zerodumb_dev)  
- [Blog](https://zerodumb.dev)  
- [Store - Coming Soon](https://store.zerodumb.dev)
- [Buy Me Coffee](https://buymeacoffee.com/iamnotaskid) Please, seriously, lol

---

**Remember: Knowledge is power, but with great power comes great responsibility! 🐸**

**Happy Frog: Where Education Meets Innovation in HID Emulation**

*"One Small Step for HID. One Giant Leap for Keyboard Chaos."*

**Stay Loud**
-zero
