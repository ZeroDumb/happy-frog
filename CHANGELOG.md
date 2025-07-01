# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.7] - 2025-07-01

### Added
- **Android Device support** with mobile-specific automation commands:
  - `ANDROID_HOME` - Navigate to home screen
  - `ANDROID_BACK` - Navigate back
  - `ANDROID_MENU` - Open context menu
  - `ANDROID_APP_SWITCH` - Switch between recent apps
  - `ANDROID_NOTIFICATIONS` - Open notifications panel
  - `ANDROID_QUICK_SETTINGS` - Open quick settings
  - `ANDROID_SCREENSHOT` - Take screenshot
  - `ANDROID_VOLUME_UP/DOWN` - Volume controls
  - `ANDROID_MUTE` - Mute audio
  - `ANDROID_POWER` - Power button
  - `ANDROID_OPEN_APP <name>` - Open specific app
  - `ANDROID_CLOSE_APP` - Close current app
  - `ANDROID_CLEAR_RECENTS` - Clear recent apps
  - `ANDROID_GOOGLE_ASSISTANT` - Activate Google Assistant
  - `ANDROID_SPLIT_SCREEN` - Enable split screen
  - `ANDROID_PIP_MODE` - Picture-in-picture mode
  - `ANDROID_ACCESSIBILITY` - Accessibility menu
  - `ANDROID_DEVELOPER_OPTIONS` - Developer options access
- **EvilCrow-Cable specialty commands** for advanced BadUSB operations:
  - `RELEASE` - Release all pressed keys
  - `WIFI_SEND <data>` - Send data over WiFi serial
  - `WIFI_CONNECT <ssid> <password>` - Connect to WiFi network
  - `SHELLWIN <ip>` - Trigger Windows remote shell
  - `SHELLNIX <ip>` - Trigger Linux remote shell
  - `SHELLMAC <ip>` - Trigger macOS remote shell
- **Enhanced parser support** for EvilCrow-Cable specific commands
- **Production-ready encoders** for all major devices:
  - Teensy 4.0 - High-performance ARM Cortex-M7 optimization
  - Arduino Leonardo - Native USB HID with ATmega32u4
  - DigiSpark - Ultra-compact ATtiny85 with stealth capabilities
  - ESP32 - Bluetooth HID with WiFi and web server support
  - EvilCrow-Cable - WiFi-enabled BadUSB with specialty commands
- **ATTACKMODE detection** with WiFi support across all devices
- **New CLI commands** for payload management:
  - `list-payloads` - List all available sample payloads
  - `copy-payload <name> <destination>` - Copy sample payloads to user directory
- **Enhanced CLI help system** with improved formatting and descriptions
- **Unicode encoding fallback** for terminal compatibility
- **Comprehensive device support documentation** in microcontrollers.md

### Changed
- **Production mode optimization** - All devices now generate production-ready code with `--production` or `-p` flag
- **Device encoder architecture** - Unified production/educational mode support across all encoders
- **EvilCrow-Cable integration** - Fully integrated with CLI and device manager
- **Parser extensibility** - Enhanced to support device-specific specialty commands
- **Documentation consolidation** - Merged multiple overlapping documents:
  - Merged `HELLO_HAPPY_FROG.md` into `usage.md` for comprehensive user guide
  - Merged `How_We_Are_Different.md` into `README.md` for project differentiation
  - Merged `devices/README` into `microcontrollers.md` for device support
  - Renamed `INSTALL.md` to `DEVELOPMENT.md` with developer-focused content
- **Updated CLI interface** - Standardized command structure across all documentation
- **Improved help system** - Added detailed descriptions and examples for all commands
- **Enhanced device documentation** - Complete device list with categories and status

### Fixed
- **Device manager integration** - Fixed EvilCrow-Cable import and registration issues
- **Backward compatibility** - Ensured all existing devices continue to work with new parser features
- **CLI help display issues** - Fixed incomplete help output for subcommands
- **Unicode encoding errors** - Added graceful fallback for terminal compatibility
- **Documentation inconsistencies** - Standardized CLI examples and device names
- **Missing feature documentation** - Added ATTACKMODE and production mode to usage guide

