from typing import List, Dict, Any
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType

class XiaoRP2040Encoder:
    """
    Encoder that generates CircuitPython code for the Seeed Xiao RP2040.
    The output is meant to be copied to the device as code.py.
    """
    def __init__(self):
        self.device_name = "Seeed Xiao RP2040"
        self.processor = "RP2040"
        self.framework = "CircuitPython"
        self.production_mode = False
        self.optimizations = {
            'circuitpython': True,
            'adafruit_hid': True,
            'educational': True,
        }

    def set_production_mode(self, enabled: bool):
        """Set production mode for immediate execution on boot."""
        self.production_mode = enabled

    def generate_header(self, script: HappyFrogScript) -> List[str]:
        lines = []
        
        if self.production_mode:
            lines.append('"""')
            lines.append(f"Happy Frog - {self.device_name} Production Code")
            lines.append("HID Emulation Script - Runs immediately on boot")
            lines.append("")
            lines.append(f"Device: {self.device_name}")
            lines.append(f"Processor: {self.processor}")
            lines.append(f"Framework: {self.framework}")
            lines.append("Mode: Production (immediate execution)")
            lines.append("")
            lines.append("⚠️ PRODUCTION MODE: This code runs immediately when device boots!")
            lines.append("⚠️ Use only for authorized testing and educational purposes!")
            lines.append('"""')
            lines.append("")
            lines.append("import time")
            lines.append("import board")
            lines.append("import usb_hid")
            lines.append("from adafruit_hid.keyboard import Keyboard")
            lines.append("from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS")
            lines.append("from adafruit_hid.keycode import Keycode")
            lines.append("")
            lines.append("keyboard = Keyboard(usb_hid.devices)")
            lines.append("keyboard_layout = KeyboardLayoutUS(keyboard)")
            lines.append("")
        else:
            lines.append('"""')
            lines.append(f"Happy Frog - {self.device_name} Generated Code")
            lines.append("Educational HID Emulation Script")
            lines.append("")
            lines.append(f"Device: {self.device_name}")
            lines.append(f"Processor: {self.processor}")
            lines.append(f"Framework: {self.framework}")
            lines.append("")
            lines.append("This code was automatically generated from a Happy Frog Script.")
            lines.append("Optimized for Seeed Xiao RP2040 with CircuitPython.")
            lines.append("")
            lines.append("⚠️ IMPORTANT: Use only for educational purposes and authorized testing!")
            lines.append('"""')
            lines.append("")
            lines.append("import time")
            lines.append("import board")
            lines.append("import usb_hid")
            lines.append("from adafruit_hid.keyboard import Keyboard")
            lines.append("from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS")
            lines.append("from adafruit_hid.keycode import Keycode")
            lines.append("")
            lines.append("keyboard = Keyboard(usb_hid.devices)")
            lines.append("keyboard_layout = KeyboardLayoutUS(keyboard)")
            lines.append("")
            lines.append("def main():")
            lines.append("    # Wait for system to recognize the device")
            lines.append("    time.sleep(2)")
        
        return lines

    def generate_footer(self) -> List[str]:
        lines = []
        
        if not self.production_mode:
            lines.append("")
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
        lines = []
        
        # Determine indentation based on production mode
        indent = "" if self.production_mode else "    "
        
        # Add Xiao RP2040-specific comment
        comment = f"{indent}# Xiao RP2040 Command: {command.raw_text}"
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
        
        if command.command_type == CommandType.DELAY:
            try:
                delay_ms = int(command.parameters[0])
                lines.append(f"{indent}time.sleep({delay_ms/1000:.3f})  # Delay {delay_ms}ms")
            except (ValueError, IndexError):
                lines.append(f"{indent}# ERROR: Invalid delay value")
        elif command.command_type == CommandType.STRING:
            if command.parameters:
                text = command.parameters[0].replace('"', '\\"')
                lines.append(f'{indent}keyboard_layout.write("{text}")')
            else:
                lines.append(f"{indent}# ERROR: STRING command missing text")
        elif command.command_type == CommandType.MODIFIER_COMBO:
            # Example: MOD r or CTRL ALT DEL
            for param in command.parameters:
                keycode = self._get_keycode(param)
                lines.append(f"{indent}keyboard.press({keycode})")
            for param in reversed(command.parameters):
                keycode = self._get_keycode(param)
                lines.append(f"{indent}keyboard.release({keycode})")
        else:
            # Standard key press/release
            keycode = self._get_keycode(command.command_type.value)
            lines.append(f"{indent}keyboard.press({keycode})")
            lines.append(f"{indent}keyboard.release({keycode})")
        return lines

    def _get_keycode(self, key: str) -> str:
        # Map Happy Frog/standard keys to Keycode constants
        key = key.upper()
        mapping = {
            'MOD': 'Keycode.WINDOWS',
            'WINDOWS': 'Keycode.WINDOWS',
            'CTRL': 'Keycode.CONTROL',
            'CONTROL': 'Keycode.CONTROL',
            'SHIFT': 'Keycode.SHIFT',
            'ALT': 'Keycode.ALT',
            'ENTER': 'Keycode.ENTER',
            'TAB': 'Keycode.TAB',
            'ESC': 'Keycode.ESCAPE',
            'ESCAPE': 'Keycode.ESCAPE',
            'UP': 'Keycode.UP_ARROW',
            'DOWN': 'Keycode.DOWN_ARROW',
            'LEFT': 'Keycode.LEFT_ARROW',
            'RIGHT': 'Keycode.RIGHT_ARROW',
            'SPACE': 'Keycode.SPACEBAR',
            'DELETE': 'Keycode.DELETE',
            'BACKSPACE': 'Keycode.BACKSPACE',
            'CAPSLOCK': 'Keycode.CAPS_LOCK',
            'F1': 'Keycode.F1',
            'F2': 'Keycode.F2',
            'F3': 'Keycode.F3',
            'F4': 'Keycode.F4',
            'F5': 'Keycode.F5',
            'F6': 'Keycode.F6',
            'F7': 'Keycode.F7',
            'F8': 'Keycode.F8',
            'F9': 'Keycode.F9',
            'F10': 'Keycode.F10',
            'F11': 'Keycode.F11',
            'F12': 'Keycode.F12',
        }
        if key in mapping:
            return mapping[key]
        elif len(key) == 1 and key.isalpha():
            return f'Keycode.{key}'
        elif len(key) == 1 and key.isdigit():
            return f'Keycode.{key}'
        else:
            return f'Keycode.{key}'

    def get_device_info(self) -> Dict[str, any]:
        return {
            'device_name': self.device_name,
            'processor': self.processor,
            'framework': self.framework,
            'optimizations': self.optimizations,
            'notes': 'Generates CircuitPython code for Seeed Xiao RP2040. Copy output to device as code.py.'
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