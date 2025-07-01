"""
Happy Frog - Arduino Leonardo Device Template

This module provides Arduino code generation specifically for the Arduino Leonardo.
The Leonardo is a classic choice for HID emulation due to its native USB HID support
and widespread availability in the security research community.

Educational Purpose: Demonstrates Arduino-specific code generation and USB HID implementation.

Author: ZeroDumb
License: GNU GPLv3
"""

from typing import List, Dict, Any, Optional
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType


class ArduinoLeonardoEncoder:
    """
    Encoder that generates Arduino code specifically for Arduino Leonardo.
    
    The Leonardo uses the ATmega32u4 processor and has native USB HID support,
    making it ideal for keyboard and mouse emulation.
    """
    
    def __init__(self):
        """Initialize the Leonardo-specific encoder."""
        self.device_name = "Arduino Leonardo"
        self.processor = "ATmega32u4"
        self.framework = "Arduino"
        self.production_mode = False
        
        # Leonardo-specific optimizations
        self.optimizations = {
            'native_usb': True,  # Native USB HID support
            'keyboard_library': True,  # Built-in Keyboard library
            'mouse_library': True,  # Built-in Mouse library
            'serial_debug': True,  # Serial debugging available
        }
    
    def set_production_mode(self, production: bool = True):
        """Set production mode for immediate execution on boot."""
        self.production_mode = production
    
    def generate_header(self, script: HappyFrogScript) -> List[str]:
        """Generate Leonardo-specific header code."""
        lines = []
        
        if self.production_mode:
            lines.append('/*')
            lines.append('Happy Frog - Arduino Leonardo Production Code')
            lines.append('HID Emulation Script - Runs immediately on boot')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Processor: {self.processor}')
            lines.append(f'Framework: {self.framework}')
            lines.append('Mode: Production (immediate execution)')
            lines.append('')
            lines.append('⚠️ PRODUCTION MODE: This code runs immediately when device boots!')
            lines.append('⚠️ Use only for authorized testing and educational purposes!')
            lines.append('*/')
            lines.append('')
        else:
            lines.append('/*')
            lines.append('Happy Frog - Arduino Leonardo Generated Code')
            lines.append('Educational HID Emulation Script')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Processor: {self.processor}')
            lines.append(f'Framework: {self.framework}')
            lines.append('')
            lines.append('This code was automatically generated from a Happy Frog Script.')
            lines.append('Optimized for Arduino Leonardo with ATmega32u4 processor.')
            lines.append('')
            lines.append('⚠️ IMPORTANT: Use only for educational purposes and authorized testing!')
            lines.append('*/')
            lines.append('')
        
        # Leonardo-specific includes
        lines.append('#include <Keyboard.h>')
        lines.append('#include <Mouse.h>')
        lines.append('')
        
        # Leonardo-specific setup
        lines.append('void setup() {')
        lines.append('  // Initialize Leonardo for HID emulation')
        lines.append('  Keyboard.begin();')
        lines.append('  Mouse.begin();')
        lines.append('  ')
        lines.append('  // Leonardo-specific startup delay')
        lines.append('  delay(2000);  // Wait for system to recognize device')
        lines.append('}')
        lines.append('')
        
        if self.production_mode:
            lines.append('void loop() {')
            lines.append('  // Production mode - execute payload immediately')
            lines.append('  executePayload();')
            lines.append('  ')
            lines.append('  // Leonardo: Efficient infinite loop for production')
            lines.append('  while(true) {')
            lines.append('    delay(1000);  // Prevent re-execution')
            lines.append('  }')
            lines.append('}')
            lines.append('')
        else:
            lines.append('void loop() {')
            lines.append('  // Educational mode - main execution - runs once')
            lines.append('  executePayload();')
            lines.append('  ')
            lines.append('  // Leonardo: Stop execution after payload')
            lines.append('  while(true) {')
            lines.append('    delay(1000);  // Infinite loop to prevent re-execution')
            lines.append('  }')
            lines.append('}')
            lines.append('')
        
        lines.append('void executePayload() {')
        lines.append('  // Generated Happy Frog payload for Arduino Leonardo')
        lines.append('')
        
        return lines
    
    def generate_footer(self) -> List[str]:
        """Generate Leonardo-specific footer code."""
        lines = []
        
        lines.append('  // End of Happy Frog payload')
        lines.append('}')
        lines.append('')
        lines.append('/*')
        if self.production_mode:
            lines.append('End of Happy Frog Production Code for Arduino Leonardo')
            lines.append('')
            lines.append('Production Notes:')
            lines.append('- This code runs immediately on device boot')
            lines.append('- Optimized for native USB HID emulation')
            lines.append('- ATmega32u4 processor provides reliable USB communication')
            lines.append('- Classic choice for security research and automation')
        else:
            lines.append('End of Happy Frog Generated Code for Arduino Leonardo')
            lines.append('')
            lines.append('Educational Notes:')
            lines.append('- Arduino Leonardo provides native USB HID support')
            lines.append('- ATmega32u4 processor is optimized for USB communication')
            lines.append('- Built-in Keyboard and Mouse libraries make development easy')
            lines.append('- Classic choice for security research and education')
        lines.append('')
        lines.append('For more information, visit: https://github.com/ZeroDumb/happy-frog')
        lines.append('*/')
        
        return lines
    
    def encode_command(self, command: HappyFrogCommand) -> List[str]:
        """Encode a command specifically for Arduino Leonardo."""
        lines = []
        
        # Add Leonardo-specific comment
        comment = f"  // Leonardo Command: {command.raw_text}"
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
                    lines.append(f"  // ATTACKMODE: Configured for HID emulation ({mode_config})")
                    lines.append(f"  // Note: This device is configured as a HID keyboard/mouse")
                    lines.append(f"  // Configuration: {mode_config}")
                elif 'STORAGE' in mode_config:
                    lines.append(f"  // ATTACKMODE: Configured for storage emulation ({mode_config})")
                    lines.append(f"  // Note: This device is configured as a storage device")
                    lines.append(f"  // Configuration: {mode_config}")
                else:
                    lines.append(f"  // ATTACKMODE: Configured with '{mode_config}'")
                    lines.append(f"  // Note: This is a BadUSB attack mode configuration")
                    lines.append(f"  // Configuration: {mode_config}")
            else:
                lines.append(f"  // ATTACKMODE: BadUSB attack mode configuration")
            return lines
        
        # Encode based on command type with Leonardo optimizations
        if command.command_type == CommandType.DELAY:
            lines.extend(self._encode_delay_leonardo(command))
        elif command.command_type == CommandType.STRING:
            lines.extend(self._encode_string_leonardo(command))
        elif command.command_type == CommandType.MODIFIER_COMBO:
            lines.extend(self._encode_modifier_combo_leonardo(command))
        elif command.command_type == CommandType.RANDOM_DELAY:
            lines.extend(self._encode_random_delay_leonardo(command))
        elif command.command_type == CommandType.REPEAT:
            lines.extend(self._encode_repeat_leonardo(command))
        elif command.command_type in [CommandType.DEFAULT_DELAY, CommandType.DEFAULTDELAY]:
            lines.extend(self._encode_default_delay_leonardo(command))
        elif command.command_type == CommandType.IF:
            lines.extend(self._encode_if_leonardo(command))
        elif command.command_type == CommandType.ELSE:
            lines.extend(self._encode_else_leonardo(command))
        elif command.command_type == CommandType.ENDIF:
            lines.extend(self._encode_endif_leonardo(command))
        elif command.command_type == CommandType.WHILE:
            lines.extend(self._encode_while_leonardo(command))
        elif command.command_type == CommandType.ENDWHILE:
            lines.extend(self._encode_endwhile_leonardo(command))
        elif command.command_type == CommandType.LOG:
            lines.extend(self._encode_log_leonardo(command))
        elif command.command_type == CommandType.VALIDATE:
            lines.extend(self._encode_validate_leonardo(command))
        elif command.command_type == CommandType.SAFE_MODE:
            lines.extend(self._encode_safe_mode_leonardo(command))
        elif command.command_type == CommandType.PAUSE:
            lines.extend(self._encode_pause_leonardo(command))
        elif command.command_type in [CommandType.COMMENT, CommandType.REM]:
            lines.extend(self._encode_comment_leonardo(command))
        else:
            # Use standard encoding for other commands
            lines.extend(self._encode_standard_command_leonardo(command))
        
        return lines
    
    def _encode_delay_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode delay with Leonardo-specific optimizations."""
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise ValueError("Delay value must be non-negative")
            
            return [f"  delay({delay_ms});  // Leonardo delay: {delay_ms}ms"]
                
        except (ValueError, IndexError):
            return ["  // ERROR: Invalid delay value"]
    
    def _encode_string_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode string with Leonardo-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: STRING command missing text"]
        
        text = command.parameters[0]
        # Arduino Keyboard.print() handles escaping automatically
        return [
            f'  Keyboard.print("{text}");  // Leonardo string input'
        ]
    
    def _encode_modifier_combo_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode modifier combo with Leonardo-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: MODIFIER_COMBO command missing parameters"]
        
        lines = []
        lines.append("  // Leonardo optimized modifier combo")
        
        # Press all keys in the combo
        for param in command.parameters:
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_arduino_keycode(param.upper())
                lines.append(f"  Keyboard.press({key_code});  // Press {param}")
            else:
                key_code = self._get_arduino_keycode(param)
                lines.append(f"  Keyboard.press({key_code});  // Press {param}")
        
        # Release all keys in reverse order
        for param in reversed(command.parameters):
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_arduino_keycode(param.upper())
                lines.append(f"  Keyboard.release({key_code});  // Release {param}")
            else:
                key_code = self._get_arduino_keycode(param)
                lines.append(f"  Keyboard.release({key_code});  // Release {param}")
        
        return lines
    
    def _encode_random_delay_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode random delay with Leonardo-specific optimizations."""
        if len(command.parameters) < 2:
            return ["  // ERROR: RANDOM_DELAY command missing min/max values"]
        
        try:
            min_delay = int(command.parameters[0])
            max_delay = int(command.parameters[1])
            
            return [
                f"  // Leonardo optimized random delay: {min_delay}ms to {max_delay}ms",
                "  int random_delay = random(min_delay, max_delay);",
                "  delay(random_delay);"
            ]
            
        except ValueError:
            return ["  // ERROR: Invalid random delay values"]
    
    def _encode_repeat_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode REPEAT command for Arduino Leonardo."""
        if not command.parameters:
            return ["  // ERROR: REPEAT command missing count"]
        
        try:
            repeat_count = int(command.parameters[0])
            
            return [
                f"  // REPEAT: Repeat last command {repeat_count} times",
                f"  // Note: Leonardo optimized repeat functionality",
                f"  for (int i = 0; i < {repeat_count}; i++) {{",
                f"    // Placeholder for repeated command",
                f"  }}"
            ]
            
        except ValueError:
            return ["  // ERROR: Invalid repeat count"]
    
    def _encode_default_delay_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode DEFAULT_DELAY command for Arduino Leonardo."""
        if not command.parameters:
            return ["  // ERROR: DEFAULT_DELAY command missing value"]
        
        try:
            delay_ms = int(command.parameters[0])
            
            return [
                f"  // DEFAULT_DELAY: Set default delay to {delay_ms}ms between commands",
                f"  int default_delay = {delay_ms};  // Default delay in milliseconds"
            ]
            
        except ValueError:
            return ["  // ERROR: Invalid default delay value"]
    
    def _encode_if_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode IF command for Arduino Leonardo."""
        if not command.parameters:
            return ["  // ERROR: IF command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // IF: Conditional execution based on '{condition}'",
            f"  // Note: This is a simplified condition check for Leonardo",
            f"  if (true) {{  // Placeholder for condition: {condition}"
        ]
    
    def _encode_else_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode ELSE command for Arduino Leonardo."""
        return [
            "  // ELSE: Alternative execution path",
            "  } else {"
        ]
    
    def _encode_endif_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDIF command for Arduino Leonardo."""
        return [
            "  // ENDIF: End conditional block",
            "  }"
        ]
    
    def _encode_while_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode WHILE command for Arduino Leonardo."""
        if not command.parameters:
            return ["  // ERROR: WHILE command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // WHILE: Loop execution based on '{condition}'",
            f"  // Note: This is a simplified loop condition for Leonardo",
            f"  while (true) {{  // Placeholder for condition: {condition}"
        ]
    
    def _encode_endwhile_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDWHILE command for Arduino Leonardo."""
        return [
            "  // ENDWHILE: End loop block",
            "  }"
        ]
    
    def _encode_log_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode LOG command for Arduino Leonardo."""
        if not command.parameters:
            return ["  // ERROR: LOG command missing message"]
        
        message = command.parameters[0]
        
        return [
            f"  // LOG: {message}",
            f"  Serial.println(\"Leonardo Log: {message}\");"
        ]
    
    def _encode_validate_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode VALIDATE command for Arduino Leonardo."""
        if not command.parameters:
            return ["  // ERROR: VALIDATE command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // VALIDATE: Check environment condition '{condition}'",
            f"  // Note: This is a placeholder for environment validation on Leonardo",
            f"  Serial.println(\"Leonardo Validating: {condition}\");"
        ]
    
    def _encode_safe_mode_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode SAFE_MODE command for Arduino Leonardo."""
        if not command.parameters:
            return ["  // ERROR: SAFE_MODE command missing ON/OFF value"]
        
        mode = command.parameters[0].upper()
        
        if mode not in ['ON', 'OFF']:
            return ["  // ERROR: SAFE_MODE must be ON or OFF"]
        
        return [
            f"  // SAFE_MODE: {'Enabled' if mode == 'ON' else 'Disabled'} safe mode restrictions",
            f"  bool safe_mode = {str(mode == 'ON').lower()};"
        ]
    
    def _encode_pause_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode PAUSE command for Arduino Leonardo."""
        return [
            "  // PAUSE: Waiting for user input (press any key to continue)",
            "  // Note: In Arduino on Leonardo, we'll use a long delay as a simple pause",
            "  // For more sophisticated pause functionality, consider using button input",
            "  delay(5000);  // Pause for 5 seconds (Ducky Script PAUSE equivalent)"
        ]
    
    def _encode_comment_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode comment command for Arduino Leonardo."""
        comment_text = command.parameters[0] if command.parameters else ""
        
        return [
            f"  // {comment_text}"
        ]
    
    def _encode_standard_command_leonardo(self, command: HappyFrogCommand) -> List[str]:
        """Encode standard commands for Leonardo."""
        key_code = self._get_arduino_keycode(command.command_type.value)
        return [
            f"  Keyboard.press({key_code});  // Leonardo key press: {command.command_type.value}",
            f"  Keyboard.release({key_code});  // Leonardo key release: {command.command_type.value}"
        ]
    
    def _get_arduino_keycode(self, key: str) -> str:
        """Get Arduino keycode for a key."""
        key = key.upper()
        
        # Modifier keys
        if key == 'MOD':
            return "KEY_LEFT_GUI"
        elif key == 'CTRL':
            return "KEY_LEFT_CTRL"
        elif key == 'SHIFT':
            return "KEY_LEFT_SHIFT"
        elif key == 'ALT':
            return "KEY_LEFT_ALT"
        
        # Single letter keys
        if len(key) == 1 and key.isalpha():
            return f"'{key}'"
        
        # Number keys
        if key.isdigit():
            return f"'{key}'"
        
        # Special mappings
        key_mappings = {
            'ENTER': 'KEY_RETURN',
            'SPACE': "' '",
            'TAB': 'KEY_TAB',
            'BACKSPACE': 'KEY_BACKSPACE',
            'DELETE': 'KEY_DELETE',
            'ESCAPE': 'KEY_ESC',
            'HOME': 'KEY_HOME',
            'END': 'KEY_END',
            'INSERT': 'KEY_INSERT',
            'PAGE_UP': 'KEY_PAGE_UP',
            'PAGE_DOWN': 'KEY_PAGE_DOWN',
            'UP': 'KEY_UP_ARROW',
            'DOWN': 'KEY_DOWN_ARROW',
            'LEFT': 'KEY_LEFT_ARROW',
            'RIGHT': 'KEY_RIGHT_ARROW',
        }
        
        return key_mappings.get(key, f"'{key}'")
    
    def get_device_info(self) -> Dict[str, Any]:
        """Get device information for the Leonardo."""
        return {
            'name': self.device_name,
            'processor': self.processor,
            'framework': self.framework,
            'price_range': '$15-25',
            'difficulty': 'Intermediate',
            'features': [
                'ATmega32u4 processor',
                'Native USB HID support',
                'Built-in Keyboard library',
                'Built-in Mouse library',
                'Serial debugging',
                'Widespread availability',
                'Classic security research choice'
            ],
            'setup_notes': [
                'Install Arduino IDE',
                'Select Arduino Leonardo board',
                'Install Keyboard and Mouse libraries',
                'Upload code to device',
                'Test in controlled environment'
            ],
            'notes': 'Generates Arduino code for Arduino Leonardo. Upload output to device using Arduino IDE.'
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
                lines.append("  // Production code - executes immediately on device boot/plug-in")
                lines.append("  // ATTACKMODE HID STORAGE detected - running payload automatically")
                lines.append("")
                lines.append("  // Wait for system to recognize the device")
                lines.append("  delay(2000);")
                lines.append("")
            else:
                lines.append("  // Production code - main execution function")
                lines.append("  // Wait for system to recognize the device")
                lines.append("  delay(2000);")
                lines.append("")
        else:
            # Educational mode - always use main() function
            lines.append("  // Main execution loop")
            lines.append("  // Wait for system to recognize the device")
            lines.append("  delay(2000);")
            lines.append("")
        
        # Process each command
        for i, command in enumerate(script.commands):
            lines.extend(self.encode_command(command))
            lines.append("")  # Add blank line for readability
        
        return lines 