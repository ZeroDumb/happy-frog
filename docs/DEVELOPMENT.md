# Happy Frog - Development Guide

This guide covers development setup, Python API usage, and integration scenarios for Happy Frog.

## 🚀 Development Installation

### From Source (Recommended for Development)
```bash
# Clone the repository
git clone https://github.com/ZeroDumb/happy-frog.git
cd happy-frog

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### From PyPI (For Integration)
```bash
pip install happy-frog
```

### From GitHub (Latest Development Version)
```bash
pip install git+https://github.com/ZeroDumb/happy-frog.git
```

## 📦 Package Architecture

Happy Frog is organized into several core modules:

### Core Modules
- `happy_frog_parser` - Script parsing and encoding engine
- `devices` - Device-specific code generation and management
- `payloads` - Example payload scripts and utilities

### Command Line Interface
```bash
happy-frog --help
happy-frog encode --help
happy-frog parse --help
```

## 🔧 Development Setup

### Prerequisites
- Python 3.7 or higher
- Git
- Virtual environment (recommended)

### Development Dependencies
```bash
# Install development tools
pip install pytest black flake8

# Run tests
pytest

# Format code
black .

# Lint code
flake8
```

### Building the Package
```bash
# Install build tools
pip install build

# Build package
python -m build

# Install from built package
pip install dist/happy_frog-*.whl
```

## 🐍 Python API Usage

### Basic Script Parsing and Encoding

```python
from happy_frog_parser import HappyFrogParser, CircuitPythonEncoder
from devices import DeviceManager

# Initialize components
parser = HappyFrogParser()
encoder = CircuitPythonEncoder()
device_manager = DeviceManager()

# Parse a script
script_content = """
DELAY 1000
STRING Hello World!
ENTER
"""
parsed_script = parser.parse(script_content)

# Generate CircuitPython code
device_code = encoder.encode(parsed_script)
print(device_code)
```

### Device-Specific Code Generation

```python
# Generate code for specific device
device_code = device_manager.encode_script(
    parsed_script, 
    "xiao_rp2040", 
    "output.py",
    production_mode=True
)

# List available devices
devices = device_manager.list_devices()
for device in devices:
    print(f"{device['id']}: {device['name']}")
```

### Working with Payloads

```python
from payloads import load_payload, list_payloads

# List available sample payloads
available_payloads = list_payloads()
print("Available payloads:", available_payloads)

# Load a specific payload
payload_content = load_payload("hello_world.txt")
print("Payload content:", payload_content)
```

### Advanced Script Validation

```python
# Validate a script for errors
warnings = parser.validate_script(parsed_script)
if warnings:
    print("Validation warnings:")
    for warning in warnings:
        print(f"  - {warning}")

# Validate for specific device
device_warnings = device_manager.validate_device_support("xiao_rp2040", parsed_script)
```

## 🔗 Integration Examples

### As a Dependency in Your Project

Add to your `requirements.txt`:
```
happy-frog>=0.2.0
```

### As a Git Submodule
```bash
git submodule add https://github.com/ZeroDumb/happy-frog.git external/happy-frog
```

### Custom HID Automation Framework

```python
from happy_frog_parser import HappyFrogParser, CircuitPythonEncoder
from devices import DeviceManager

class CustomHIDFramework:
    def __init__(self):
        self.parser = HappyFrogParser()
        self.encoder = CircuitPythonEncoder()
        self.device_manager = DeviceManager()
    
    def create_automation_script(self, commands):
        """Create automation script from command list"""
        script_content = "\n".join(commands)
        return self.parser.parse(script_content)
    
    def generate_device_code(self, script, device_id, production=False):
        """Generate device-specific code"""
        return self.device_manager.encode_script(
            script, device_id, "output.py", production
        )
    
    def validate_script(self, script):
        """Validate script for errors"""
        return self.parser.validate_script(script)

# Usage
framework = CustomHIDFramework()
commands = ["DELAY 1000", "STRING Hello World!", "ENTER"]
script = framework.create_automation_script(commands)
code = framework.generate_device_code(script, "xiao_rp2040", production=True)
```

### Educational Platform Integration

```python
from happy_frog_parser import HappyFrogParser

class EducationalPlatform:
    def __init__(self):
        self.parser = HappyFrogParser()
    
    def analyze_student_script(self, script_content):
        """Analyze student-written scripts for educational purposes"""
        try:
            script = self.parser.parse(script_content)
            return {
                "valid": True,
                "command_count": len(script.commands),
                "warnings": self.parser.validate_script(script),
                "complexity_score": self._calculate_complexity(script)
            }
        except Exception as e:
            return {
                "valid": False,
                "error": str(e)
            }
    
    def _calculate_complexity(self, script):
        """Calculate script complexity for educational assessment"""
        advanced_commands = ["IF", "WHILE", "LOG", "VALIDATE"]
        complexity = 0
        for cmd in script.commands:
            if cmd.command_type.value in advanced_commands:
                complexity += 1
        return complexity

# Usage
platform = EducationalPlatform()
result = platform.analyze_student_script("STRING Hello\nIF system_windows\nENTER\nENDIF")
print(f"Script analysis: {result}")
```

## 🐛 Development Troubleshooting

### Import Errors
```bash
# Check if package is properly installed
pip show happy-frog

# Reinstall if needed
pip uninstall happy-frog
pip install -e .
```

### Version Conflicts
```bash
# Use virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install happy-frog
```

### Build Issues
```bash
# Upgrade build tools
pip install --upgrade pip setuptools wheel

# Clean install
pip install -e . --force-reinstall
```

### Test Failures
```bash
# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_parser.py

# Run with coverage
pytest --cov=happy_frog_parser
```

## 📋 Development Checklist

Before contributing:

- [ ] Code passes all tests (`pytest`)
- [ ] Code is formatted (`black .`)
- [ ] Code passes linting (`flake8`)
- [ ] Documentation is updated
- [ ] New features are tested
- [ ] Device compatibility is verified

## 🔮 Contributing

### Adding New Device Support
1. Create device encoder in `devices/` directory
2. Add device to `DeviceManager`
3. Update device list in `microcontrollers.md`
4. Add tests for new device
5. Update documentation

### Adding New Script Commands
1. Add command to parser in `happy_frog_parser/`
2. Update encoder to handle new command
3. Add tests for new command
4. Update documentation and examples

### Reporting Issues
- Use GitHub Issues for bug reports
- Include reproduction steps
- Provide error messages and stack traces
- Specify device and environment details

## 📄 License

This package is licensed under GNU GPLv3. See LICENSE file for details.

---

**Happy developing! 🐸** 