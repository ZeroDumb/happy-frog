#!/usr/bin/env python3
"""
Happy Frog - Command Line Interface

A simple CLI for parsing and encoding Happy Frog Script files into CircuitPython code.

Educational Purpose: This demonstrates how to create user-friendly command-line
interfaces for development tools, including argument parsing, error handling,
and user feedback.

Author: ZeroDumb
License: GNU GPLv3
"""

import argparse
import sys
import os
from pathlib import Path
import shutil
import importlib.resources as pkg_resources

# Import our modules directly since we're in the root directory
from happy_frog_parser import HappyFrogParser, CircuitPythonEncoder, HappyFrogScriptError, EncoderError
from ducky_converter import DuckyConverter
from devices.device_manager import DeviceManager

# For compatibility with both source and installed packages
try:
    import payloads
except ImportError:
    payloads = None


def print_welcome_banner():
    """Print the Happy Frog welcome banner with ASCII art."""
    try:
        banner = """
    ╔═════════════════════════════════════════════════════════╗
    ║                    🐸 Happy Frog 🐸                     ║
    ║            Educational HID Emulation Framework          ║
    ╚═════════════════════════════════════════════════════════╝

🎓 Educational Purpose: Learn HID emulation and cybersecurity concepts
⚡ Simple Scripting: Easy-to-learn automation language
🔒 Safe Testing: Built-in validation and ethical guidelines
📚 Open Source: Free educational tool for everyone

⚠️  IMPORTANT: Use only for EDUCATIONAL PURPOSES and AUTHORIZED TESTING!
"""
        print(banner)
    except UnicodeEncodeError:
        # Fallback banner without Unicode characters
        fallback_banner = """
    +=========================================================+
    |                    Happy Frog                           |
    |            Educational HID Emulation Framework          |
    +=========================================================+

Educational Purpose: Learn HID emulation and cybersecurity concepts
Simple Scripting: Easy-to-learn automation language
Safe Testing: Built-in validation and ethical guidelines
Open Source: Free educational tool for everyone

IMPORTANT: Use only for EDUCATIONAL PURPOSES and AUTHORIZED TESTING!
"""
        print(fallback_banner)


