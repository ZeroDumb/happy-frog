# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Production-ready packaging configuration
- Clean dependency management
- Proper version control
- **ATTACKMODE support** for immediate execution on device boot
- **Production mode** for generating immediate execution code (no main() function)
- **Educational mode** with enhanced safety features and detailed comments
- **Device-specific encoders** with production mode support
- **Xiao RP2040 encoder** with proper ATTACKMODE detection and import board support

### Changed
- Excluded development files from package distribution
- Updated development status to Beta
- Streamlined package structure
- **Deprecated and removed redundant `ducky_parser`** - consolidated to single `happy_frog_parser`
- **Enhanced ATTACKMODE handling** - flexible regex pattern vs restrictive pattern
- **Improved code generation** - template-based system with production/educational modes
- **Updated device manager** to support production mode for device-specific encoders

### Fixed
- Import issues with device modules
- Conditional CircuitPython imports for host compatibility
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
- Happy Frog Script parser and encoder
- Support for multiple microcontroller platforms:
  - Xiao RP2040 (CircuitPython)
  - ESP32 (Arduino)
  - Arduino Leonardo
  - Raspberry Pi Pico
  - Teensy 4
  - Digispark
  - Evil Crow Cable
- Educational payload examples
- Command-line interface
- Comprehensive test suite

### Features
- Script parsing and validation
- Device-specific code generation
- Educational HID emulation framework
- Cross-platform compatibility
- Ethical cybersecurity education tools

---

## Version History

- **0.1.0**: Initial release with core functionality
- **Unreleased**: Production packaging improvements, ATTACKMODE integration, ducky_parser deprecation

## Release Process

1. Update version in `happy_frog_parser/_version.py`
2. Update this CHANGELOG.md
3. Create git tag: `git tag v0.1.8`
4. Push tag: `git push origin v0.1.8`
5. Build package: `python -m build`
6. Upload to PyPI: `twine upload dist/*`

## Semantic Versioning

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in backward-compatible manner
- **PATCH**: Backward-compatible bug fixes 