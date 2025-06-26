"""
Happy Frog - CircuitPython Encoder

This module converts parsed Happy Frog Script commands into CircuitPython code that can
be executed on microcontrollers like the Seeed Xiao RP2040.

Educational Purpose: This demonstrates code generation, microcontroller programming,
and how to translate high-level commands into low-level hardware operations.

Author: ZeroDumb
License: GNU GPLv3
"""

from typing import List, Dict, Any, Optional
from .parser import HappyFrogScript, HappyFrogCommand, CommandType


class EncoderError(Exception):
    """Custom exception for encoding errors."""
    pass


class CircuitPythonEncoder:
    """
    Encoder that converts parsed Happy Frog Script commands into CircuitPython code.
    
    This encoder generates human-readable CircuitPython code that can be directly
    uploaded to compatible microcontrollers. It includes educational comments
    to help users understand how each command works.
    """
    
    def __init__(self):
        """Initialize the encoder with key mappings and templates."""
        # USB HID key codes for CircuitPython
        self.key_codes = {
            # Basic keys
            CommandType.ENTER: "Keycode.ENTER",
            CommandType.SPACE: "Keycode.SPACE",
            CommandType.TAB: "Keycode.TAB",
            CommandType.BACKSPACE: "Keycode.BACKSPACE",
            CommandType.DELETE: "Keycode.DELETE",
            
            # Arrow keys
            CommandType.UP: "Keycode.UP_ARROW",
            CommandType.DOWN: "Keycode.DOWN_ARROW",
            CommandType.LEFT: "Keycode.LEFT_ARROW",
            CommandType.RIGHT: "Keycode.RIGHT_ARROW",
            
            # Navigation keys
            CommandType.HOME: "Keycode.HOME",
            CommandType.END: "Keycode.END",
            CommandType.INSERT: "Keycode.INSERT",
            CommandType.PAGE_UP: "Keycode.PAGE_UP",
            CommandType.PAGE_DOWN: "Keycode.PAGE_DOWN",
            CommandType.ESCAPE: "Keycode.ESCAPE",
            
            # Function keys
            CommandType.F1: "Keycode.F1",
            CommandType.F2: "Keycode.F2",
            CommandType.F3: "Keycode.F3",
            CommandType.F4: "Keycode.F4",
            CommandType.F5: "Keycode.F5",
            CommandType.F6: "Keycode.F6",
            CommandType.F7: "Keycode.F7",
            CommandType.F8: "Keycode.F8",
            CommandType.F9: "Keycode.F9",
            CommandType.F10: "Keycode.F10",
            CommandType.F11: "Keycode.F11",
            CommandType.F12: "Keycode.F12",
            
            # Modifier keys
            CommandType.CTRL: "Keycode.CONTROL",
            CommandType.SHIFT: "Keycode.SHIFT",
            CommandType.ALT: "Keycode.ALT",
            CommandType.MOD: "Keycode.GUI",  # MOD maps to GUI (Windows/Command key)
            
            # Execution control
            CommandType.PAUSE: "PAUSE",  # Special handling for PAUSE command
        }
        
        # State for advanced features (set before templates)
        self.default_delay = 0  # Default delay between commands
        self.last_command = None  # For REPEAT functionality
        self.safe_mode = True  # Safe mode enabled by default
        
        # CircuitPython code templates
        self.templates = {
            'header': self._get_header_template(),
            'footer': self._get_footer_template(),
            'delay': self._get_delay_template(),
            'string': self._get_string_template(),
            'key_press': self._get_key_press_template(),
            'comment': self._get_comment_template(),
            'repeat': self._get_repeat_template(),
            'conditional': self._get_conditional_template(),
            'loop': self._get_loop_template(),
            'log': self._get_log_template(),
        }
    
    def set_production_mode(self, production: bool = True):
        """Set the encoder to production mode (disables safe mode)."""
        self.safe_mode = not production
        # Update templates for the new mode
        self.templates = {
            'header': self._get_header_template(),
            'footer': self._get_footer_template(),
            'delay': self._get_delay_template(),
            'string': self._get_string_template(),
            'key_press': self._get_key_press_template(),
            'comment': self._get_comment_template(),
            'repeat': self._get_repeat_template(),
            'conditional': self._get_conditional_template(),
            'loop': self._get_loop_template(),
            'log': self._get_log_template(),
        }
    
    def encode(self, script: HappyFrogScript, output_file: Optional[str] = None) -> str:
        """
        Encode a parsed Happy Frog Script into CircuitPython code.
        
        Args:
            script: Parsed HappyFrogScript object
            output_file: Optional output file path
            
        Returns:
            Generated CircuitPython code as string
            
        Raises:
            EncoderError: If encoding fails
        """
        try:
            # Generate the main code
            code_lines = []
            
            # Add header with educational comments
            code_lines.extend(self._generate_header(script))
            
            # Add main execution code
            code_lines.extend(self._generate_main_code(script))
            
            # Add footer
            code_lines.extend(self._generate_footer())
            
            # Join all lines
            code = '\n'.join(code_lines)
            
            # Write to file if specified
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(code)
            
            return code
            
        except Exception as e:
            raise EncoderError(f"Failed to encode script: {str(e)}")
    
    def _generate_header(self, script: HappyFrogScript) -> List[str]:
        """Generate the header section of the CircuitPython code."""
        lines = []
        
        # Add template header
        lines.extend(self.templates['header'].split('\n'))
        
        # Add script metadata as comments (only in safe mode)
        if self.safe_mode:
            lines.append("")
            lines.append("# Script Information:")
            lines.append(f"# Source: {script.metadata.get('source', 'Unknown')}")
            lines.append(f"# Total Commands: {script.metadata.get('total_commands', 0)}")
            lines.append(f"# Total Lines: {script.metadata.get('total_lines', 0)}")
            lines.append("")
        
        return lines
    
    def _generate_main_code(self, script: HappyFrogScript) -> List[str]:
        """Generate the main execution code from script commands."""
        lines = []
        
        # Check if ATTACKMODE HID STORAGE is present for immediate execution
        has_attackmode = any(
            cmd.command_type == CommandType.ATTACKMODE and 
            cmd.parameters and 
            'HID' in ' '.join(cmd.parameters).upper()
            for cmd in script.commands
        )
        
        if self.safe_mode:
            lines.append("# Main execution loop")
            lines.append("def main():")
            if self.safe_mode:
                lines.append("    # Wait for system to recognize the device")
            lines.append("    time.sleep(2)")
            lines.append("")
        else:
            if has_attackmode:
                lines.append("# Production code - executes immediately on device boot/plug-in")
                lines.append("# ATTACKMODE HID STORAGE detected - running payload automatically")
                lines.append("")
                lines.append("# Wait for system to recognize the device")
                lines.append("time.sleep(2)")
                lines.append("")
            else:
                lines.append("# Production code - main execution function")
                lines.append("def main():")
                lines.append("    # Wait for system to recognize the device")
                lines.append("    time.sleep(2)")
                lines.append("")
        
        # Process each command
        for i, command in enumerate(script.commands):
            lines.extend(self._encode_command(command, i + 1))
        
        lines.append("")
        
        return lines
    
    def _encode_command(self, command: HappyFrogCommand, command_index: int) -> List[str]:
        """Encode a single command into CircuitPython code."""
        lines = []
        
        # Add comment with original command (only in safe mode)
        if self.safe_mode:
            comment = f"    # Command {command_index}: {command.raw_text}"
            lines.append(comment)
        
        # Determine indentation based on mode
        indent = "    " if self.safe_mode else ""
        
        # Encode based on command type
        if command.command_type == CommandType.DELAY:
            lines.extend(self._encode_delay(command))
        elif command.command_type == CommandType.STRING:
            lines.extend(self._encode_string(command))
        elif command.command_type == CommandType.MODIFIER_COMBO:
            lines.extend(self._encode_modifier_combo(command))
        elif command.command_type == CommandType.PAUSE:
            lines.extend(self._encode_pause(command))
        elif command.command_type == CommandType.REPEAT:
            lines.extend(self._encode_repeat(command))
        elif command.command_type in [CommandType.DEFAULT_DELAY, CommandType.DEFAULTDELAY]:
            lines.extend(self._encode_default_delay(command))
        elif command.command_type == CommandType.IF:
            lines.extend(self._encode_if(command))
        elif command.command_type == CommandType.ELSE:
            lines.extend(self._encode_else(command))
        elif command.command_type == CommandType.ENDIF:
            lines.extend(self._encode_endif(command))
        elif command.command_type == CommandType.WHILE:
            lines.extend(self._encode_while(command))
        elif command.command_type == CommandType.ENDWHILE:
            lines.extend(self._encode_endwhile(command))
        elif command.command_type == CommandType.RANDOM_DELAY:
            lines.extend(self._encode_random_delay(command))
        elif command.command_type == CommandType.LOG:
            lines.extend(self._encode_log(command))
        elif command.command_type == CommandType.VALIDATE:
            lines.extend(self._encode_validate(command))
        elif command.command_type == CommandType.SAFE_MODE:
            lines.extend(self._encode_safe_mode(command))
        elif command.command_type == CommandType.ATTACKMODE:
            lines.extend(self._encode_attackmode(command))
        elif command.command_type in self.key_codes:
            lines.extend(self._encode_key_press(command))
        elif command.command_type in [CommandType.COMMENT, CommandType.REM]:
            lines.extend(self._encode_comment(command))
        else:
            # Unknown command - add warning comment (only in safe mode)
            if self.safe_mode:
                lines.append(f"    # WARNING: Unknown command '{command.command_type}'")
            lines.append("    pass")
        
        # Apply default delay after each command (except for DELAY, DEFAULT_DELAY, and comments)
        if (self.default_delay > 0 and 
            command.command_type not in [CommandType.DELAY, CommandType.DEFAULT_DELAY, CommandType.DEFAULTDELAY, 
                                        CommandType.COMMENT, CommandType.REM, CommandType.IF, CommandType.ELSE, 
                                        CommandType.ENDIF, CommandType.WHILE, CommandType.ENDWHILE]):
            lines.append(f"{indent}time.sleep(default_delay)  # Default delay: {self.default_delay}ms")
        
        lines.append("")  # Add blank line for readability
        return lines
    
    def _encode_delay(self, command: HappyFrogCommand) -> List[str]:
        """Encode a DELAY command."""
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise EncoderError("Delay value must be non-negative")
            
            indent = "    " if self.safe_mode else ""
            if self.safe_mode:
                return [
                    f"{indent}time.sleep({delay_ms / 1000.0})  # Delay for {delay_ms}ms"
                ]
            else:
                return [
                    f"{indent}time.sleep({delay_ms / 1000.0})  # Delay {delay_ms}ms"
                ]
        except (ValueError, IndexError):
            raise EncoderError(f"Invalid delay value '{command.parameters[0] if command.parameters else 'None'}' in command: {command.raw_text}")
    
    def _encode_string(self, command: HappyFrogCommand) -> List[str]:
        """Encode a STRING command."""
        if not command.parameters:
            raise EncoderError(f"STRING command missing text: {command.raw_text}")
        
        text = command.parameters[0]
        # Escape quotes and special characters
        escaped_text = text.replace('\\', '\\\\').replace('"', '\\"')
        
        indent = "    " if self.safe_mode else ""
        if self.safe_mode:
            return [
                f'{indent}keyboard_layout.write("{escaped_text}")  # Type: {text}'
            ]
        else:
            return [
                f'{indent}keyboard_layout.write("{escaped_text}")  # Type text'
            ]
    
    def _encode_pause(self, command: HappyFrogCommand) -> List[str]:
        """Encode a PAUSE command - wait for user input."""
        indent = "    " if self.safe_mode else ""
        if self.safe_mode:
            return [
                f"{indent}# PAUSE: Waiting for user input (press any key to continue)",
                f"{indent}# Note: In CircuitPython, we'll use a long delay as a simple pause",
                f"{indent}# For more sophisticated pause functionality, consider using button input",
                f"{indent}time.sleep(5)  # Pause for 5 seconds (Ducky Script PAUSE equivalent)"
            ]
        else:
            return [
                f"{indent}time.sleep(5)  # Pause execution"
            ]
    
    def _encode_modifier_combo(self, command: HappyFrogCommand) -> List[str]:
        """Encode a MODIFIER_COMBO command (e.g., MOD r, CTRL ALT DEL)."""
        if not command.parameters:
            raise EncoderError(f"MODIFIER_COMBO command missing parameters: {command.raw_text}")
        
        lines = []
        indent = "    " if self.safe_mode else ""
        
        # Press all keys in the combo
        for param in command.parameters:
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                # It's a modifier key
                key_code = self.key_codes.get(CommandType(param.upper()))
                if key_code:
                    if self.safe_mode:
                        lines.append(f"{indent}kbd.press({key_code})  # Press {param}")
                    else:
                        lines.append(f"{indent}kbd.press({key_code})  # Press {param}")
            else:
                # It's a regular key - map it to the appropriate keycode
                key_code = self._map_key_to_keycode(param)
                if key_code:
                    if self.safe_mode:
                        lines.append(f"{indent}kbd.press({key_code})  # Press {param}")
                    else:
                        lines.append(f"{indent}kbd.press({key_code})  # Press {param}")
        
        # Release all keys in reverse order
        for param in reversed(command.parameters):
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self.key_codes.get(CommandType(param.upper()))
                if key_code:
                    if self.safe_mode:
                        lines.append(f"{indent}kbd.release({key_code})  # Release {param}")
                    else:
                        lines.append(f"{indent}kbd.release({key_code})  # Release {param}")
            else:
                key_code = self._map_key_to_keycode(param)
                if key_code:
                    if self.safe_mode:
                        lines.append(f"{indent}kbd.release({key_code})  # Release {param}")
                    else:
                        lines.append(f"{indent}kbd.release({key_code})  # Release {param}")
        
        return lines
    
    def _map_key_to_keycode(self, key: str) -> str:
        """Map a key string to its CircuitPython keycode."""
        key = key.upper()
        
        # Single letter keys
        if len(key) == 1 and key.isalpha():
            return f"Keycode.{key}"
        
        # Number keys
        if key.isdigit():
            return f"Keycode.{key}"
        
        # Special mappings
        key_mappings = {
            'R': 'Keycode.R',
            'DEL': 'Keycode.DELETE',
            'BACKSPACE': 'Keycode.BACKSPACE',
            'ENTER': 'Keycode.ENTER',
            'SPACE': 'Keycode.SPACE',
            'TAB': 'Keycode.TAB',
            'ESC': 'Keycode.ESCAPE',
            'ESCAPE': 'Keycode.ESCAPE',
        }
        
        return key_mappings.get(key, f"Keycode.{key}")
    
    def _encode_key_press(self, command: HappyFrogCommand) -> List[str]:
        """Encode a key press command."""
        key_code = self.key_codes.get(command.command_type)
        if not key_code:
            raise EncoderError(f"Unsupported key: {command.command_type}")
        
        indent = "    " if self.safe_mode else ""
        if self.safe_mode:
            return [
                f"{indent}kbd.press({key_code})  # Press {command.command_type.value}",
                f"{indent}kbd.release({key_code})  # Release {command.command_type.value}"
            ]
        else:
            return [
                f"{indent}kbd.press({key_code})  # Press {command.command_type.value}",
                f"{indent}kbd.release({key_code})  # Release {command.command_type.value}"
            ]
    
    def _encode_comment(self, command: HappyFrogCommand) -> List[str]:
        """Encode a comment command."""
        comment_text = command.parameters[0] if command.parameters else ""
        indent = "    " if self.safe_mode else ""
        return [
            f"{indent}# {comment_text}"
        ]
    
    def _generate_footer(self) -> List[str]:
        """Generate the footer section of the CircuitPython code."""
        if self.safe_mode:
            return self.templates['footer'].split('\n')
        else:
            return ['"""', 'End of Happy Frog Generated Code', '"""']
    
    def _get_header_template(self) -> str:
        """Get the header template for CircuitPython code."""
        if self.safe_mode:
            return '''"""
Happy Frog - Generated CircuitPython Code
Educational HID Emulation Script

This code was automatically generated from a Happy Frog Script.
It demonstrates how to use CircuitPython for HID emulation.

⚠️ IMPORTANT: Use only for educational purposes and authorized testing!
"""

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize HID devices
kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)

# Educational note: This creates a virtual keyboard that the computer
# will recognize as a USB HID device. The keyboard can send keystrokes
# just like a physical keyboard would.'''
        else:
            return '''"""
Happy Frog - Production CircuitPython Code
Generated from Happy Frog Script

This code will execute automatically when the device is plugged in.
Educational comments show what each command does.
"""

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize HID devices
kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)'''
    
    def _get_footer_template(self) -> str:
        """Get the footer template for CircuitPython code."""
        if self.safe_mode:
            return '''if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error during execution: {e}')
        kbd.release_all()
    finally:
        kbd.release_all()
        print('Happy Frog execution completed.')

"""
End of Happy Frog Generated Code

Educational Notes:
- This script demonstrates basic HID emulation techniques
- Always test in controlled environments
- Use responsibly and ethically
- Consider the security implications of automated input

For more information, visit: https://github.com/ZeroDumb/happy-frog
"""'''
        else:
            return '''# Production code - executes immediately on device boot/plug-in
# Error handling for production
try:
    kbd.release_all()  # Ensure no keys are stuck
except Exception as e:
    pass  # Silent error handling for production

"""
End of Happy Frog Production Code
Generated from Happy Frog Script
"""'''
    
    def _get_delay_template(self) -> str:
        """Get the delay command template."""
        return "time.sleep({delay})  # Delay for {delay_ms}ms"
    
    def _get_string_template(self) -> str:
        """Get the string command template."""
        return 'keyboard_layout.write("{text}")  # Type: {original_text}'
    
    def _get_key_press_template(self) -> str:
        """Get the key press template."""
        return [
            "kbd.press({key_code})  # Press {key_name}",
            "kbd.release({key_code})  # Release {key_name}"
        ]
    
    def _get_comment_template(self) -> str:
        """Get the comment template."""
        return "# {comment_text}"
    
    def _get_repeat_template(self) -> str:
        """Get the repeat command template."""
        return "    # REPEAT: Repeat the last command"
    
    def _get_conditional_template(self) -> str:
        """Get the conditional command template."""
        return "    # CONDITIONAL: Execute command based on condition"
    
    def _get_loop_template(self) -> str:
        """Get the loop command template."""
        return "    # LOOP: Repeat command multiple times"
    
    def _get_log_template(self) -> str:
        """Get the log command template."""
        return "    # LOG: Record command execution"
    
    def validate_script(self, script: HappyFrogScript) -> List[str]:
        """
        Validate a script for encoding compatibility.
        
        Args:
            script: Parsed HappyFrogScript object
            
        Returns:
            List of warning messages (empty if no issues)
        """
        warnings = []
        
        for command in script.commands:
            # Check for unsupported commands
            if command.command_type not in self.key_codes and \
               command.command_type not in [CommandType.DELAY, CommandType.STRING, 
                                           CommandType.COMMENT, CommandType.REM,
                                           CommandType.MODIFIER_COMBO]:
                warnings.append(
                    f"Line {command.line_number}: Command '{command.command_type.value}' "
                    "may not be fully supported"
                )
            
            # Check for very long strings that might cause issues
            if command.command_type == CommandType.STRING and command.parameters:
                text = command.parameters[0]
                if len(text) > 1000:
                    warnings.append(
                        f"Line {command.line_number}: Very long string ({len(text)} chars) "
                        "may cause timing issues"
                    )
        
        return warnings
    
    def _encode_repeat(self, command: HappyFrogCommand) -> List[str]:
        """Encode a REPEAT command - repeat the last command n times."""
        if not command.parameters:
            raise EncoderError(f"REPEAT command missing count: {command.raw_text}")
        
        try:
            repeat_count = int(command.parameters[0])
            if repeat_count < 1:
                raise EncoderError("Repeat count must be at least 1")
            
            if not self.last_command:
                raise EncoderError("No previous command to repeat")
            
            lines = [
                f"    # REPEAT: Repeating last command {repeat_count} times",
                f"    for _ in range({repeat_count}):"
            ]
            
            # Add the last command with proper indentation
            last_lines = self._encode_command(self.last_command, 0)  # 0 for no line number
            for line in last_lines:
                if line.strip() and not line.strip().startswith('#'):
                    lines.append(f"        {line.strip()}")
            
            return lines
            
        except ValueError:
            raise EncoderError(f"Invalid repeat count '{command.parameters[0]}' in command: {command.raw_text}")
    
    def _encode_default_delay(self, command: HappyFrogCommand) -> List[str]:
        """Encode a DEFAULT_DELAY command - set default delay between commands."""
        if not command.parameters:
            raise EncoderError(f"DEFAULT_DELAY command missing value: {command.raw_text}")
        
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise EncoderError("Default delay value must be non-negative")
            
            self.default_delay = delay_ms
            indent = "    " if self.safe_mode else ""
            return [
                f"{indent}# DEFAULT_DELAY: Set default delay to {delay_ms}ms between commands",
                f"{indent}default_delay = {delay_ms / 1000.0}  # Convert to seconds"
            ]
            
        except ValueError:
            raise EncoderError(f"Invalid default delay value '{command.parameters[0]}' in command: {command.raw_text}")
    
    def _encode_if(self, command: HappyFrogCommand) -> List[str]:
        """Encode an IF command - conditional execution."""
        if not command.parameters:
            raise EncoderError(f"IF command missing condition: {command.raw_text}")
        
        condition = command.parameters[0]
        return [
            f"    # IF: Conditional execution based on '{condition}'",
            f"    # Note: This is a simplified condition check",
            f"    if True:  # Placeholder for condition: {condition}"
        ]
    
    def _encode_else(self, command: HappyFrogCommand) -> List[str]:
        """Encode an ELSE command."""
        return [
            "    # ELSE: Alternative execution path",
            "    else:"
        ]
    
    def _encode_endif(self, command: HappyFrogCommand) -> List[str]:
        """Encode an ENDIF command."""
        return [
            "    # ENDIF: End conditional block"
        ]
    
    def _encode_while(self, command: HappyFrogCommand) -> List[str]:
        """Encode a WHILE command - loop execution."""
        if not command.parameters:
            raise EncoderError(f"WHILE command missing condition: {command.raw_text}")
        
        condition = command.parameters[0]
        return [
            f"    # WHILE: Loop execution based on '{condition}'",
            f"    # Note: This is a simplified loop condition",
            f"    while True:  # Placeholder for condition: {condition}"
        ]
    
    def _encode_endwhile(self, command: HappyFrogCommand) -> List[str]:
        """Encode an ENDWHILE command."""
        return [
            "    # ENDWHILE: End loop block"
        ]
    
    def _encode_random_delay(self, command: HappyFrogCommand) -> List[str]:
        """Encode a RANDOM_DELAY command - random delay for human-like behavior."""
        if len(command.parameters) < 2:
            raise EncoderError(f"RANDOM_DELAY command missing min/max values: {command.raw_text}")
        
        try:
            min_delay = int(command.parameters[0])
            max_delay = int(command.parameters[1])
            if min_delay < 0 or max_delay < min_delay:
                raise EncoderError("Invalid random delay range")
            
            return [
                f"    # RANDOM_DELAY: Human-like random delay between {min_delay}ms and {max_delay}ms",
                f"    import random",
                f"    random_delay = random.uniform({min_delay / 1000.0}, {max_delay / 1000.0})",
                f"    time.sleep(random_delay)"
            ]
            
        except ValueError:
            raise EncoderError(f"Invalid random delay values in command: {command.raw_text}")
    
    def _encode_log(self, command: HappyFrogCommand) -> List[str]:
        """Encode a LOG command - logging for debugging."""
        if not command.parameters:
            raise EncoderError(f"LOG command missing message: {command.raw_text}")
        
        message = command.parameters[0]
        return [
            f"    # LOG: {message}",
            f"    print('Happy Frog Log: {message}')"
        ]
    
    def _encode_validate(self, command: HappyFrogCommand) -> List[str]:
        """Encode a VALIDATE command - validate environment before execution."""
        if not command.parameters:
            raise EncoderError(f"VALIDATE command missing condition: {command.raw_text}")
        
        condition = command.parameters[0]
        return [
            f"    # VALIDATE: Check environment condition '{condition}'",
            f"    # Note: This is a placeholder for environment validation",
            f"    print('Validating: {condition}')"
        ]
    
    def _encode_safe_mode(self, command: HappyFrogCommand) -> List[str]:
        """Encode a SAFE_MODE command - enable/disable safe mode restrictions."""
        if not command.parameters:
            raise EncoderError(f"SAFE_MODE command missing ON/OFF value: {command.raw_text}")
        
        mode = command.parameters[0].upper()
        if mode not in ['ON', 'OFF']:
            raise EncoderError("SAFE_MODE must be ON or OFF")
        
        self.safe_mode = (mode == 'ON')
        return [
            f"    # SAFE_MODE: {'Enabled' if self.safe_mode else 'Disabled'} safe mode restrictions",
            f"    safe_mode = {str(self.safe_mode).lower()}"
        ]
    
    def _encode_attackmode(self, command: HappyFrogCommand) -> List[str]:
        """Encode an ATTACKMODE command - BadUSB attack mode configuration."""
        if not command.parameters:
            raise EncoderError(f"ATTACKMODE command missing configuration: {command.raw_text}")
        
        mode_config = command.parameters[0].upper()
        
        # Handle different ATTACKMODE configurations
        if 'HID' in mode_config:
            return [
                f"    # ATTACKMODE: Configured for HID emulation ({mode_config})",
                f"    # Note: This device is configured as a HID keyboard/mouse",
                f"    # Configuration: {mode_config}"
            ]
        elif 'STORAGE' in mode_config:
            return [
                f"    # ATTACKMODE: Configured for storage emulation ({mode_config})",
                f"    # Note: This device is configured as a storage device",
                f"    # Configuration: {mode_config}"
            ]
        elif mode_config in ['ON', 'OFF']:
            # Legacy ON/OFF support
            self.safe_mode = (mode_config == 'ON')
            return [
                f"    # ATTACKMODE: {'Enabled' if self.safe_mode else 'Disabled'} attack mode",
                f"    safe_mode = {str(self.safe_mode).lower()}"
            ]
        else:
            # Generic ATTACKMODE configuration
            return [
                f"    # ATTACKMODE: Configured with '{mode_config}'",
                f"    # Note: This is a BadUSB attack mode configuration",
                f"    # Configuration: {mode_config}"
            ] 