def main():
    """Main CLI entry point."""
    # Print welcome banner
    print_welcome_banner()
    
    parser = argparse.ArgumentParser(
        description="Happy Frog - Educational HID Script Parser and Encoder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s parse payloads/demo_automation.txt
  %(prog)s encode payloads/demo_automation.txt
  %(prog)s encode payloads/demo_automation.txt -d xiao_rp2040
  %(prog)s encode payloads/demo_automation.txt -o custom_output.py
  %(prog)s validate payloads/demo_automation.txt
  %(prog)s convert ducky_script.txt
  %(prog)s encode example_payload.txt -d xiao_rp2040 -p (production mode)
  %(prog)s list-payloads
  %(prog)s copy-payload example_payload.txt /path/to/destination

Device Selection:
  Use --device (-d) to generate code for specific microcontrollers:
  - xiao_rp2040: Seeed Xiao RP2040 (recommended)
  - raspberry_pi_pico: Raspberry Pi Pico
  - arduino_leonardo: Arduino Leonardo
  - teensy_4: Teensy 4.0
  - digispark: DigiSpark
  - esp32: ESP32
  - evilcrow_cable: EvilCrow-Cable (BadUSB device)

Educational Purpose:
  This tool demonstrates parsing, code generation, and CLI development concepts.
  Use only for authorized educational and testing purposes.
        """
    )
    
    # Add subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Parse command
    parse_parser = subparsers.add_parser('parse', 
                                       help='Parse a Happy Frog Script file',
                                       formatter_class=argparse.RawDescriptionHelpFormatter,
                                       description='Parse and analyze a Happy Frog Script file to show its structure and validate syntax.')
    parse_parser.add_argument('input_file', help='Input Happy Frog Script file (.txt)')
    parse_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output showing detailed command breakdown')
    
    # Encode command
    encode_parser = subparsers.add_parser('encode', 
                                         help='Encode a Happy Frog Script to device-specific code',
                                         formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description='Convert a Happy Frog Script into executable code for specific microcontrollers.')
    encode_parser.add_argument('input_file', help='Input Happy Frog Script file (.txt)')
    encode_parser.add_argument('-o', '--output', help='Output file path (default: compiled/input_name.py)')
    encode_parser.add_argument('--device', '-d', 
                              help='Target device: xiao_rp2040, raspberry_pi_pico, arduino_leonardo, teensy_4, digispark, esp32, evilcrow_cable')
    encode_parser.add_argument('--production', '-p', action='store_true', 
                              help='Generate production-ready code (runs immediately on boot with ATTACKMODE)')
    encode_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output showing generated code preview')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', 
                                           help='Validate a Happy Frog Script file',
                                           formatter_class=argparse.RawDescriptionHelpFormatter,
                                           description='Check a Happy Frog Script for syntax errors and potential issues.')
    validate_parser.add_argument('input_file', help='Input Happy Frog Script file (.txt)')
    validate_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output showing detailed validation results')
    
    # Convert command
    convert_parser = subparsers.add_parser('convert', 
                                          help='Convert Ducky Script to Happy Frog Script',
                                          formatter_class=argparse.RawDescriptionHelpFormatter,
                                          description='Convert legacy Ducky Script files to modern Happy Frog Script format.')
    convert_parser.add_argument('input_file', help='Input Ducky Script file (.txt)')
    convert_parser.add_argument('-o', '--output', help='Output Happy Frog Script file (.txt)')
    convert_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output showing conversion details')
    
    # List payloads command
    list_payloads_parser = subparsers.add_parser('list-payloads',
        help='List all available sample payloads',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='List all .txt payloads included with Happy Frog.')

    # Copy payload command
    copy_payload_parser = subparsers.add_parser('copy-payload',
        help='Copy a sample payload to a destination',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Copy a sample payload file to a specified destination path.')
    copy_payload_parser.add_argument('payload_name', help='Name of the payload file (e.g., hello_world.txt)')
    copy_payload_parser.add_argument('destination', help='Destination file path')

    # Parse arguments
    args = parser.parse_args()
    
    # If no command specified, show help
    if not args.command:
        parser.print_help()
        return 1
    
    try:
        # Execute the appropriate command
        if args.command == 'parse':
            return parse_command(args)
        elif args.command == 'encode':
            return encode_command(args)
        elif args.command == 'validate':
            return validate_command(args)
        elif args.command == 'convert':
            return convert_command(args)
        elif args.command == 'list-payloads':
            return list_payloads_command()
        elif args.command == 'copy-payload':
            return copy_payload_command(args)
        else:
            print(f"Unknown command: {args.command}")
            return 1
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def parse_command(args):
    """Handle the parse command."""
    try:
        # Check if input file exists
        if not os.path.exists(args.input_file):
            print(f"Error: Input file '{args.input_file}' not found.")
            return 1
        
        # Parse the script
        parser = HappyFrogParser()
        script = parser.parse_file(args.input_file)
        
        # Display results
        print(f"✅ Successfully parsed '{args.input_file}'")
        print(f"📊 Script Statistics:")
        print(f"   Total Commands: {len(script.commands)}")
        print(f"   Total Lines: {script.metadata.get('total_lines', 'Unknown')}")
        print(f"   Source: {script.metadata.get('source', 'Unknown')}")
        
        if args.verbose:
            print(f"\n📝 Commands:")
            for i, cmd in enumerate(script.commands, 1):
                print(f"   {i:2d}. {cmd.command_type.value}: {cmd.raw_text}")
        
        # Show validation warnings
        warnings = parser.validate_script(script)
        if warnings:
            print(f"\n⚠️  Warnings:")
            for warning in warnings:
                print(f"   {warning}")
        
        return 0
        
    except HappyFrogScriptError as e:
        print(f"❌ Parse Error: {e}")
        return 1


def encode_command(args):
    """Handle the encode command."""
    try:
        # Check if input file exists
        if not os.path.exists(args.input_file):
            print(f"Error: Input file '{args.input_file}' not found.")
            return 1
        
        # Parse the script
        parser = HappyFrogParser()
        script = parser.parse_file(args.input_file)
        
        # Determine output file
        if args.output:
            output_file = args.output
        else:
            # Generate output filename from input and save to compiled/ directory
            input_path = Path(args.input_file)
            # Determine appropriate extension based on device
            if args.device:
                # Use .ino for Arduino-based devices, .py for CircuitPython
                if args.device in ['arduino_leonardo', 'teensy_4', 'digispark', 'evilcrow_cable']:
                    extension = '.ino'
                else:
                    extension = '.py'
            else:
                extension = '.py'  # Default CircuitPython
            
            output_filename = input_path.stem + extension
            output_file = Path('compiled') / output_filename
        
        # Choose encoder based on device specification
        if args.device:
            # Use device-specific encoder
            device_manager = DeviceManager()
            try:
                # Set production mode if requested
                if args.production:
                    print(f"🔧 Production mode enabled - code will run immediately on boot")
                
                code = device_manager.encode_script(script, args.device, output_file, args.production)
                device_info = device_manager.get_device_info(args.device)
                device_name = device_info['name'] if device_info else args.device
                mode = "production" if args.production else "educational"
                print(f"✅ Successfully encoded '{args.input_file}' for {device_name} to '{output_file}' ({mode} mode)")
            except ValueError as e:
                print(f"❌ Device Error: {e}")
                print(f"Available devices:")
                for device in device_manager.list_devices():
                    print(f"   - {device['id']}: {device['name']}")
                return 1
        else:
            # Use default CircuitPython encoder
            encoder = CircuitPythonEncoder()
            
            # Set production mode if requested
            if args.production:
                encoder.set_production_mode(True)
                print(f"🔧 Production mode enabled - code will run immediately on boot")
            
            code = encoder.encode(script, output_file)
            mode = "production" if args.production else "educational"
            print(f"✅ Successfully encoded '{args.input_file}' to '{output_file}' ({mode} mode)")
        
        # Display results
        print(f"📊 Encoding Statistics:")
        print(f"   Input Commands: {len(script.commands)}")
        print(f"   Output Lines: {len(code.split(chr(10)))}")
        
        if args.verbose:
            print(f"\n📝 Generated Code Preview:")
            lines = code.split(chr(10))
            for i, line in enumerate(lines[:20], 1):  # Show first 20 lines
                print(f"   {i:2d}: {line}")
            if len(lines) > 20:
                print(f"   ... ({len(lines) - 20} more lines)")
        
        # Show validation warnings
        if args.device:
            device_manager = DeviceManager()
            warnings = device_manager.validate_device_support(args.device, script)
        else:
            encoder = CircuitPythonEncoder()
            warnings = encoder.validate_script(script)
            
        if warnings:
            print(f"\n⚠️  Warnings:")
            for warning in warnings:
                print(f"   {warning}")
        
        return 0
        
    except (HappyFrogScriptError, EncoderError) as e:
        print(f"❌ Encode Error: {e}")
        return 1


def validate_command(args):
    """Handle the validate command."""
    try:
        # Check if input file exists
        if not os.path.exists(args.input_file):
            print(f"Error: Input file '{args.input_file}' not found.")
            return 1
        
        # Parse the script
        parser = HappyFrogParser()
        script = parser.parse_file(args.input_file)
        
        # Validate the script
        parser_warnings = parser.validate_script(script)
        encoder = CircuitPythonEncoder()
        encoder_warnings = encoder.validate_script(script)
        
        # Display results
        print(f"✅ Successfully validated '{args.input_file}'")
        print(f"📊 Validation Results:")
        print(f"   Total Commands: {len(script.commands)}")
        print(f"   Parser Warnings: {len(parser_warnings)}")
        print(f"   Encoder Warnings: {len(encoder_warnings)}")
        
        # Show warnings
        all_warnings = parser_warnings + encoder_warnings
        if all_warnings:
            print(f"\n⚠️  Warnings:")
            for warning in all_warnings:
                print(f"   {warning}")
        else:
            print(f"\n✅ No warnings found!")
        
        if args.verbose:
            print(f"\n📝 Command Summary:")
            command_counts = {}
            for cmd in script.commands:
                cmd_type = cmd.command_type.value
                command_counts[cmd_type] = command_counts.get(cmd_type, 0) + 1
            
            for cmd_type, count in sorted(command_counts.items()):
                print(f"   {cmd_type}: {count}")
        
        return 0
        
    except HappyFrogScriptError as e:
        print(f"❌ Validation Error: {e}")
        return 1


def convert_command(args):
    """Handle the convert command (Ducky Script to Happy Frog Script)."""
    try:
        # Check if input file exists
        if not os.path.exists(args.input_file):
            print(f"Error: Input file '{args.input_file}' not found.")
            return 1
        
        # Convert the Ducky Script
        converter = DuckyConverter()
        converted_content, warnings = converter.convert_file(args.input_file, args.output)
        
        # Print conversion report
        converter.print_conversion_report(warnings, args.input_file)
        
        # Determine the actual output file path (where it was actually saved)
        if args.output:
            output_file = args.output
        else:
            input_path = Path(args.input_file)
            output_file = input_path.with_name(f"{input_path.stem}_converted{input_path.suffix}")
        
        print(f"\n✅ Successfully converted to: {output_file}")
        
        if args.verbose:
            print(f"\n📝 Converted Content Preview:")
            lines = converted_content.split('\n')
            for i, line in enumerate(lines[:20], 1):
                print(f"   {i:2d}: {line}")
            if len(lines) > 20:
                print(f"   ... ({len(lines) - 20} more lines)")
        
        return 0
        
    except Exception as e:
        print(f"❌ Conversion Error: {e}")
        return 1


def list_payloads_command():
    """List all .txt payloads included in the package."""
    try:
        if payloads is None:
            print("Error: Could not import payloads package.")
            return 1
        payload_list = [name for name in pkg_resources.contents('payloads') if name.endswith('.txt')]
        if not payload_list:
            print("No payloads found.")
            return 0
        print("Available payloads:")
        for name in sorted(payload_list):
            print(f"  {name}")
        return 0
    except Exception as e:
        print(f"Error listing payloads: {e}")
        return 1


def copy_payload_command(args):
    """Copy a payload file to the specified destination."""
    try:
        if payloads is None:
            print("Error: Could not import payloads package.")
            return 1
        payload_name = args.payload_name
        dest_path = args.destination
        # Check if payload exists
        payload_list = [name for name in pkg_resources.contents('payloads') if name.endswith('.txt')]
        if payload_name not in payload_list:
            print(f"Payload '{payload_name}' not found. Use 'list-payloads' to see available payloads.")
            return 1
        # Read the payload and write to destination
        with pkg_resources.open_binary('payloads', payload_name) as src, open(dest_path, 'wb') as dst:
            shutil.copyfileobj(src, dst)
        print(f"Copied '{payload_name}' to '{dest_path}'")
        return 0
    except Exception as e:
        print(f"Error copying payload: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main()) 