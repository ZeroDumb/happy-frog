"""
Happy Frog - Raspberry Pi Pico Device Template

This module provides CircuitPython code generation specifically for the Raspberry Pi Pico.
The Pico is one of the most popular devices for HID emulation due to its low cost,
excellent CircuitPython support, and powerful RP2040 processor.

Educational Purpose: Demonstrates device-specific code generation and optimization.

Author: ZeroDumb
License: GNU GPLv3
"""

from typing import List, Dict, Any, Optional
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType


class RaspberryPiPicoEncoder:
    """
    Encoder that generates CircuitPython code specifically for Raspberry Pi Pico.
    
    The Pico uses the RP2040 processor and has excellent CircuitPython support
    for HID emulation. This encoder optimizes code for the Pico's capabilities.
    """
    
    def __init__(self):
        """Initialize the Pico-specific encoder."""
        self.device_name = "Raspberry Pi Pico"
        self.processor = "RP2040"
        self.framework = "CircuitPython"
        self.production_mode = False
        
        # Pico-specific optimizations
        self.optimizations = {
            'fast_startup': True,  # Pico boots quickly
            'usb_hid_native': True,  # Native USB HID support
            'dual_core': True,  # Can use both cores if needed
            'flash_storage': True,  # Can store scripts in flash
        }
    
    def set_production_mode(self, production: bool = True):
        """Set production mode for immediate execution on boot."""
        self.production_mode = production
    
    def generate_header(self, script: HappyFrogScript) -> List[str]:
        """Generate Pico-specific header code."""
        lines = []
        
        if self.production_mode:
            lines.append('"""')
            lines.append(f'Happy Frog - {self.device_name} Production Code')
            lines.append('HID Emulation Script - Runs immediately on boot')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Processor: {self.processor}')
            lines.append(f'Framework: {self.framework}')
            lines.append('Mode: Production (immediate execution)')
            lines.append('')
            lines.append('⚠️ PRODUCTION MODE: This code runs immediately when device boots!')
            lines.append('⚠️ Use only for authorized testing and educational purposes!')
            lines.append('"""')
            lines.append('')
            lines.append('import time')
            lines.append('import board')
            lines.append('import usb_hid')
            lines.append('from adafruit_hid.keyboard import Keyboard')
            lines.append('from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS')
            lines.append('from adafruit_hid.keycode import Keycode')
            lines.append('')
            lines.append('keyboard = Keyboard(usb_hid.devices)')
            lines.append('keyboard_layout = KeyboardLayoutUS(keyboard)')
            lines.append('')
        else:
            lines.append('"""')
            lines.append(f'Happy Frog - {self.device_name} Generated Code')
            lines.append('Educational HID Emulation Script')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Processor: {self.processor}')
            lines.append(f'Framework: {self.framework}')
            lines.append('')
            lines.append('This code was automatically generated from a Happy Frog Script.')
            lines.append('Optimized for Raspberry Pi Pico with RP2040 processor.')
            lines.append('')
            lines.append('⚠️ IMPORTANT: Use only for educational purposes and authorized testing!')
            lines.append('"""')
            lines.append('')
            lines.append('import time')
            lines.append('import board')
            lines.append('import usb_hid')
            lines.append('from adafruit_hid.keyboard import Keyboard')
            lines.append('from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS')
            lines.append('from adafruit_hid.keycode import Keycode')
            lines.append('')
            lines.append('keyboard = Keyboard(usb_hid.devices)')
            lines.append('keyboard_layout = KeyboardLayoutUS(keyboard)')
            lines.append('')
            lines.append('def main():')
            lines.append('    # Wait for system to recognize the device')
            lines.append('    time.sleep(2)')
        
        return lines
    
    def generate_footer(self) -> List[str]:
        """Generate Pico-specific footer code."""
        lines = []
        
        if not self.production_mode:
            lines.append('')
            lines.append("if __name__ == '__main__':")
            lines.append("    try:")
            lines.append("        main()")
            lines.append("    except Exception as e:")
            lines.append("        print(f'Error during execution: {e}')")
            lines.append("        keyboard.release_all()")
            lines.append("    finally:")
            lines.append("        print('Happy Frog execution completed.')")
        
        return lines
    
    def encode_command(self, command: HappyFrogCommand) -> List[str]:
        """Encode a command specifically for Raspberry Pi Pico."""
        lines = []
        
        # Determine indentation based on production mode
        indent = "" if self.production_mode else "    "
        
        # Add Pico-specific comment
        comment = f"{indent}# Pico Command: {command.raw_text}"
        lines.append(comment)
        
        # Handle comment lines (lines starting with #)
        if command.raw_text.strip().startswith('#'):
            # Skip comment lines - they're already handled by the comment above
            return lines
        
        # Handle ATTACKMODE command (BadUSB attack mode configuration)
        if command.command_type == CommandType.ATTACKMODE:
            if command.parameters:
                mode_config = ' '.join(command.parameters).upper()
                if 'HID' in mode_config:
                    lines.append(f"{indent}# ATTACKMODE: Configured for HID emulation ({mode_config})")
                    lines.append(f"{indent}# Note: This device is configured as a HID keyboard/mouse")
                    lines.append(f"{indent}# Configuration: {mode_config}")
                elif 'STORAGE' in mode_config:
                    lines.append(f"{indent}# ATTACKMODE: Configured for storage emulation ({mode_config})")
                    lines.append(f"{indent}# Note: This device is configured as a storage device")
                    lines.append(f"{indent}# Configuration: {mode_config}")
                else:
                    lines.append(f"{indent}# ATTACKMODE: Configured with '{mode_config}'")
                    lines.append(f"{indent}# Note: This is a BadUSB attack mode configuration")
                    lines.append(f"{indent}# Configuration: {mode_config}")
            else:
                lines.append(f"{indent}# ATTACKMODE: BadUSB attack mode configuration")
            return lines
        
        # Encode based on command type with Pico optimizations
        if command.command_type == CommandType.DELAY:
            lines.extend(self._encode_delay_pico(command))
        elif command.command_type == CommandType.STRING:
            lines.extend(self._encode_string_pico(command))
        elif command.command_type == CommandType.MODIFIER_COMBO:
            lines.extend(self._encode_modifier_combo_pico(command))
        elif command.command_type == CommandType.RANDOM_DELAY:
            lines.extend(self._encode_random_delay_pico(command))
        elif command.command_type == CommandType.REPEAT:
            lines.extend(self._encode_repeat_pico(command))
        elif command.command_type in [CommandType.DEFAULT_DELAY, CommandType.DEFAULTDELAY]:
            lines.extend(self._encode_default_delay_pico(command))
        elif command.command_type == CommandType.IF:
            lines.extend(self._encode_if_pico(command))
        elif command.command_type == CommandType.ELSE:
            lines.extend(self._encode_else_pico(command))
        elif command.command_type == CommandType.ENDIF:
            lines.extend(self._encode_endif_pico(command))
        elif command.command_type == CommandType.WHILE:
            lines.extend(self._encode_while_pico(command))
        elif command.command_type == CommandType.ENDWHILE:
            lines.extend(self._encode_endwhile_pico(command))
        elif command.command_type == CommandType.LOG:
            lines.extend(self._encode_log_pico(command))
        elif command.command_type == CommandType.VALIDATE:
            lines.extend(self._encode_validate_pico(command))
        elif command.command_type == CommandType.SAFE_MODE:
            lines.extend(self._encode_safe_mode_pico(command))
        elif command.command_type == CommandType.PAUSE:
            lines.extend(self._encode_pause_pico(command))
        elif command.command_type in [CommandType.COMMENT, CommandType.REM]:
            lines.extend(self._encode_comment_pico(command))
        else:
            # Standard key press/release
            lines.extend(self._encode_standard_command(command))
        
        return lines
    
    def _encode_delay_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode delay with Pico-specific optimizations."""
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise ValueError("Delay value must be non-negative")
            
            indent = "" if self.production_mode else "    "
            
            # Pico-specific delay optimization
            if delay_ms < 10:
                # Very short delays - use microsecond precision
                return [f"{indent}time.sleep({delay_ms / 1000.0})  # Pico optimized delay: {delay_ms}ms"]
            else:
                # Standard delays
                return [f"{indent}time.sleep({delay_ms / 1000.0})  # Delay: {delay_ms}ms"]
                
        except (ValueError, IndexError):
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: Invalid delay value"]
    
    def _encode_string_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode string with Pico-specific optimizations."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: STRING command missing text"]
        
        text = command.parameters[0]
        escaped_text = text.replace('\\', '\\\\').replace('"', '\\"')
        indent = "" if self.production_mode else "    "
        
        return [
            f'{indent}keyboard_layout.write("{escaped_text}")  # Pico string input: {text}'
        ]
    
    def _encode_modifier_combo_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode modifier combo with Pico-specific optimizations."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: MODIFIER_COMBO command missing parameters"]
        
        lines = []
        indent = "" if self.production_mode else "    "
        lines.append(f"{indent}# Pico optimized modifier combo")
        
        # Press all keys in the combo
        for param in command.parameters:
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_keycode(param.upper())
                lines.append(f"{indent}keyboard.press({key_code})  # Press {param}")
            else:
                key_code = self._get_keycode(param)
                lines.append(f"{indent}keyboard.press({key_code})  # Press {param}")
        
        # Release all keys in reverse order
        for param in reversed(command.parameters):
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_keycode(param.upper())
                lines.append(f"{indent}keyboard.release({key_code})  # Release {param}")
            else:
                key_code = self._get_keycode(param)
                lines.append(f"{indent}keyboard.release({key_code})  # Release {param}")
        
        return lines
    
    def _encode_random_delay_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode random delay with Pico-specific optimizations."""
        if len(command.parameters) < 2:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: RANDOM_DELAY command missing min/max values"]
        
        try:
            min_delay = int(command.parameters[0])
            max_delay = int(command.parameters[1])
            indent = "" if self.production_mode else "    "
            
            return [
                f"{indent}# Pico optimized random delay: {min_delay}ms to {max_delay}ms",
                f"{indent}import random",
                f"{indent}random_delay = random.uniform({min_delay / 1000.0}, {max_delay / 1000.0})",
                f"{indent}time.sleep(random_delay)"
            ]
            
        except ValueError:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: Invalid random delay values"]
    
    def _encode_standard_command(self, command: HappyFrogCommand) -> List[str]:
        """Encode standard commands for Pico."""
        key_code = self._get_keycode(command.command_type.value)
        indent = "" if self.production_mode else "    "
        
        return [
            f"{indent}keyboard.press({key_code})  # Pico key press: {command.command_type.value}",
            f"{indent}keyboard.release({key_code})  # Pico key release: {command.command_type.value}"
        ]
    
    def _encode_repeat_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode REPEAT command for Pico."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: REPEAT command missing count"]
        
        try:
            repeat_count = int(command.parameters[0])
            indent = "" if self.production_mode else "    "
            
            return [
                f"{indent}# REPEAT: Repeat last command {repeat_count} times",
                f"{indent}# Note: Pico optimized repeat functionality",
                f"{indent}for _ in range({repeat_count}):",
                f"{indent}    pass  # Placeholder for repeated command"
            ]
            
        except ValueError:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: Invalid repeat count"]
    
    def _encode_default_delay_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode DEFAULT_DELAY command for Pico."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: DEFAULT_DELAY command missing value"]
        
        try:
            delay_ms = int(command.parameters[0])
            indent = "" if self.production_mode else "    "
            
            return [
                f"{indent}# DEFAULT_DELAY: Set default delay to {delay_ms}ms between commands",
                f"{indent}default_delay = {delay_ms / 1000.0}  # Convert to seconds"
            ]
            
        except ValueError:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: Invalid default delay value"]
    
    def _encode_if_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode IF command for Pico."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: IF command missing condition"]
        
        condition = command.parameters[0]
        indent = "" if self.production_mode else "    "
        
        return [
            f"{indent}# IF: Conditional execution based on '{condition}'",
            f"{indent}# Note: This is a simplified condition check for Pico",
            f"{indent}if True:  # Placeholder for condition: {condition}"
        ]
    
    def _encode_else_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode ELSE command for Pico."""
        indent = "" if self.production_mode else "    "
        return [
            f"{indent}# ELSE: Alternative execution path",
            f"{indent}else:"
        ]
    
    def _encode_endif_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDIF command for Pico."""
        indent = "" if self.production_mode else "    "
        return [
            f"{indent}# ENDIF: End conditional block"
        ]
    
    def _encode_while_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode WHILE command for Pico."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: WHILE command missing condition"]
        
        condition = command.parameters[0]
        indent = "" if self.production_mode else "    "
        
        return [
            f"{indent}# WHILE: Loop execution based on '{condition}'",
            f"{indent}# Note: This is a simplified loop condition for Pico",
            f"{indent}while True:  # Placeholder for condition: {condition}"
        ]
    
    def _encode_endwhile_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDWHILE command for Pico."""
        indent = "" if self.production_mode else "    "
        return [
            f"{indent}# ENDWHILE: End loop block"
        ]
    
    def _encode_log_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode LOG command for Pico."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: LOG command missing message"]
        
        message = command.parameters[0]
        indent = "" if self.production_mode else "    "
        
        return [
            f"{indent}# LOG: {message}",
            f"{indent}print('Pico Log: {message}')"
        ]
    
    def _encode_validate_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode VALIDATE command for Pico."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: VALIDATE command missing condition"]
        
        condition = command.parameters[0]
        indent = "" if self.production_mode else "    "
        
        return [
            f"{indent}# VALIDATE: Check environment condition '{condition}'",
            f"{indent}# Note: This is a placeholder for environment validation on Pico",
            f"{indent}print('Pico Validating: {condition}')"
        ]
    
    def _encode_safe_mode_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode SAFE_MODE command for Pico."""
        if not command.parameters:
            indent = "" if self.production_mode else "    "
            return [f"{indent}# ERROR: SAFE_MODE command missing ON/OFF value"]
        
        mode = command.parameters[0].upper()
        indent = "" if self.production_mode else "    "
        
        if mode not in ['ON', 'OFF']:
            return [f"{indent}# ERROR: SAFE_MODE must be ON or OFF"]
        
        return [
            f"{indent}# SAFE_MODE: {'Enabled' if mode == 'ON' else 'Disabled'} safe mode restrictions",
            f"{indent}safe_mode = {str(mode == 'ON').lower()}"
        ]
    
    def _encode_pause_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode PAUSE command for Pico."""
        indent = "" if self.production_mode else "    "
        
        return [
            f"{indent}# PAUSE: Waiting for user input (press any key to continue)",
            f"{indent}# Note: In CircuitPython on Pico, we'll use a long delay as a simple pause",
            f"{indent}# For more sophisticated pause functionality, consider using button input",
            f"{indent}time.sleep(5)  # Pause for 5 seconds (Ducky Script PAUSE equivalent)"
        ]
    
    def _encode_comment_pico(self, command: HappyFrogCommand) -> List[str]:
        """Encode comment command for Pico."""
        comment_text = command.parameters[0] if command.parameters else ""
        indent = "" if self.production_mode else "    "
        
        return [
            f"{indent}# {comment_text}"
        ]
    
    def _get_keycode(self, key: str) -> str:
        """Get CircuitPython keycode for a key."""
        key = key.upper()
        
        # Modifier keys
        if key == 'MOD':
            return "Keycode.GUI"
        elif key == 'CTRL':
            return "Keycode.CONTROL"
        elif key == 'SHIFT':
            return "Keycode.SHIFT"
        elif key == 'ALT':
            return "Keycode.ALT"
        
        # Single letter keys
        if len(key) == 1 and key.isalpha():
            return f"Keycode.{key}"
        
        # Number keys
        if key.isdigit():
            return f"Keycode.{key}"
        
        # Special mappings
        key_mappings = {
            'ENTER': 'Keycode.ENTER',
            'SPACE': 'Keycode.SPACE',
            'TAB': 'Keycode.TAB',
            'BACKSPACE': 'Keycode.BACKSPACE',
            'DELETE': 'Keycode.DELETE',
            'ESCAPE': 'Keycode.ESCAPE',
            'HOME': 'Keycode.HOME',
            'END': 'Keycode.END',
            'INSERT': 'Keycode.INSERT',
            'PAGE_UP': 'Keycode.PAGE_UP',
            'PAGE_DOWN': 'Keycode.PAGE_DOWN',
            'UP': 'Keycode.UP_ARROW',
            'DOWN': 'Keycode.DOWN_ARROW',
            'LEFT': 'Keycode.LEFT_ARROW',
            'RIGHT': 'Keycode.RIGHT_ARROW',
        }
        
        return key_mappings.get(key, f"Keycode.{key}")
    
    def get_device_info(self) -> Dict[str, Any]:
        """Get device information for the Pico."""
        return {
            'name': self.device_name,
            'processor': self.processor,
            'framework': self.framework,
            'price_range': '$4-8',
            'difficulty': 'Beginner',
            'features': [
                'Dual-core ARM Cortex-M0+',
                '264KB SRAM',
                '2MB Flash',
                'Native USB HID support',
                'CircuitPython compatible',
                'Low cost',
                'Fast boot time'
            ],
            'setup_notes': [
                'Install CircuitPython firmware',
                'Install adafruit_hid library',
                'Copy code to device',
                'Test in controlled environment'
            ],
            'notes': 'Generates CircuitPython code for Raspberry Pi Pico. Copy output to device as code.py.'
        }
    
    def _generate_main_code(self, script: HappyFrogScript) -> List[str]:
        """Generate the main execution code with ATTACKMODE detection."""
        lines = []
        
        # Check if ATTACKMODE HID STORAGE is present for immediate execution
        has_attackmode = any(
            cmd.command_type == CommandType.ATTACKMODE and 
            cmd.parameters and 
            'HID' in ' '.join(cmd.parameters).upper()
            for cmd in script.commands
        )
        
        if self.production_mode:
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
        else:
            # Educational mode - always use main() function
            lines.append("# Main execution loop")
            lines.append("def main():")
            lines.append("    # Wait for system to recognize the device")
            lines.append("    time.sleep(2)")
            lines.append("")
        
        # Process each command
        for i, command in enumerate(script.commands):
            lines.extend(self.encode_command(command))
            lines.append("")  # Add blank line for readability
        
        return lines 