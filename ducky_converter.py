#!/usr/bin/env python3
"""
Happy Frog - Ducky Script Converter

This module provides reliable conversion from Ducky Script syntax to Happy Frog Script syntax.
It includes safety validation, educational warnings, and maintains the educational focus
of the Happy Frog project.

Educational Purpose: This demonstrates script conversion, syntax parsing, and
safety validation techniques used in development tools.

Author: ZeroDumb
License: GNU GPLv3
"""

import re
import os
from typing import List, Dict, Tuple, Optional
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ConversionWarning:
    """Represents a warning during Ducky Script conversion."""
    line_number: int
    warning_type: str
    message: str
    severity: str  # 'info', 'warning', 'danger'


class DuckyConverter:
    """
    Converts Ducky Script syntax to Happy Frog Script syntax.
    
    This converter handles the translation of Ducky Script commands to their
    Happy Frog Script equivalents while providing safety validation and
    educational guidance.
    """
    
    def __init__(self):
        """Initialize the converter with command mappings and patterns."""
        # Ducky Script to Happy Frog Script command mappings
        self.command_mappings = {
            # Modifier key mappings
            'WINDOWS': 'MOD',
            'GUI': 'MOD',
            'COMMAND': 'MOD',  # macOS equivalent
            
            # Comment mappings
            'REM': '#',
            
            # Commands that are the same in both
            'DELAY': 'DELAY',
            'STRING': 'STRING',
            'ENTER': 'ENTER',
            'SPACE': 'SPACE',
            'TAB': 'TAB',
            'BACKSPACE': 'BACKSPACE',
            'DELETE': 'DELETE',
            
            # Arrow keys (with Ducky alternatives)
            'UP': 'UP',
            'UPARROW': 'UP',  # Ducky alternative
            'DOWN': 'DOWN',
            'DOWNARROW': 'DOWN',  # Ducky alternative
            'LEFT': 'LEFT',
            'LEFTARROW': 'LEFT',  # Ducky alternative
            'RIGHT': 'RIGHT',
            'RIGHTARROW': 'RIGHT',  # Ducky alternative
            
            # Navigation keys
            'HOME': 'HOME',
            'END': 'END',
            'INSERT': 'INSERT',
            'PAGE_UP': 'PAGE_UP',
            'PAGEUP': 'PAGE_UP',  # Ducky alternative
            'PAGE_DOWN': 'PAGE_DOWN',
            'PAGEDOWN': 'PAGE_DOWN',  # Ducky alternative
            'ESCAPE': 'ESCAPE',
            'ESC': 'ESCAPE',  # Ducky alternative
            
            # Function keys
            'F1': 'F1', 'F2': 'F2', 'F3': 'F3', 'F4': 'F4',
            'F5': 'F5', 'F6': 'F6', 'F7': 'F7', 'F8': 'F8',
            'F9': 'F9', 'F10': 'F10', 'F11': 'F11', 'F12': 'F12',
            
            # Modifier keys
            'CTRL': 'CTRL', 'CONTROL': 'CTRL',  # Ducky alternative
            'SHIFT': 'SHIFT',
            'ALT': 'ALT',
            
            # Additional Ducky commands that we should support
            'PAUSE': 'PAUSE',  # Ducky command for pausing execution
            'BREAK': 'PAUSE',  # Alternative to PAUSE
            
            # Advanced Ducky Script features
            'REPEAT': 'REPEAT',  # Repeat previous command
            'DEFAULT_DELAY': 'DEFAULT_DELAY',  # Set default delay
            'DEFAULTDELAY': 'DEFAULT_DELAY',  # Alternative syntax
        }
        
        # Patterns for detecting potentially dangerous commands
        self.dangerous_patterns = {
            'network_access': [
                r'http[s]?://',
                r'ftp://',
                r'invoke-webrequest',
                r'curl',
                r'wget',
            ],
            'system_modification': [
                r'reg\s+add',
                r'reg\s+delete',
                r'reg\s+edit',
                r'rundll32',
                r'system32',
                r'%systemroot%',
                r'%programfiles%',
            ],
            'process_execution': [
                r'start\s+',
                r'cmd\s+/c',
                r'powershell\s+-command',
                r'powershell\s+-c',
                r'exec',
                r'runas',
            ],
            'file_operations': [
                r'del\s+/s',
                r'rmdir\s+/s',
                r'format\s+',
                r'copy\s+.*\s+%system',
                r'move\s+.*\s+%system',
            ],
        }
        
        # Educational warnings for different command types
        self.educational_warnings = {
            'network_access': "Network access detected. This could download files or communicate with external servers.",
            'system_modification': "System modification detected. This could change system settings or registry.",
            'process_execution': "Process execution detected. This could run programs or commands.",
            'file_operations': "File operations detected. This could modify or delete files.",
        }
    
    def convert_file(self, input_file: str, output_file: Optional[str] = None) -> Tuple[str, List[ConversionWarning]]:
        """
        Convert a Ducky Script file to Happy Frog Script format.
        
        Args:
            input_file: Path to the input Ducky Script file
            output_file: Optional output file path (auto-generated if not provided)
            
        Returns:
            Tuple of (converted_content, warnings)
            
        Raises:
            FileNotFoundError: If input file doesn't exist
            ValueError: If conversion fails
        """
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Ducky Script file not found: {input_file}")
        
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert the content
        converted_content, warnings = self.convert_string(content, input_file)
        
        # Determine output file
        if not output_file:
            input_path = Path(input_file)
            output_file = input_path.with_name(f"{input_path.stem}_converted{input_path.suffix}")
        
        # Write the converted content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        return converted_content, warnings
    
    def convert_string(self, content: str, source_name: str = "<string>") -> Tuple[str, List[ConversionWarning]]:
        """
        Convert Ducky Script content to Happy Frog Script format.
        
        Args:
            content: Ducky Script content as string
            source_name: Name of the source (for error reporting)
            
        Returns:
            Tuple of (converted_content, warnings)
        """
        lines = content.split('\n')
        converted_lines = []
        warnings = []
        
        for line_number, line in enumerate(lines, 1):
            original_line = line
            converted_line = line
            
            # Convert the line
            converted_line, line_warnings = self._convert_line(line, line_number, source_name)
            
            # Add educational header for the first line
            if line_number == 1:
                converted_lines.append("# Happy Frog Script - Converted from Ducky Script")
                converted_lines.append(f"# Original source: {source_name}")
                converted_lines.append("# Educational conversion - review all commands before execution")
                converted_lines.append("")
            
            converted_lines.append(converted_line)
            warnings.extend(line_warnings)
        
        # Add educational footer
        converted_lines.append("")
        converted_lines.append("# Conversion completed by Happy Frog")
        converted_lines.append("# Remember: Use only for educational purposes and authorized testing!")
        
        return '\n'.join(converted_lines), warnings
    
    def _convert_line(self, line: str, line_number: int, source_name: str) -> Tuple[str, List[ConversionWarning]]:
        """
        Convert a single line from Ducky Script to Happy Frog Script.
        
        Args:
            line: The line to convert
            line_number: Line number for error reporting
            source_name: Source name for error reporting
            
        Returns:
            Tuple of (converted_line, warnings)
        """
        warnings = []
        converted_line = line.strip()
        
        # Skip empty lines
        if not converted_line:
            return line, warnings
        
        # Handle comments (REM -> #)
        if converted_line.upper().startswith('REM '):
            converted_line = converted_line.replace('REM ', '# ', 1)
            return converted_line, warnings
        
        # Handle WINDOWS/GUI commands
        if converted_line.upper().startswith('WINDOWS '):
            converted_line = converted_line.replace('WINDOWS ', 'MOD ', 1)
            warnings.append(ConversionWarning(
                line_number=line_number,
                warning_type='command_conversion',
                message='WINDOWS command converted to MOD (Happy Frog Script syntax)',
                severity='info'
            ))
        elif converted_line.upper().startswith('GUI '):
            converted_line = converted_line.replace('GUI ', 'MOD ', 1)
            warnings.append(ConversionWarning(
                line_number=line_number,
                warning_type='command_conversion',
                message='GUI command converted to MOD (Happy Frog Script syntax)',
                severity='info'
            ))
        elif converted_line.upper().startswith('COMMAND '):
            converted_line = converted_line.replace('COMMAND ', 'MOD ', 1)
            warnings.append(ConversionWarning(
                line_number=line_number,
                warning_type='command_conversion',
                message='COMMAND command converted to MOD (Happy Frog Script syntax)',
                severity='info'
            ))
        
        # Add stealth conversion for PowerShell commands
        if converted_line.upper().startswith('STRING ') and 'powershell' in converted_line.lower():
            converted_line = self._add_stealth_to_powershell(converted_line)
            warnings.append(ConversionWarning(
                line_number=line_number,
                warning_type='stealth_conversion',
                message='PowerShell command converted to stealth mode (hidden window)',
                severity='info'
            ))
        
        # Check for potentially dangerous commands
        if converted_line.upper().startswith('STRING '):
            string_content = converted_line[7:]  # Remove 'STRING ' prefix
            danger_warnings = self._check_dangerous_content(string_content, line_number)
            warnings.extend(danger_warnings)
        
        return converted_line, warnings
    
    def _add_stealth_to_powershell(self, line: str) -> str:
        """
        Add stealth options to PowerShell commands.
        
        Args:
            line: The original STRING line containing PowerShell
            
        Returns:
            Modified line with stealth options
        """
        # Extract the PowerShell command
        if line.upper().startswith('STRING '):
            command = line[7:]  # Remove 'STRING ' prefix
            
            # Add stealth options to PowerShell commands
            if 'powershell' in command.lower():
                # Replace basic PowerShell with stealth version
                if 'powershell -command' in command.lower():
                    command = command.replace('powershell -command', 'powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command')
                elif 'powershell -c' in command.lower():
                    command = command.replace('powershell -c', 'powershell -WindowStyle Hidden -NoProfile -NonInteractive -Command')
                elif 'powershell' in command.lower() and not any(flag in command.lower() for flag in ['-windowstyle', '-noprofile', '-noninteractive']):
                    # Add stealth flags to basic PowerShell
                    command = command.replace('powershell', 'powershell -WindowStyle Hidden -NoProfile -NonInteractive')
                
                # For commands that should run silently, add Start-Process wrapper
                if any(keyword in command.lower() for keyword in ['invoke-webrequest', 'reg add', 'rundll32']):
                    # Wrap in Start-Process for silent execution
                    command = f'Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile", "-NonInteractive", "-Command", "{command}" -Wait'
            
            return f'STRING {command}'
        
        return line
    
    def _check_dangerous_content(self, content: str, line_number: int) -> List[ConversionWarning]:
        """
        Check string content for potentially dangerous commands.
        
        Args:
            content: The string content to check
            line_number: Line number for warning reporting
            
        Returns:
            List of conversion warnings
        """
        warnings = []
        content_lower = content.lower()
        
        for danger_type, patterns in self.dangerous_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content_lower, re.IGNORECASE):
                    warnings.append(ConversionWarning(
                        line_number=line_number,
                        warning_type='dangerous_command',
                        message=f"{self.educational_warnings[danger_type]} Pattern: {pattern}",
                        severity='warning'
                    ))
        
        # Special check for PowerShell commands
        if 'powershell' in content_lower:
            warnings.append(ConversionWarning(
                line_number=line_number,
                warning_type='powershell_command',
                message='PowerShell command detected. Review carefully - this can execute system commands.',
                severity='warning'
            ))
        
        return warnings
    
    def validate_conversion(self, original_content: str, converted_content: str) -> List[ConversionWarning]:
        """
        Validate the conversion process and results.
        
        Args:
            original_content: Original Ducky Script content
            converted_content: Converted Happy Frog Script content
            
        Returns:
            List of validation warnings
        """
        warnings = []
        
        # Check if conversion preserved all non-empty lines
        original_lines = [line.strip() for line in original_content.split('\n') if line.strip()]
        converted_lines = [line.strip() for line in converted_content.split('\n') if line.strip() and not line.startswith('#')]
        
        # Remove educational headers/footers from converted lines for comparison
        converted_lines = [line for line in converted_lines if not line.startswith('# Happy Frog Script') and 
                          not line.startswith('# Original source:') and 
                          not line.startswith('# Educational conversion') and
                          not line.startswith('# Conversion completed') and
                          not line.startswith('# Remember:')]
        
        if len(original_lines) != len(converted_lines):
            warnings.append(ConversionWarning(
                line_number=0,
                warning_type='conversion_validation',
                message=f'Line count mismatch: Original {len(original_lines)} lines, Converted {len(converted_lines)} lines',
                severity='warning'
            ))
        
        return warnings
    
    def print_conversion_report(self, warnings: List[ConversionWarning], source_name: str):
        """
        Print a detailed conversion report.
        
        Args:
            warnings: List of conversion warnings
            source_name: Name of the source file
        """
        print(f"\n🐸 Ducky Script Conversion Report")
        print(f"📁 Source: {source_name}")
        print(f"📊 Total Warnings: {len(warnings)}")
        
        if not warnings:
            print("✅ No warnings - conversion completed successfully!")
            return
        
        # Group warnings by severity
        info_warnings = [w for w in warnings if w.severity == 'info']
        warning_warnings = [w for w in warnings if w.severity == 'warning']
        danger_warnings = [w for w in warnings if w.severity == 'danger']
        
        if info_warnings:
            print(f"\nℹ️  Information ({len(info_warnings)}):")
            for warning in info_warnings:
                print(f"   Line {warning.line_number}: {warning.message}")
        
        if warning_warnings:
            print(f"\n⚠️  Warnings ({len(warning_warnings)}):")
            for warning in warning_warnings:
                print(f"   Line {warning.line_number}: {warning.message}")
        
        if danger_warnings:
            print(f"\n🚨 High Risk ({len(danger_warnings)}):")
            for warning in danger_warnings:
                print(f"   Line {warning.line_number}: {warning.message}")
        
        print(f"\n💡 Educational Note:")
        print("   - Review all converted commands before execution")
        print("   - Test in a controlled environment first")
        print("   - Ensure you have proper authorization")
        print("   - Use responsibly and ethically!")


def main():
    """Command-line interface for the Ducky Script converter."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Convert Ducky Script files to Happy Frog Script format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s convert ducky_script.txt
  %(prog)s convert ducky_script.txt -o happy_frog_script.txt
  %(prog)s convert ducky_script.txt --verbose

Educational Purpose:
  This tool demonstrates script conversion and safety validation techniques.
  Use only for authorized educational and testing purposes.
        """
    )
    
    parser.add_argument('input_file', help='Input Ducky Script file (.txt)')
    parser.add_argument('-o', '--output', help='Output Happy Frog Script file (.txt)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    try:
        converter = DuckyConverter()
        converted_content, warnings = converter.convert_file(args.input_file, args.output)
        
        # Print conversion report
        converter.print_conversion_report(warnings, args.input_file)
        
        if args.output:
            print(f"\n✅ Successfully converted to: {args.output}")
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


if __name__ == '__main__':
    exit(main()) 