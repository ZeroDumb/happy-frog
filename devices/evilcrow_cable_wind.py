from typing import List, Dict, Any
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType

class EvilCrowCableEncoder:
    """
    Encoder that generates Arduino code specifically for EvilCrow-Cable.
    Optimized for WiFi-enabled BadUSB attacks and stealth operations.
    """
    def __init__(self):
        self.device_name = "EvilCrow-Cable"
        self.processor = "ATtiny85"
        self.framework = "Arduino (EvilCrow-Cable)"
        self.production_mode = False
        self.optimizations = {
            'built_in_usb_c': True,
            'stealth_design': True,
            'badusb_optimized': True,
            'compact_form': True,
            'limited_memory': True,
            'specialized_hardware': True,
            'wifi_enabled': True,  # Unique to EvilCrow-Cable
        }

    def set_production_mode(self, production: bool = True):
        """Set production mode for immediate execution on boot."""
        self.production_mode = production

    def generate_header(self, script: HappyFrogScript) -> List[str]:
        lines = []
        if self.production_mode:
            lines.append('/*')
            lines.append('Happy Frog - EvilCrow-Cable Production Code')
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
            lines.append('Happy Frog - EvilCrow-Cable Generated Code')
            lines.append('Educational HID Emulation Script')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Processor: {self.processor}')
            lines.append(f'Framework: {self.framework}')
            lines.append('')
            lines.append('This code was automatically generated from a Happy Frog Script.')
            lines.append('Optimized for EvilCrow-Cable with ATtiny85 processor.')
            lines.append('')
            lines.append('⚠️ IMPORTANT: Use only for educational purposes and authorized testing!')
            lines.append('⚠️ This device is designed for cybersecurity education and research.')
            lines.append('*/')
            lines.append('')
        # Includes
        lines.append('#include "DigiKeyboard.h"  // EvilCrow-Cable keyboard library')
        lines.append('#include <SoftwareSerial.h> // For WiFi module')
        lines.append('#define WIFI_RX 2')
        lines.append('#define WIFI_TX 3')
        lines.append('SoftwareSerial wifiSerial(WIFI_RX, WIFI_TX); // RX, TX')
        lines.append('')
        lines.append('void setup() {')
        lines.append('  // Initialize EvilCrow-Cable for stealth HID emulation')
        lines.append('  DigiKeyboard.update();')
        lines.append('  wifiSerial.begin(115200); // Start WiFi serial')
        lines.append('  DigiKeyboard.delay(1000);  // Stealth startup delay')
        lines.append('}')
        lines.append('')
        if self.production_mode:
            lines.append('void loop() {')
            lines.append('  // Production mode - execute payload immediately')
            lines.append('  executePayload();')
            lines.append('  while(true) { ; }')
            lines.append('}')
            lines.append('')
        else:
            lines.append('void loop() {')
            lines.append('  // Educational mode - main execution - runs once')
            lines.append('  executePayload();')
            lines.append('  while(true) { ; }')
            lines.append('}')
            lines.append('')
        lines.append('void executePayload() {')
        lines.append('  // Generated Happy Frog payload for EvilCrow-Cable')
        lines.append('')
        return lines

    def generate_footer(self) -> List[str]:
        lines = []
        lines.append('  // End of Happy Frog payload')
        lines.append('}')
        lines.append('')
        lines.append('/*')
        if self.production_mode:
            lines.append('End of Happy Frog Production Code for EvilCrow-Cable')
            lines.append('')
            lines.append('Production Notes:')
            lines.append('- This code runs immediately on device boot')
            lines.append('- Optimized for WiFi-enabled BadUSB attacks')
            lines.append('- Stealth design and compact form factor')
            lines.append('- Use only for authorized testing and education')
        else:
            lines.append('End of Happy Frog Generated Code for EvilCrow-Cable')
            lines.append('')
            lines.append('Educational Notes:')
            lines.append('- EvilCrow-Cable provides ultra-stealth HID emulation')
            lines.append('- ATtiny85 processor enables portable attack scenarios')
            lines.append('- Built-in USB-C connectors for maximum compatibility')
            lines.append('- Designed for cybersecurity education and research')
            lines.append('- Use responsibly and ethically!')
        lines.append('')
        lines.append('For more information, visit: https://github.com/ZeroDumb/happy-frog')
        lines.append('*/')
        return lines

    def encode_command(self, command: HappyFrogCommand) -> List[str]:
        lines = []
        comment = f"  // EvilCrow-Cable Command: {command.raw_text}"
        lines.append(comment)
        if command.raw_text.strip().startswith('#'):
            return lines
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
                elif 'WIFI' in mode_config:
                    lines.append(f"  // ATTACKMODE: Configured for WiFi-enabled attack ({mode_config})")
                    lines.append(f"  // Note: This device will use WiFi for payload delivery")
                    lines.append(f"  // Configuration: {mode_config}")
                else:
                    lines.append(f"  // ATTACKMODE: Configured with '{mode_config}'")
                    lines.append(f"  // Note: This is a BadUSB attack mode configuration")
                    lines.append(f"  // Configuration: {mode_config}")
            else:
                lines.append(f"  // ATTACKMODE: BadUSB attack mode configuration")
            return lines
        if command.command_type == CommandType.DELAY:
            lines.extend(self._encode_delay_evilcrow(command))
        elif command.command_type == CommandType.STRING:
            lines.extend(self._encode_string_evilcrow(command))
        elif command.command_type == CommandType.MODIFIER_COMBO:
            lines.extend(self._encode_modifier_combo_evilcrow(command))
        elif command.command_type == CommandType.RANDOM_DELAY:
            lines.extend(self._encode_random_delay_evilcrow(command))
        elif command.command_type == CommandType.REPEAT:
            lines.extend(self._encode_repeat_evilcrow(command))
        elif command.command_type in [CommandType.DEFAULT_DELAY, CommandType.DEFAULTDELAY]:
            lines.extend(self._encode_default_delay_evilcrow(command))
        elif command.command_type == CommandType.IF:
            lines.extend(self._encode_if_evilcrow(command))
        elif command.command_type == CommandType.ELSE:
            lines.extend(self._encode_else_evilcrow(command))
        elif command.command_type == CommandType.ENDIF:
            lines.extend(self._encode_endif_evilcrow(command))
        elif command.command_type == CommandType.WHILE:
            lines.extend(self._encode_while_evilcrow(command))
        elif command.command_type == CommandType.ENDWHILE:
            lines.extend(self._encode_endwhile_evilcrow(command))
        elif command.command_type == CommandType.LOG:
            lines.extend(self._encode_log_evilcrow(command))
        elif command.command_type == CommandType.VALIDATE:
            lines.extend(self._encode_validate_evilcrow(command))
        elif command.command_type == CommandType.SAFE_MODE:
            lines.extend(self._encode_safe_mode_evilcrow(command))
        elif command.command_type == CommandType.PAUSE:
            lines.extend(self._encode_pause_evilcrow(command))
        elif command.command_type == CommandType.RELEASE:
            lines.extend(self._encode_release_evilcrow(command))
        elif command.command_type == CommandType.WIFI_SEND:
            lines.extend(self._encode_wifi_send_evilcrow(command))
        elif command.command_type == CommandType.WIFI_CONNECT:
            lines.extend(self._encode_wifi_connect_evilcrow(command))
        elif command.command_type == CommandType.SHELLWIN:
            lines.extend(self._encode_shellwin_evilcrow(command))
        elif command.command_type == CommandType.SHELLNIX:
            lines.extend(self._encode_shellnix_evilcrow(command))
        elif command.command_type == CommandType.SHELLMAC:
            lines.extend(self._encode_shellmac_evilcrow(command))
        elif command.command_type in [CommandType.COMMENT, CommandType.REM]:
            lines.extend(self._encode_comment_evilcrow(command))
        else:
            lines.extend(self._encode_standard_command_evilcrow(command))
        return lines

    def _encode_delay_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise ValueError("Delay value must be non-negative")
            return [f"  DigiKeyboard.delay({delay_ms});  // EvilCrow-Cable delay: {delay_ms}ms"]
        except (ValueError, IndexError):
            return ["  // ERROR: Invalid delay value"]

    def _encode_string_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: STRING command missing text"]
        text = command.parameters[0]
        return [f'  DigiKeyboard.print("{text}");  // EvilCrow-Cable string input']

    def _encode_modifier_combo_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: MODIFIER_COMBO command missing parameters"]
        lines = ["  // EvilCrow-Cable stealth modifier combo"]
        for param in command.parameters:
            key_code = self._get_evilcrow_keycode(param.upper()) if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT'] else self._get_evilcrow_keycode(param)
            lines.append(f"  DigiKeyboard.sendKeyPress({key_code});  // Press {param}")
        return lines

    def _encode_random_delay_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if len(command.parameters) < 2:
            return ["  // ERROR: RANDOM_DELAY command missing min/max values"]
        try:
            min_delay = int(command.parameters[0])
            max_delay = int(command.parameters[1])
            return [
                f"  // EvilCrow-Cable stealth random delay: {min_delay}ms to {max_delay}ms",
                "  int random_delay = random(min_delay, max_delay);",
                "  DigiKeyboard.delay(random_delay);"
            ]
        except ValueError:
            return ["  // ERROR: Invalid random delay values"]

    def _encode_repeat_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: REPEAT command missing count"]
        try:
            repeat_count = int(command.parameters[0])
            return [
                f"  // REPEAT: Repeat last command {repeat_count} times",
                f"  // Note: EvilCrow-Cable optimized repeat functionality",
                f"  for (int i = 0; i < {repeat_count}; i++) {{",
                f"    // Placeholder for repeated command",
                f"  }}"
            ]
        except ValueError:
            return ["  // ERROR: Invalid repeat count"]

    def _encode_default_delay_evilcrow(self, command: HappyFrogCommand) -> List[str]:
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

    def _encode_if_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: IF command missing condition"]
        condition = command.parameters[0]
        return [
            f"  // IF: Conditional execution based on '{condition}'",
            f"  // Note: This is a simplified condition check for EvilCrow-Cable",
            f"  if (true) {{  // Placeholder for condition: {condition}"
        ]

    def _encode_else_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        return [
            "  // ELSE: Alternative execution path",
            "  } else {"
        ]

    def _encode_endif_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        return [
            "  // ENDIF: End conditional block",
            "  }"
        ]

    def _encode_while_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: WHILE command missing condition"]
        condition = command.parameters[0]
        return [
            f"  // WHILE: Loop execution based on '{condition}'",
            f"  // Note: This is a simplified loop condition for EvilCrow-Cable",
            f"  while (true) {{  // Placeholder for condition: {condition}"
        ]

    def _encode_endwhile_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        return [
            "  // ENDWHILE: End loop block",
            "  }"
        ]

    def _encode_log_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: LOG command missing message"]
        message = command.parameters[0]
        return [
            f"  // LOG: {message}",
            f"  // Note: EvilCrow-Cable has limited serial output capabilities"
        ]

    def _encode_validate_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: VALIDATE command missing condition"]
        condition = command.parameters[0]
        return [
            f"  // VALIDATE: Check environment condition '{condition}'",
            f"  // Note: This is a placeholder for environment validation on EvilCrow-Cable",
            f"  // EvilCrow-Cable has limited validation capabilities due to memory constraints"
        ]

    def _encode_safe_mode_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        if not command.parameters:
            return ["  // ERROR: SAFE_MODE command missing ON/OFF value"]
        mode = command.parameters[0].upper()
        if mode not in ['ON', 'OFF']:
            return ["  // ERROR: SAFE_MODE must be ON or OFF"]
        return [
            f"  // SAFE_MODE: {'Enabled' if mode == 'ON' else 'Disabled'} safe mode restrictions",
            f"  bool safe_mode = {str(mode == 'ON').lower()};"
        ]

    def _encode_pause_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        return [
            "  // PAUSE: Waiting for user input (press any key to continue)",
            "  // Note: In EvilCrow-Cable, we'll use a long delay as a simple pause",
            "  // For more sophisticated pause functionality, consider using WiFi input",
            "  DigiKeyboard.delay(5000);  // Pause for 5 seconds (Ducky Script PAUSE equivalent)"
        ]

    def _encode_comment_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        comment_text = command.parameters[0] if command.parameters else ""
        return [f"  // {comment_text}"]

    def _encode_standard_command_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        key_code = self._get_evilcrow_keycode(command.command_type.value)
        return [f"  DigiKeyboard.sendKeyPress({key_code});  // EvilCrow-Cable key press: {command.command_type.value}"]

    def _get_evilcrow_keycode(self, key: str) -> str:
        key = key.upper()
        if key == 'MOD': return "KEY_GUI"
        elif key == 'CTRL': return "KEY_CTRL"
        elif key == 'SHIFT': return "KEY_SHIFT"
        elif key == 'ALT': return "KEY_ALT"
        elif key == 'ENTER': return "KEY_ENTER"
        elif key == 'TAB': return "KEY_TAB"
        elif key == 'ESC' or key == 'ESCAPE': return "KEY_ESC"
        elif key == 'SPACE': return "KEY_SPACE"
        elif key == 'DELETE': return "KEY_DELETE"
        elif key == 'BACKSPACE': return "KEY_BACKSPACE"
        elif key == 'UP': return "KEY_UP_ARROW"
        elif key == 'DOWN': return "KEY_DOWN_ARROW"
        elif key == 'LEFT': return "KEY_LEFT_ARROW"
        elif key == 'RIGHT': return "KEY_RIGHT_ARROW"
        elif key in ['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']: return f"KEY_{key}"
        elif key == 'HOME': return "KEY_HOME"
        elif key == 'END': return "KEY_END"
        elif key == 'PAGE_UP': return "KEY_PAGE_UP"
        elif key == 'PAGE_DOWN': return "KEY_PAGE_DOWN"
        elif key == 'INSERT': return "KEY_INSERT"
        elif len(key) == 1 and (key.isalpha() or key.isdigit()): return f"KEY_{key}"
        else: return f"KEY_{key}"

    def get_device_info(self) -> Dict[str, Any]:
        return {
            'device_name': self.device_name,
            'processor': self.processor,
            'framework': self.framework,
            'optimizations': self.optimizations,
            'notes': 'Generates Arduino code for EvilCrow-Cable. Copy output to device as code.ino',
            'setup_notes': [
                'Install Arduino IDE with EvilCrow-Cable board support',
                'Select EvilCrow-Cable board',
                'Install DigiKeyboard library',
                'Connect WiFi module to RX/TX pins',
                'Upload code to device',
                'Test in controlled environment'
            ],
            'warnings': [
                'This device is designed for cybersecurity education and research',
                'Use only for authorized testing and educational purposes',
                'Ensure compliance with local laws and regulations'
            ]
        }

    def _generate_main_code(self, script: HappyFrogScript) -> List[str]:
        lines = []
        has_attackmode = any(
            cmd.command_type == CommandType.ATTACKMODE and 
            cmd.parameters and 
            ('HID' in ' '.join(cmd.parameters).upper() or 'WIFI' in ' '.join(cmd.parameters).upper())
            for cmd in script.commands
        )
        if self.production_mode:
            if has_attackmode:
                lines.append("  // Production code - executes immediately on device boot/plug-in")
                lines.append("  // ATTACKMODE detected - running payload automatically")
                lines.append("")
                lines.append("  // Wait for system to recognize the device")
                lines.append("  DigiKeyboard.delay(2000);")
                lines.append("")
            else:
                lines.append("  // Production code - main execution function")
                lines.append("  // Wait for system to recognize the device")
                lines.append("  DigiKeyboard.delay(2000);")
                lines.append("")
        else:
            lines.append("  // Main execution loop")
            lines.append("  // Wait for system to recognize the device")
            lines.append("  DigiKeyboard.delay(2000);")
            lines.append("")
        for i, command in enumerate(script.commands):
            lines.extend(self.encode_command(command))
            lines.append("")
        return lines
    
    def _encode_release_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        """Encode RELEASE command for EvilCrow-Cable."""
        return [
            "  // RELEASE: Release all pressed keys",
            "  DigiKeyboard.sendKeyPress(0);  // Release all keys"
        ]
    
    def _encode_wifi_send_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        """Encode WIFI_SEND command for EvilCrow-Cable."""
        if not command.parameters:
            return ["  // ERROR: WIFI_SEND command missing data"]
        
        data = command.parameters[0]
        return [
            f"  // WIFI_SEND: Send data over WiFi serial",
            f"  wifiSerial.println(\"{data}\");  // Send data via WiFi serial"
        ]
    
    def _encode_wifi_connect_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        """Encode WIFI_CONNECT command for EvilCrow-Cable."""
        if len(command.parameters) < 2:
            return ["  // ERROR: WIFI_CONNECT command missing SSID or password"]
        
        ssid = command.parameters[0]
        password = command.parameters[1]
        return [
            f"  // WIFI_CONNECT: Connect to WiFi network",
            f"  wifiSerial.println(\"CONNECT:{ssid}:{password}\");  // WiFi connect command"
        ]
    
    def _encode_shellwin_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        """Encode SHELLWIN command for EvilCrow-Cable."""
        if not command.parameters:
            return ["  // ERROR: SHELLWIN command missing IP address"]
        
        ip_address = command.parameters[0]
        return [
            f"  // SHELLWIN: Trigger Windows remote shell",
            f"  DigiKeyboard.print(\"ShellWin {ip_address}\");  // Windows remote shell payload",
            "  DigiKeyboard.sendKeyPress(KEY_ENTER);"
        ]
    
    def _encode_shellnix_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        """Encode SHELLNIX command for EvilCrow-Cable."""
        if not command.parameters:
            return ["  // ERROR: SHELLNIX command missing IP address"]
        
        ip_address = command.parameters[0]
        return [
            f"  // SHELLNIX: Trigger Linux remote shell",
            f"  DigiKeyboard.print(\"ShellNix {ip_address}\");  // Linux remote shell payload",
            "  DigiKeyboard.sendKeyPress(KEY_ENTER);"
        ]
    
    def _encode_shellmac_evilcrow(self, command: HappyFrogCommand) -> List[str]:
        """Encode SHELLMAC command for EvilCrow-Cable."""
        if not command.parameters:
            return ["  // ERROR: SHELLMAC command missing IP address"]
        
        ip_address = command.parameters[0]
        return [
            f"  // SHELLMAC: Trigger macOS remote shell",
            f"  DigiKeyboard.print(\"ShellMac {ip_address}\");  // macOS remote shell payload",
            "  DigiKeyboard.sendKeyPress(KEY_ENTER);"
        ] 