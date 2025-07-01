"""
Happy Frog - Teensy 4.0 Device Template

This module provides Arduino code generation specifically for the Teensy 4.0.
The Teensy 4.0 is a high-performance device popular in advanced security research
due to its ARM Cortex-M7 processor and extensive USB HID capabilities.

Educational Purpose: Demonstrates high-performance device optimization and advanced features.

Author: ZeroDumb
License: GNU GPLv3
"""

from typing import List, Dict, Any, Optional
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType


class Teensy4Encoder:
    """
    Encoder that generates Arduino code specifically for Teensy 4.0.
    
    The Teensy 4.0 uses the ARM Cortex-M7 processor and provides excellent
    performance for complex HID emulation scenarios.
    """
    
    def __init__(self):
        """Initialize the Teensy 4.0-specific encoder."""
        self.device_name = "Teensy 4.0"
        self.processor = "ARM Cortex-M7"
        self.framework = "Arduino (Teensyduino)"
        self.production_mode = False
        
        # Teensy 4.0-specific optimizations
        self.optimizations = {
            'high_performance': True,  # 600MHz processor
            'extended_usb': True,  # Extended USB HID support
            'flash_storage': True,  # Large flash storage
            'sram_optimized': True,  # 1MB SRAM
            'crypto_hardware': True,  # Hardware crypto acceleration
        }
    
    def set_production_mode(self, production: bool = True):
        """Set production mode for immediate execution on boot."""
        self.production_mode = production
    
    def generate_header(self, script: HappyFrogScript) -> List[str]:
        """Generate Teensy 4.0-specific header code."""
        lines = []
        
        if self.production_mode:
            lines.append('/*')
            lines.append('Happy Frog - Teensy 4.0 Production Code')
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
            lines.append('Happy Frog - Teensy 4.0 Generated Code')
            lines.append('Educational HID Emulation Script')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Processor: {self.processor}')
            lines.append(f'Framework: {self.framework}')
            lines.append('')
            lines.append('This code was automatically generated from a Happy Frog Script.')
            lines.append('Optimized for Teensy 4.0 with ARM Cortex-M7 processor.')
            lines.append('')
            lines.append('⚠️ IMPORTANT: Use only for educational purposes and authorized testing!')
            lines.append('*/')
            lines.append('')
        
        # Teensy 4.0-specific includes
        lines.append('#include <Keyboard.h>')
        lines.append('#include <Mouse.h>')
        lines.append('#include <USBHost_t36.h>  // Teensy 4.0 USB Host support')
        lines.append('')
        
        # Teensy 4.0-specific setup
        lines.append('void setup() {')
        lines.append('  // Initialize Teensy 4.0 for high-performance HID emulation')
        lines.append('  Keyboard.begin();')
        lines.append('  Mouse.begin();')
        lines.append('  ')
        lines.append('  // Teensy 4.0: Fast startup with minimal delay')
        lines.append('  delay(500);  // Optimized startup delay')
        lines.append('}')
        lines.append('')
        
        if self.production_mode:
            lines.append('void loop() {')
            lines.append('  // Production mode - execute payload immediately')
            lines.append('  executePayload();')
            lines.append('  ')
            lines.append('  // Teensy 4.0: Efficient infinite loop for production')
            lines.append('  while(true) {')
            lines.append('    yield();  // Allow background tasks')
            lines.append('  }')
            lines.append('}')
            lines.append('')
        else:
            lines.append('void loop() {')
            lines.append('  // Educational mode - main execution - runs once')
            lines.append('  executePayload();')
            lines.append('  ')
            lines.append('  // Teensy 4.0: Efficient infinite loop')
            lines.append('  while(true) {')
            lines.append('    yield();  // Allow background tasks')
            lines.append('  }')
            lines.append('}')
            lines.append('')
        
        lines.append('void executePayload() {')
        lines.append('  // Generated Happy Frog payload for Teensy 4.0')
        lines.append('')
        
        return lines
    
    def generate_footer(self) -> List[str]:
        """Generate Teensy 4.0-specific footer code."""
        lines = []
        
        lines.append('  // End of Happy Frog payload')
        lines.append('}')
        lines.append('')
        lines.append('/*')
        if self.production_mode:
            lines.append('End of Happy Frog Production Code for Teensy 4.0')
            lines.append('')
            lines.append('Production Notes:')
            lines.append('- This code runs immediately on device boot')
            lines.append('- Optimized for high-performance HID emulation')
            lines.append('- ARM Cortex-M7 processor enables complex automation')
            lines.append('- Extended USB capabilities support advanced features')
        else:
            lines.append('End of Happy Frog Generated Code for Teensy 4.0')
            lines.append('')
            lines.append('Educational Notes:')
            lines.append('- Teensy 4.0 provides exceptional performance for HID emulation')
            lines.append('- ARM Cortex-M7 processor enables complex automation scenarios')
            lines.append('- Extended USB capabilities support advanced HID features')
            lines.append('- Hardware crypto acceleration available for advanced applications')
        lines.append('')
        lines.append('For more information, visit: https://github.com/ZeroDumb/happy-frog')
        lines.append('*/')
        
        return lines
    
    def encode_command(self, command: HappyFrogCommand) -> List[str]:
        """Encode a command specifically for Teensy 4.0."""
        lines = []
        
        # Add Teensy 4.0-specific comment
        comment = f"  // Teensy 4.0 Command: {command.raw_text}"
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
        
        # Encode based on command type with Teensy 4.0 optimizations
        if command.command_type == CommandType.DELAY:
            lines.extend(self._encode_delay_teensy(command))
        elif command.command_type == CommandType.STRING:
            lines.extend(self._encode_string_teensy(command))
        elif command.command_type == CommandType.MODIFIER_COMBO:
            lines.extend(self._encode_modifier_combo_teensy(command))
        elif command.command_type == CommandType.RANDOM_DELAY:
            lines.extend(self._encode_random_delay_teensy(command))
        elif command.command_type == CommandType.REPEAT:
            lines.extend(self._encode_repeat_teensy(command))
        elif command.command_type in [CommandType.DEFAULT_DELAY, CommandType.DEFAULTDELAY]:
            lines.extend(self._encode_default_delay_teensy(command))
        elif command.command_type == CommandType.IF:
            lines.extend(self._encode_if_teensy(command))
        elif command.command_type == CommandType.ELSE:
            lines.extend(self._encode_else_teensy(command))
        elif command.command_type == CommandType.ENDIF:
            lines.extend(self._encode_endif_teensy(command))
        elif command.command_type == CommandType.WHILE:
            lines.extend(self._encode_while_teensy(command))
        elif command.command_type == CommandType.ENDWHILE:
            lines.extend(self._encode_endwhile_teensy(command))
        elif command.command_type == CommandType.LOG:
            lines.extend(self._encode_log_teensy(command))
        elif command.command_type == CommandType.VALIDATE:
            lines.extend(self._encode_validate_teensy(command))
        elif command.command_type == CommandType.SAFE_MODE:
            lines.extend(self._encode_safe_mode_teensy(command))
        elif command.command_type == CommandType.PAUSE:
            lines.extend(self._encode_pause_teensy(command))
        elif command.command_type in [CommandType.COMMENT, CommandType.REM]:
            lines.extend(self._encode_comment_teensy(command))
        else:
            # Use standard encoding for other commands
            lines.extend(self._encode_standard_command_teensy(command))
        
        return lines
    
    def _encode_delay_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode delay with Teensy 4.0-specific optimizations."""
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise ValueError("Delay value must be non-negative")
            
            # Teensy 4.0: High-precision delays
            if delay_ms < 1:
                return [f"  delayMicroseconds({delay_ms * 1000});  // Teensy 4.0 microsecond delay"]
            else:
                return [f"  delay({delay_ms});  // Teensy 4.0 optimized delay: {delay_ms}ms"]
                
        except (ValueError, IndexError):
            return ["  // ERROR: Invalid delay value"]
    
    def _encode_string_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode string with Teensy 4.0-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: STRING command missing text"]
        
        text = command.parameters[0]
        # Teensy 4.0: High-performance string input
        return [
            f'  Keyboard.print("{text}");  // Teensy 4.0 high-performance string input'
        ]
    
    def _encode_modifier_combo_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode modifier combo with Teensy 4.0-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: MODIFIER_COMBO command missing parameters"]
        
        lines = []
        lines.append("  // Teensy 4.0 high-performance modifier combo")
        
        # Press all keys in the combo
        for param in command.parameters:
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_teensy_keycode(param.upper())
                lines.append(f"  Keyboard.press({key_code});  // Press {param}")
            else:
                key_code = self._get_teensy_keycode(param)
                lines.append(f"  Keyboard.press({key_code});  // Press {param}")
        
        # Release all keys in reverse order
        for param in reversed(command.parameters):
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_teensy_keycode(param.upper())
                lines.append(f"  Keyboard.release({key_code});  // Release {param}")
            else:
                key_code = self._get_teensy_keycode(param)
                lines.append(f"  Keyboard.release({key_code});  // Release {param}")
        
        return lines
    
    def _encode_random_delay_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode random delay with Teensy 4.0-specific optimizations."""
        if len(command.parameters) < 2:
            return ["  // ERROR: RANDOM_DELAY command missing min/max values"]
        
        try:
            min_delay = int(command.parameters[0])
            max_delay = int(command.parameters[1])
            
            return [
                f"  // Teensy 4.0 high-precision random delay: {min_delay}ms to {max_delay}ms",
                "  int random_delay = random(min_delay, max_delay);",
                "  delay(random_delay);"
            ]
            
        except ValueError:
            return ["  // ERROR: Invalid random delay values"]
    
    def _encode_repeat_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode REPEAT command for Teensy 4.0."""
        if not command.parameters:
            return ["  // ERROR: REPEAT command missing count"]
        
        try:
            repeat_count = int(command.parameters[0])
            
            return [
                f"  // REPEAT: Repeat last command {repeat_count} times",
                f"  // Note: Teensy 4.0 optimized repeat functionality",
                f"  for (int i = 0; i < {repeat_count}; i++) {{",
                f"    // Placeholder for repeated command",
                f"  }}"
            ]
            
        except ValueError:
            return ["  // ERROR: Invalid repeat count"]
    
    def _encode_default_delay_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode DEFAULT_DELAY command for Teensy 4.0."""
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
    
    def _encode_if_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode IF command for Teensy 4.0."""
        if not command.parameters:
            return ["  // ERROR: IF command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // IF: Conditional execution based on '{condition}'",
            f"  // Note: This is a simplified condition check for Teensy 4.0",
            f"  if (true) {{  // Placeholder for condition: {condition}"
        ]
    
    def _encode_else_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode ELSE command for Teensy 4.0."""
        return [
            "  // ELSE: Alternative execution path",
            "  } else {"
        ]
    
    def _encode_endif_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDIF command for Teensy 4.0."""
        return [
            "  // ENDIF: End conditional block",
            "  }"
        ]
    
    def _encode_while_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode WHILE command for Teensy 4.0."""
        if not command.parameters:
            return ["  // ERROR: WHILE command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // WHILE: Loop execution based on '{condition}'",
            f"  // Note: This is a simplified loop condition for Teensy 4.0",
            f"  while (true) {{  // Placeholder for condition: {condition}"
        ]
    
    def _encode_endwhile_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDWHILE command for Teensy 4.0."""
        return [
            "  // ENDWHILE: End loop block",
            "  }"
        ]
    
    def _encode_log_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode LOG command for Teensy 4.0."""
        if not command.parameters:
            return ["  // ERROR: LOG command missing message"]
        
        message = command.parameters[0]
        
        return [
            f"  // LOG: {message}",
            f"  Serial.println(\"Teensy 4.0 Log: {message}\");"
        ]
    
    def _encode_validate_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode VALIDATE command for Teensy 4.0."""
        if not command.parameters:
            return ["  // ERROR: VALIDATE command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // VALIDATE: Check environment condition '{condition}'",
            f"  // Note: This is a placeholder for environment validation on Teensy 4.0",
            f"  Serial.println(\"Teensy 4.0 Validating: {condition}\");"
        ]
    
    def _encode_safe_mode_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode SAFE_MODE command for Teensy 4.0."""
        if not command.parameters:
            return ["  // ERROR: SAFE_MODE command missing ON/OFF value"]
        
        mode = command.parameters[0].upper()
        
        if mode not in ['ON', 'OFF']:
            return ["  // ERROR: SAFE_MODE must be ON or OFF"]
        
        return [
            f"  // SAFE_MODE: {'Enabled' if mode == 'ON' else 'Disabled'} safe mode restrictions",
            f"  bool safe_mode = {str(mode == 'ON').lower()};"
        ]
    
    def _encode_pause_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode PAUSE command for Teensy 4.0."""
        return [
            "  // PAUSE: Waiting for user input (press any key to continue)",
            "  // Note: In Arduino on Teensy 4.0, we'll use a long delay as a simple pause",
            "  // For more sophisticated pause functionality, consider using button input",
            "  delay(5000);  // Pause for 5 seconds (Ducky Script PAUSE equivalent)"
        ]
    
    def _encode_comment_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode comment command for Teensy 4.0."""
        comment_text = command.parameters[0] if command.parameters else ""
        
        return [
            f"  // {comment_text}"
        ]
    
    def _encode_standard_command_teensy(self, command: HappyFrogCommand) -> List[str]:
        """Encode standard commands for Teensy 4.0."""
        key_code = self._get_teensy_keycode(command.command_type.value)
        return [
            f"  Keyboard.press({key_code});  // Teensy 4.0 key press: {command.command_type.value}",
            f"  Keyboard.release({key_code});  // Teensy 4.0 key release: {command.command_type.value}"
        ]
    
    def _get_teensy_keycode(self, key: str) -> str:
        """Get Teensy keycode for a key."""
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
        """Get device information for the Teensy 4.0."""
        return {
            'name': self.device_name,
            'processor': self.processor,
            'framework': self.framework,
            'price_range': '$25-35',
            'difficulty': 'Advanced',
            'features': [
                'ARM Cortex-M7 processor (600MHz)',
                '1MB SRAM, 2MB Flash',
                'Extended USB HID support',
                'Hardware crypto acceleration',
                'High-performance capabilities',
                'Advanced security research tool',
                'Teensyduino framework'
            ],
            'setup_notes': [
                'Install Arduino IDE with Teensyduino',
                'Select Teensy 4.0 board',
                'Install required libraries',
                'Upload code to device',
                'Test in controlled environment'
            ],
            'notes': 'Generates Arduino code for Teensy 4.0. Upload output to device using Arduino IDE with Teensyduino.'
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