### Removed
- **Redundant documentation files**:
  - `docs/HELLO_HAPPY_FROG.md` - Content merged into usage.md
  - `docs/How_We_Are_Different.md` - Content merged into README.md
  - `devices/README` - Content merged into microcontrollers.md
  - `docs/INSTALL.md` - Renamed to DEVELOPMENT.md

## [0.2.6] - 2025-06-27

### Added
- **Production-ready packaging configuration**
- **Clean dependency management**
- **Proper version control**
- **ATTACKMODE support** for immediate execution on device boot
- **Production mode** for generating immediate execution code (no main() function)
- **Educational mode** with enhanced safety features and detailed comments
- **Device-specific encoders** with production mode support
- **Xiao RP2040 encoder** with proper ATTACKMODE detection and import board support
- **Enhanced CLI interface** with subcommands (parse, encode, validate, convert)
- **Device-specific code generation** with support for 7+ microcontrollers
- **Ducky Script conversion** functionality
- **Verbose output options** for debugging and education

### Changed
- **Excluded development files** from package distribution
- **Updated development status** to Beta
- **Streamlined package structure**
- **Deprecated and removed redundant `ducky_parser`** - consolidated to single `happy_frog_parser`
- **Enhanced ATTACKMODE handling** - flexible regex pattern vs restrictive pattern
- **Improved code generation** - template-based system with production/educational modes
- **Updated device manager** to support production mode for device-specific encoders
- **CLI interface** - Now uses subcommands instead of direct file processing

### Fixed
- **Import issues** with device modules
- **Conditional CircuitPython imports** for host compatibility
- **Missing `import board`** in device-specific encoders
- **ATTACKMODE command handling** - now properly triggers immediate execution
- **Production mode not being passed** to device-specific encoders
- **Invalid keycode usage** (COMMENT, ATTACKMODE) in generated code
- **Redundant file cleanup** - removed unused test files and sample outputs

### Removed
- **`ducky_parser/` directory** - redundant parser with limited functionality
- **`compiled/output.sample.py`** - outdated sample files
- **`test_production.py`** - redundant test file
- **Unused test materials** and redundant text files

## [0.1.0] - 2024-01-XX

### Added
- **Happy Frog Script parser and encoder**
- **Support for multiple microcontroller platforms**:
  - Xiao RP2040 (CircuitPython)
  - ESP32 (Arduino)
  - Arduino Leonardo
  - Raspberry Pi Pico
  - Teensy 4
  - Digispark
  - Evil Crow Cable
- **Educational payload examples**
- **Command-line interface**
- **Comprehensive test suite**

### Features
- **Script parsing and validation**
- **Device-specific code generation**
- **Educational HID emulation framework**
- **Cross-platform compatibility**
- **Ethical cybersecurity education tools**

---

## Version History

- **0.2.7**: Production Ready: All devices production-ready, EvilCrow-Cable specialty commands, enhanced parser
- **0.2.6**: Bleeding Edge: enhanced CLI, device-specific encoders, payload list/download 
- **0.2.4**: Stable: Production packaging, ATTACKMODE support
- **0.1.0**: Initial release with core functionality

## Release Process

1. Update version in `happy_frog_parser/_version.py`
2. Update this CHANGELOG.md
3. Create git tag: `git tag v0.2.7`
4. Push tag: `git push origin v0.2.7`
5. Build package: `python -m build`
6. Upload to PyPI: `twine upload dist/*`

## Semantic Versioning

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in backward-compatible manner
- **PATCH**: Backward-compatible bug fixes

## Documentation Structure

### Current Documentation Files
- **README.md**: Project overview, differentiation from USB Rubber Ducky, quick start
- **docs/usage.md**: Comprehensive user guide (merged from HELLO_HAPPY_FROG.md)
- **docs/microcontrollers.md**: Hardware setup and device support (merged from devices/README)
- **docs/DEVELOPMENT.md**: Developer guide and integration (renamed from INSTALL.md)
- **DISCLAIMER.md**: Legal and ethical guidelines
- **CHANGELOG.md**: This file - project change history

### Removed Documentation Files
- `docs/HELLO_HAPPY_FROG.md` - Content merged into usage.md
- `docs/How_We_Are_Different.md` - Content merged into README.md
- `devices/README` - Content merged into microcontrollers.md
- `docs/INSTALL.md` - Renamed and updated to DEVELOPMENT.md 
