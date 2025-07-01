"""
Happy Frog - ESP32 Device Template

This module provides Arduino code generation specifically for the ESP32.
The ESP32 is popular for WiFi-enabled HID emulation and IoT scenarios due to
its built-in WiFi, Bluetooth, and extensive connectivity options.

Educational Purpose: Demonstrates wireless HID emulation and IoT security concepts.

Author: ZeroDumb
License: GNU GPLv3
"""

from typing import List, Dict, Any, Optional
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType


class ESP32Encoder:
    """
    Encoder that generates Arduino code specifically for ESP32.
    
    The ESP32 uses dual-core processors and provides WiFi/Bluetooth capabilities,
    making it ideal for wireless HID emulation and IoT security research.
    """
    
    def __init__(self):
        """Initialize the ESP32-specific encoder."""
        self.device_name = "ESP32"
        self.processor = "Dual-core Xtensa LX6"
        self.framework = "Arduino (ESP32)"
        self.production_mode = False
        
        # ESP32-specific optimizations
        self.optimizations = {
            'wifi_enabled': True,  # Built-in WiFi
            'bluetooth_enabled': True,  # Built-in Bluetooth
            'dual_core': True,  # Dual-core processor
            'iot_capable': True,  # IoT connectivity
            'wireless_attacks': True,  # Wireless attack scenarios
        }
    
    def set_production_mode(self, production: bool = True):
        """Set production mode for immediate execution on boot."""
        self.production_mode = production
    
    def generate_header(self, script: HappyFrogScript) -> List[str]:
        """Generate ESP32-specific header code."""
        lines = []
        
        if self.production_mode:
            lines.append('/*')
            lines.append('Happy Frog - ESP32 Production Code')
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
            lines.append('Happy Frog - ESP32 Generated Code')
            lines.append('Educational HID Emulation Script')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Processor: {self.processor}')
            lines.append(f'Framework: {self.framework}')
            lines.append('')
            lines.append('This code was automatically generated from a Happy Frog Script.')
            lines.append('Optimized for ESP32 with WiFi/Bluetooth capabilities.')
            lines.append('')
            lines.append('⚠️ IMPORTANT: Use only for educational purposes and authorized testing!')
            lines.append('*/')
            lines.append('')
        
        # ESP32-specific includes
        lines.append('#include <BleKeyboard.h>  // ESP32 Bluetooth HID')
        lines.append('#include <WiFi.h>  // ESP32 WiFi')
        lines.append('#include <WebServer.h>  // ESP32 Web Server')
        lines.append('')
        
        # ESP32-specific setup
        lines.append('// ESP32-specific configuration')
        lines.append('BleKeyboard bleKeyboard("Happy Frog ESP32", "Happy Frog Team", 100);')
        lines.append('WebServer server(80);  // Web server for remote control')
        lines.append('')
        
        lines.append('void setup() {')
        lines.append('  // Initialize ESP32 for wireless HID emulation')
        lines.append('  Serial.begin(115200);  // ESP32 serial communication')
        lines.append('  ')
        lines.append('  // Initialize Bluetooth HID')
        lines.append('  bleKeyboard.begin();')
        lines.append('  ')
        lines.append('  // ESP32: Wait for Bluetooth connection')
        lines.append('  Serial.println("Waiting for Bluetooth connection...");')
        lines.append('  while(!bleKeyboard.isConnected()) {')
        lines.append('    delay(500);')
        lines.append('  }')
        lines.append('  Serial.println("Bluetooth connected!");')
        lines.append('  ')
        lines.append('  // ESP32: Additional startup delay')
        lines.append('  delay(2000);  // Wait for system to recognize device')
        lines.append('}')
        lines.append('')
        
        if self.production_mode:
            lines.append('void loop() {')
            lines.append('  // Production mode - execute payload immediately')
            lines.append('  executePayload();')
            lines.append('  ')
            lines.append('  // ESP32: Maintain Bluetooth connection for production')
            lines.append('  while(true) {')
            lines.append('    bleKeyboard.isConnected();  // Keep connection alive')
            lines.append('    delay(1000);')
            lines.append('  }')
            lines.append('}')
            lines.append('')
        else:
            lines.append('void loop() {')
            lines.append('  // Educational mode - main execution - runs once')
            lines.append('  executePayload();')
            lines.append('  ')
            lines.append('  // ESP32: Maintain Bluetooth connection')
            lines.append('  while(true) {')
            lines.append('    bleKeyboard.isConnected();  // Keep connection alive')
            lines.append('    delay(1000);')
            lines.append('  }')
            lines.append('}')
            lines.append('')
        
        lines.append('void executePayload() {')
        lines.append('  // Generated Happy Frog payload for ESP32')
        lines.append('')
        
        return lines
    
    def generate_footer(self) -> List[str]:
        """Generate ESP32-specific footer code."""
        lines = []
        
        lines.append('  // End of Happy Frog payload')
        lines.append('}')
        lines.append('')
        lines.append('/*')
        if self.production_mode:
            lines.append('End of Happy Frog Production Code for ESP32')
            lines.append('')
            lines.append('Production Notes:')
            lines.append('- This code runs immediately on device boot')
            lines.append('- Optimized for wireless HID emulation')
            lines.append('- Dual-core processor enables complex automation')
            lines.append('- WiFi and Bluetooth support IoT security research')
        else:
            lines.append('End of Happy Frog Generated Code for ESP32')
            lines.append('')
            lines.append('Educational Notes:')
            lines.append('- ESP32 provides wireless HID emulation capabilities')
            lines.append('- Dual-core processor enables complex automation scenarios')
            lines.append('- WiFi and Bluetooth support IoT security research')
            lines.append('- Ideal for wireless attack demonstrations and education')
        lines.append('')
        lines.append('For more information, visit: https://github.com/ZeroDumb/happy-frog')
        lines.append('*/')
        
        return lines
    
    def encode_command(self, command: HappyFrogCommand) -> List[str]:
        """Encode a command specifically for ESP32."""
        lines = []
        
        # Add ESP32-specific comment
        comment = f"  // ESP32 Command: {command.raw_text}"
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
        
        # Encode based on command type with ESP32 optimizations
        if command.command_type == CommandType.DELAY:
            lines.extend(self._encode_delay_esp32(command))
        elif command.command_type == CommandType.STRING:
            lines.extend(self._encode_string_esp32(command))
        elif command.command_type == CommandType.MODIFIER_COMBO:
            lines.extend(self._encode_modifier_combo_esp32(command))
        elif command.command_type == CommandType.RANDOM_DELAY:
            lines.extend(self._encode_random_delay_esp32(command))
        elif command.command_type == CommandType.REPEAT:
            lines.extend(self._encode_repeat_esp32(command))
        elif command.command_type in [CommandType.DEFAULT_DELAY, CommandType.DEFAULTDELAY]:
            lines.extend(self._encode_default_delay_esp32(command))
        elif command.command_type == CommandType.IF:
            lines.extend(self._encode_if_esp32(command))
        elif command.command_type == CommandType.ELSE:
            lines.extend(self._encode_else_esp32(command))
        elif command.command_type == CommandType.ENDIF:
            lines.extend(self._encode_endif_esp32(command))
        elif command.command_type == CommandType.WHILE:
            lines.extend(self._encode_while_esp32(command))
        elif command.command_type == CommandType.ENDWHILE:
            lines.extend(self._encode_endwhile_esp32(command))
        elif command.command_type == CommandType.LOG:
            lines.extend(self._encode_log_esp32(command))
        elif command.command_type == CommandType.VALIDATE:
            lines.extend(self._encode_validate_esp32(command))
        elif command.command_type == CommandType.SAFE_MODE:
            lines.extend(self._encode_safe_mode_esp32(command))
        elif command.command_type == CommandType.PAUSE:
            lines.extend(self._encode_pause_esp32(command))
        elif command.command_type in [CommandType.COMMENT, CommandType.REM]:
            lines.extend(self._encode_comment_esp32(command))
        else:
            # Use standard encoding for other commands
            lines.extend(self._encode_standard_command_esp32(command))
        
        return lines
    
    def _encode_delay_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode delay with ESP32-specific optimizations."""
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise ValueError("Delay value must be non-negative")
            
            # ESP32: High-precision delays with WiFi considerations
            return [f"  delay({delay_ms});  // ESP32 delay: {delay_ms}ms"]
                
        except (ValueError, IndexError):
            return ["  // ERROR: Invalid delay value"]
    
    def _encode_string_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode string with ESP32-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: STRING command missing text"]
        
        text = command.parameters[0]
        # ESP32: Bluetooth HID string input
        return [
            f'  bleKeyboard.print("{text}");  // ESP32 Bluetooth string input'
        ]
    
    def _encode_modifier_combo_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode modifier combo with ESP32-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: MODIFIER_COMBO command missing parameters"]
        
        lines = []
        lines.append("  // ESP32 Bluetooth modifier combo")
        
        # Press all keys in the combo
        for param in command.parameters:
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_esp32_keycode(param.upper())
                lines.append(f"  bleKeyboard.press({key_code});  // Press {param}")
            else:
                key_code = self._get_esp32_keycode(param)
                lines.append(f"  bleKeyboard.press({key_code});  // Press {param}")
        
        # Release all keys in reverse order
        for param in reversed(command.parameters):
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_esp32_keycode(param.upper())
                lines.append(f"  bleKeyboard.release({key_code});  // Release {param}")
            else:
                key_code = self._get_esp32_keycode(param)
                lines.append(f"  bleKeyboard.release({key_code});  // Release {param}")
        
        return lines
    
    def _encode_random_delay_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode random delay with ESP32-specific optimizations."""
        if len(command.parameters) < 2:
            return ["  // ERROR: RANDOM_DELAY command missing min/max values"]
        
        try:
            min_delay = int(command.parameters[0])
            max_delay = int(command.parameters[1])
            
            return [
                f"  // ESP32 wireless random delay: {min_delay}ms to {max_delay}ms",
                "  int random_delay = random(min_delay, max_delay);",
                "  delay(random_delay);"
            ]
            
        except ValueError:
            return ["  // ERROR: Invalid random delay values"]
    
    def _encode_repeat_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode REPEAT command for ESP32."""
        if not command.parameters:
            return ["  // ERROR: REPEAT command missing count"]
        
        try:
            repeat_count = int(command.parameters[0])
            
            return [
                f"  // REPEAT: Repeat last command {repeat_count} times",
                f"  // Note: ESP32 optimized repeat functionality",
                f"  for (int i = 0; i < {repeat_count}; i++) {{",
                f"    // Placeholder for repeated command",
                f"  }}"
            ]
            
        except ValueError:
            return ["  // ERROR: Invalid repeat count"]
    
    def _encode_default_delay_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode DEFAULT_DELAY command for ESP32."""
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
    
    def _encode_if_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode IF command for ESP32."""
        if not command.parameters:
            return ["  // ERROR: IF command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // IF: Conditional execution based on '{condition}'",
            f"  // Note: This is a simplified condition check for ESP32",
            f"  if (true) {{  // Placeholder for condition: {condition}"
        ]
    
    def _encode_else_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode ELSE command for ESP32."""
        return [
            "  // ELSE: Alternative execution path",
            "  } else {"
        ]
    
    def _encode_endif_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDIF command for ESP32."""
        return [
            "  // ENDIF: End conditional block",
            "  }"
        ]
    
    def _encode_while_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode WHILE command for ESP32."""
        if not command.parameters:
            return ["  // ERROR: WHILE command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // WHILE: Loop execution based on '{condition}'",
            f"  // Note: This is a simplified loop condition for ESP32",
            f"  while (true) {{  // Placeholder for condition: {condition}"
        ]
    
    def _encode_endwhile_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode ENDWHILE command for ESP32."""
        return [
            "  // ENDWHILE: End loop block",
            "  }"
        ]
    
    def _encode_log_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode LOG command for ESP32."""
        if not command.parameters:
            return ["  // ERROR: LOG command missing message"]
        
        message = command.parameters[0]
        
        return [
            f"  // LOG: {message}",
            f"  Serial.println(\"ESP32 Log: {message}\");"
        ]
    
    def _encode_validate_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode VALIDATE command for ESP32."""
        if not command.parameters:
            return ["  // ERROR: VALIDATE command missing condition"]
        
        condition = command.parameters[0]
        
        return [
            f"  // VALIDATE: Check environment condition '{condition}'",
            f"  // Note: This is a placeholder for environment validation on ESP32",
            f"  Serial.println(\"ESP32 Validating: {condition}\");"
        ]
    
    def _encode_safe_mode_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode SAFE_MODE command for ESP32."""
        if not command.parameters:
            return ["  // ERROR: SAFE_MODE command missing ON/OFF value"]
        
        mode = command.parameters[0].upper()
        
        if mode not in ['ON', 'OFF']:
            return ["  // ERROR: SAFE_MODE must be ON or OFF"]
        
        return [
            f"  // SAFE_MODE: {'Enabled' if mode == 'ON' else 'Disabled'} safe mode restrictions",
            f"  bool safe_mode = {str(mode == 'ON').lower()};"
        ]
    
    def _encode_pause_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode PAUSE command for ESP32."""
        return [
            "  // PAUSE: Waiting for user input (press any key to continue)",
            "  // Note: In ESP32, we'll use a long delay as a simple pause",
            "  // For more sophisticated pause functionality, consider using WiFi/Bluetooth input",
            "  delay(5000);  // Pause for 5 seconds (Ducky Script PAUSE equivalent)"
        ]
    
    def _encode_comment_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode comment command for ESP32."""
        comment_text = command.parameters[0] if command.parameters else ""
        
        return [
            f"  // {comment_text}"
        ]
    
    def _encode_standard_command_esp32(self, command: HappyFrogCommand) -> List[str]:
        """Encode standard commands for ESP32."""
        key_code = self._get_esp32_keycode(command.command_type.value)
        return [
            f"  bleKeyboard.press({key_code});  // ESP32 key press: {command.command_type.value}",
            f"  bleKeyboard.release({key_code});  // ESP32 key release: {command.command_type.value}"
        ]
    
    def _get_esp32_keycode(self, key: str) -> str:
        """Get ESP32 keycode for a key."""
        key = key.upper()
        
        # Modifier keys
        if key == 'MOD':
            return "KEY_GUI"
        elif key == 'CTRL':
            return "KEY_CTRL"
        elif key == 'SHIFT':
            return "KEY_SHIFT"
        elif key == 'ALT':
            return "KEY_ALT"
        
        # Single letter keys
        if len(key) == 1 and key.isalpha():
            return f"KEY_{key}"
        
        # Number keys
        if key.isdigit():
            return f"KEY_{key}"
        
        # Special mappings
        key_mappings = {
            'ENTER': 'KEY_ENTER',
            'SPACE': 'KEY_SPACE',
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
        
        return key_mappings.get(key, f"KEY_{key}")
    
    def get_device_info(self) -> Dict[str, Any]:
        """Get device information for the ESP32."""
        return {
            'name': self.device_name,
            'processor': self.processor,
            'framework': self.framework,
            'price_range': '$5-15',
            'difficulty': 'Intermediate',
            'features': [
                'Dual-core Xtensa LX6 processor',
                'Built-in WiFi and Bluetooth',
                'Wireless HID emulation',
                'IoT connectivity',
                'Web server capabilities',
                'Remote control possibilities',
                'Advanced security research tool'
            ],
            'setup_notes': [
                'Install Arduino IDE with ESP32 board support',
                'Select ESP32 board',
                'Install BleKeyboard library',
                'Upload code to device',
                'Connect via Bluetooth',
                'Test in controlled environment'
            ],
            'notes': 'Generates Arduino code for ESP32. Upload output to device using Arduino IDE with ESP32 board support. Requires Bluetooth connection to target device.'
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