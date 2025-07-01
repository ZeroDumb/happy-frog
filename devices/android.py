"""
Happy Frog - Android Device Encoder

This module provides Android-specific code generation for HID emulation on Android devices.
Android devices have unique keyboard shortcuts, navigation patterns, and automation capabilities
that differ from traditional desktop systems.

Educational Purpose: Demonstrates Android-specific automation and mobile device security concepts.

Author: ZeroDumb
License: GNU GPLv3
"""

from typing import List, Dict, Any, Optional
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType


class AndroidEncoder:
    """
    Encoder that generates Android-specific automation code.
    
    Android devices have unique characteristics:
    - Different keyboard shortcuts than desktop systems
    - Touch-based navigation patterns
    - App-specific automation capabilities
    - Mobile-specific security considerations
    """
    
    def __init__(self):
        """Initialize the Android-specific encoder."""
        self.device_name = "Android Device"
        self.platform = "Android"
        self.framework = "Android HID"
        self.production_mode = False
        
        # Android-specific optimizations
        self.optimizations = {
            'touch_navigation': True,  # Support for touch-based navigation
            'android_shortcuts': True,  # Android-specific keyboard shortcuts
            'app_automation': True,  # App-specific automation
            'mobile_security': True,  # Mobile security considerations
        }
    
    def set_production_mode(self, production: bool = True):
        """Set production mode for immediate execution on boot."""
        self.production_mode = production
    
    def generate_header(self, script: HappyFrogScript) -> List[str]:
        """Generate Android-specific header code."""
        lines = []
        
        if self.production_mode:
            lines.append('/*')
            lines.append('Happy Frog - Android Device Production Code')
            lines.append('Android Automation Script - Runs immediately on connection')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Platform: {self.platform}')
            lines.append(f'Framework: {self.framework}')
            lines.append('Mode: Production (immediate execution)')
            lines.append('')
            lines.append('⚠️ PRODUCTION MODE: This code runs immediately when device connects!')
            lines.append('⚠️ Use only for authorized testing and educational purposes!')
            lines.append('⚠️ Android devices require specific permissions and setup!')
            lines.append('*/')
            lines.append('')
        else:
            lines.append('/*')
            lines.append('Happy Frog - Android Device Generated Code')
            lines.append('Educational Android Automation Script')
            lines.append('')
            lines.append(f'Device: {self.device_name}')
            lines.append(f'Platform: {self.platform}')
            lines.append(f'Framework: {self.framework}')
            lines.append('')
            lines.append('This code was automatically generated from a Happy Frog Script.')
            lines.append('Optimized for Android devices with HID capabilities.')
            lines.append('')
            lines.append('⚠️ IMPORTANT: Use only for educational purposes and authorized testing!')
            lines.append('⚠️ Android devices require specific permissions and setup!')
            lines.append('*/')
            lines.append('')
        
        # Android-specific includes and setup
        lines.append('#include "DigiKeyboard.h"  // Android HID keyboard library')
        lines.append('#include <SoftwareSerial.h> // For additional communication')
        lines.append('')
        lines.append('// Android-specific definitions')
        lines.append('#define ANDROID_DELAY 1000  // Standard Android delay')
        lines.append('#define TOUCH_DELAY 500     // Touch interaction delay')
        lines.append('')
        
        # Android-specific setup
        lines.append('void setup() {')
        lines.append('  // Initialize Android HID device')
        lines.append('  DigiKeyboard.update();')
        lines.append('  ')
        lines.append('  // Android-specific startup delay')
        lines.append('  DigiKeyboard.delay(2000);  // Wait for Android to recognize device')
        lines.append('}')
        lines.append('')
        
        if self.production_mode:
            lines.append('void loop() {')
            lines.append('  // Production mode - execute payload immediately')
            lines.append('  executeAndroidPayload();')
            lines.append('  while(true) { ; }  // Prevent re-execution')
            lines.append('}')
            lines.append('')
        else:
            lines.append('void loop() {')
            lines.append('  // Educational mode - main execution - runs once')
            lines.append('  executeAndroidPayload();')
            lines.append('  while(true) { ; }  // Prevent re-execution')
            lines.append('}')
            lines.append('')
        
        lines.append('void executeAndroidPayload() {')
        lines.append('  // Generated Happy Frog payload for Android devices')
        lines.append('')
        
        return lines
    
    def generate_footer(self) -> List[str]:
        """Generate Android-specific footer code."""
        lines = []
        
        lines.append('  // End of Android payload')
        lines.append('}')
        lines.append('')
        lines.append('/*')
        if self.production_mode:
            lines.append('End of Happy Frog Production Code for Android')
            lines.append('')
            lines.append('Production Notes:')
            lines.append('- This code runs immediately on device connection')
            lines.append('- Optimized for Android-specific automation')
            lines.append('- Supports Android keyboard shortcuts and navigation')
            lines.append('- Mobile security considerations implemented')
        else:
            lines.append('End of Happy Frog Generated Code for Android')
            lines.append('')
            lines.append('Educational Notes:')
            lines.append('- Android devices have unique automation patterns')
            lines.append('- Touch-based navigation requires different approaches')
            lines.append('- Mobile security differs from desktop systems')
            lines.append('- App-specific automation capabilities available')
        lines.append('')
        lines.append('Android Setup Requirements:')
        lines.append('- USB debugging enabled on target device')
        lines.append('- HID device permissions granted')
        lines.append('- Appropriate Android version compatibility')
        lines.append('- Test in controlled environment only')
        lines.append('')
        lines.append('For more information, visit: https://github.com/ZeroDumb/happy-frog')
        lines.append('*/')
        
        return lines
    
    def encode_command(self, command: HappyFrogCommand) -> List[str]:
        """Encode a command specifically for Android devices."""
        lines = []
        
        # Add Android-specific comment
        comment = f"  // Android Command: {command.raw_text}"
        lines.append(comment)
        
        # Handle comment lines (lines starting with #)
        if command.raw_text.strip().startswith('#'):
            # Skip comment lines - they're already handled by the comment above
            return lines
        
        # Handle Android-specific commands
        if command.command_type == CommandType.ATTACKMODE:
            lines.extend(self._encode_attackmode_android(command))
        elif command.command_type == CommandType.DELAY:
            lines.extend(self._encode_delay_android(command))
        elif command.command_type == CommandType.STRING:
            lines.extend(self._encode_string_android(command))
        elif command.command_type == CommandType.MODIFIER_COMBO:
            lines.extend(self._encode_modifier_combo_android(command))
        elif command.command_type == CommandType.ANDROID_HOME:
            lines.extend(self._encode_android_home(command))
        elif command.command_type == CommandType.ANDROID_BACK:
            lines.extend(self._encode_android_back(command))
        elif command.command_type == CommandType.ANDROID_MENU:
            lines.extend(self._encode_android_menu(command))
        elif command.command_type == CommandType.ANDROID_APP_SWITCH:
            lines.extend(self._encode_android_app_switch(command))
        elif command.command_type == CommandType.ANDROID_NOTIFICATIONS:
            lines.extend(self._encode_android_notifications(command))
        elif command.command_type == CommandType.ANDROID_QUICK_SETTINGS:
            lines.extend(self._encode_android_quick_settings(command))
        elif command.command_type == CommandType.ANDROID_SCREENSHOT:
            lines.extend(self._encode_android_screenshot(command))
        elif command.command_type == CommandType.ANDROID_VOLUME_UP:
            lines.extend(self._encode_android_volume_up(command))
        elif command.command_type == CommandType.ANDROID_VOLUME_DOWN:
            lines.extend(self._encode_android_volume_down(command))
        elif command.command_type == CommandType.ANDROID_MUTE:
            lines.extend(self._encode_android_mute(command))
        elif command.command_type == CommandType.ANDROID_POWER:
            lines.extend(self._encode_android_power(command))
        elif command.command_type == CommandType.ANDROID_OPEN_APP:
            lines.extend(self._encode_android_open_app(command))
        elif command.command_type == CommandType.ANDROID_CLOSE_APP:
            lines.extend(self._encode_android_close_app(command))
        elif command.command_type == CommandType.ANDROID_CLEAR_RECENTS:
            lines.extend(self._encode_android_clear_recents(command))
        elif command.command_type == CommandType.ANDROID_GOOGLE_ASSISTANT:
            lines.extend(self._encode_android_google_assistant(command))
        elif command.command_type == CommandType.ANDROID_SPLIT_SCREEN:
            lines.extend(self._encode_android_split_screen(command))
        elif command.command_type == CommandType.ANDROID_PIP_MODE:
            lines.extend(self._encode_android_pip_mode(command))
        elif command.command_type == CommandType.ANDROID_ACCESSIBILITY:
            lines.extend(self._encode_android_accessibility(command))
        elif command.command_type == CommandType.ANDROID_DEVELOPER_OPTIONS:
            lines.extend(self._encode_android_developer_options(command))
        elif command.command_type in [CommandType.COMMENT, CommandType.REM]:
            lines.extend(self._encode_comment_android(command))
        else:
            # Use standard encoding for other commands
            lines.extend(self._encode_standard_command_android(command))
        
        return lines
    
    def _encode_attackmode_android(self, command: HappyFrogCommand) -> List[str]:
        """Encode ATTACKMODE command for Android."""
        if command.parameters:
            mode_config = ' '.join(command.parameters).upper()
            if 'ANDROID' in mode_config:
                return [
                    f"  // ATTACKMODE: Configured for Android automation ({mode_config})",
                    f"  // Note: This device is configured for Android-specific operations",
                    f"  // Configuration: {mode_config}"
                ]
            else:
                return [
                    f"  // ATTACKMODE: Configured with '{mode_config}'",
                    f"  // Note: This is an Android automation configuration",
                    f"  // Configuration: {mode_config}"
                ]
        else:
            return ["  // ATTACKMODE: Android automation mode configuration"]
    
    def _encode_delay_android(self, command: HappyFrogCommand) -> List[str]:
        """Encode delay with Android-specific optimizations."""
        try:
            delay_ms = int(command.parameters[0])
            if delay_ms < 0:
                raise ValueError("Delay value must be non-negative")
            
            # Android-specific delay optimization
            if delay_ms < 100:
                return [f"  DigiKeyboard.delay({delay_ms});  // Android touch delay: {delay_ms}ms"]
            else:
                return [f"  DigiKeyboard.delay({delay_ms});  // Android delay: {delay_ms}ms"]
                
        except (ValueError, IndexError):
            return ["  // ERROR: Invalid delay value"]
    
    def _encode_string_android(self, command: HappyFrogCommand) -> List[str]:
        """Encode string with Android-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: STRING command missing text"]
        
        text = command.parameters[0]
        # Android-specific string input
        return [
            f'  DigiKeyboard.print("{text}");  // Android text input'
        ]
    
    def _encode_modifier_combo_android(self, command: HappyFrogCommand) -> List[str]:
        """Encode modifier combo with Android-specific optimizations."""
        if not command.parameters:
            return ["  // ERROR: MODIFIER_COMBO command missing parameters"]
        
        lines = []
        lines.append("  // Android optimized modifier combo")
        
        # Press all keys in the combo
        for param in command.parameters:
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_android_keycode(param.upper())
                lines.append(f"  DigiKeyboard.sendKeyPress({key_code});  // Press {param}")
            else:
                key_code = self._get_android_keycode(param)
                lines.append(f"  DigiKeyboard.sendKeyPress({key_code});  // Press {param}")
        
        # Release all keys in reverse order
        for param in reversed(command.parameters):
            if param.upper() in ['MOD', 'CTRL', 'SHIFT', 'ALT']:
                key_code = self._get_android_keycode(param.upper())
                lines.append(f"  DigiKeyboard.sendKeyPress(0);  // Release {param}")
            else:
                key_code = self._get_android_keycode(param)
                lines.append(f"  DigiKeyboard.sendKeyPress(0);  // Release {param}")
        
        return lines
    
    def _encode_android_home(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android HOME button."""
        return [
            "  // Android HOME button",
            "  DigiKeyboard.sendKeyPress(KEY_HOME);  // Navigate to home screen"
        ]
    
    def _encode_android_back(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android BACK button."""
        return [
            "  // Android BACK button",
            "  DigiKeyboard.sendKeyPress(KEY_BACK);  // Navigate back"
        ]
    
    def _encode_android_menu(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android MENU button."""
        return [
            "  // Android MENU button",
            "  DigiKeyboard.sendKeyPress(KEY_MENU);  // Open context menu"
        ]
    
    def _encode_android_app_switch(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android APP SWITCH button."""
        return [
            "  // Android APP SWITCH button",
            "  DigiKeyboard.sendKeyPress(KEY_APP_SWITCH);  // Switch between recent apps"
        ]
    
    def _encode_android_notifications(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android NOTIFICATIONS panel."""
        return [
            "  // Android NOTIFICATIONS panel",
            "  DigiKeyboard.sendKeyPress(KEY_NOTIFICATIONS);  // Open notifications panel"
        ]
    
    def _encode_android_quick_settings(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android QUICK SETTINGS panel."""
        return [
            "  // Android QUICK SETTINGS panel",
            "  DigiKeyboard.sendKeyPress(KEY_QUICK_SETTINGS);  // Open quick settings"
        ]
    
    def _encode_android_screenshot(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android SCREENSHOT."""
        return [
            "  // Android SCREENSHOT",
            "  DigiKeyboard.sendKeyPress(KEY_POWER);  // Press power",
            "  DigiKeyboard.delay(100);",
            "  DigiKeyboard.sendKeyPress(KEY_VOLUME_DOWN);  // Press volume down",
            "  DigiKeyboard.delay(100);",
            "  DigiKeyboard.sendKeyPress(0);  // Release keys"
        ]
    
    def _encode_android_volume_up(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android VOLUME UP."""
        return [
            "  // Android VOLUME UP",
            "  DigiKeyboard.sendKeyPress(KEY_VOLUME_UP);  // Increase volume"
        ]
    
    def _encode_android_volume_down(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android VOLUME DOWN."""
        return [
            "  // Android VOLUME DOWN",
            "  DigiKeyboard.sendKeyPress(KEY_VOLUME_DOWN);  // Decrease volume"
        ]
    
    def _encode_android_mute(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android MUTE."""
        return [
            "  // Android MUTE",
            "  DigiKeyboard.sendKeyPress(KEY_MUTE);  // Mute audio"
        ]
    
    def _encode_android_power(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android POWER button."""
        return [
            "  // Android POWER button",
            "  DigiKeyboard.sendKeyPress(KEY_POWER);  // Power button press"
        ]
    
    def _encode_android_open_app(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android OPEN APP command."""
        if not command.parameters:
            return ["  // ERROR: ANDROID_OPEN_APP command missing app name"]
        
        app_name = command.parameters[0]
        return [
            f"  // Android OPEN APP: {app_name}",
            "  DigiKeyboard.sendKeyPress(KEY_HOME);  // Go to home",
            "  DigiKeyboard.delay(500);",
            f'  DigiKeyboard.print("{app_name}");  // Type app name',
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_ENTER);  // Open app"
        ]
    
    def _encode_android_close_app(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android CLOSE APP command."""
        return [
            "  // Android CLOSE APP",
            "  DigiKeyboard.sendKeyPress(KEY_APP_SWITCH);  // Open recent apps",
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_UP);  // Select app",
            "  DigiKeyboard.delay(100);",
            "  DigiKeyboard.sendKeyPress(KEY_ENTER);  // Close app"
        ]
    
    def _encode_android_clear_recents(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android CLEAR RECENTS command."""
        return [
            "  // Android CLEAR RECENTS",
            "  DigiKeyboard.sendKeyPress(KEY_APP_SWITCH);  // Open recent apps",
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_CLEAR_ALL);  // Clear all recent apps"
        ]
    
    def _encode_android_google_assistant(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android GOOGLE ASSISTANT activation."""
        return [
            "  // Android GOOGLE ASSISTANT",
            "  DigiKeyboard.sendKeyPress(KEY_ASSISTANT);  // Activate Google Assistant"
        ]
    
    def _encode_android_split_screen(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android SPLIT SCREEN mode."""
        return [
            "  // Android SPLIT SCREEN",
            "  DigiKeyboard.sendKeyPress(KEY_APP_SWITCH);  // Open recent apps",
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_SPLIT_SCREEN);  // Enable split screen"
        ]
    
    def _encode_android_pip_mode(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android PICTURE-IN-PICTURE mode."""
        return [
            "  // Android PICTURE-IN-PICTURE",
            "  DigiKeyboard.sendKeyPress(KEY_HOME);  // Go to home",
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_PIP);  // Enable PiP mode"
        ]
    
    def _encode_android_accessibility(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android ACCESSIBILITY menu."""
        return [
            "  // Android ACCESSIBILITY",
            "  DigiKeyboard.sendKeyPress(KEY_ACCESSIBILITY);  // Open accessibility menu"
        ]
    
    def _encode_android_developer_options(self, command: HappyFrogCommand) -> List[str]:
        """Encode Android DEVELOPER OPTIONS access."""
        return [
            "  // Android DEVELOPER OPTIONS",
            "  DigiKeyboard.sendKeyPress(KEY_HOME);  // Go to home",
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_SETTINGS);  // Open settings",
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_ABOUT_PHONE);  // About phone",
            "  DigiKeyboard.delay(500);",
            "  DigiKeyboard.sendKeyPress(KEY_BUILD_NUMBER);  // Tap build number 7 times"
        ]
    
    def _encode_comment_android(self, command: HappyFrogCommand) -> List[str]:
        """Encode comment command for Android."""
        comment_text = command.parameters[0] if command.parameters else ""
        return [
            f"  // {comment_text}"
        ]
    
    def _encode_standard_command_android(self, command: HappyFrogCommand) -> List[str]:
        """Encode standard commands for Android."""
        key_code = self._get_android_keycode(command.command_type.value)
        return [
            f"  DigiKeyboard.sendKeyPress({key_code});  // Android key press: {command.command_type.value}"
        ]
    
    def _get_android_keycode(self, key: str) -> str:
        """Get Android keycode for a key."""
        key = key.upper()
        
        # Android-specific mappings
        android_mappings = {
            # Navigation keys
            'HOME': 'KEY_HOME',
            'BACK': 'KEY_BACK',
            'MENU': 'KEY_MENU',
            'APP_SWITCH': 'KEY_APP_SWITCH',
            'NOTIFICATIONS': 'KEY_NOTIFICATIONS',
            'QUICK_SETTINGS': 'KEY_QUICK_SETTINGS',
            
            # Volume and power
            'VOLUME_UP': 'KEY_VOLUME_UP',
            'VOLUME_DOWN': 'KEY_VOLUME_DOWN',
            'MUTE': 'KEY_MUTE',
            'POWER': 'KEY_POWER',
            
            # Android-specific functions
            'ASSISTANT': 'KEY_ASSISTANT',
            'SPLIT_SCREEN': 'KEY_SPLIT_SCREEN',
            'PIP': 'KEY_PIP',
            'ACCESSIBILITY': 'KEY_ACCESSIBILITY',
            'CLEAR_ALL': 'KEY_CLEAR_ALL',
            
            # Settings and system
            'SETTINGS': 'KEY_SETTINGS',
            'ABOUT_PHONE': 'KEY_ABOUT_PHONE',
            'BUILD_NUMBER': 'KEY_BUILD_NUMBER',
            
            # Standard keys
            'ENTER': 'KEY_ENTER',
            'SPACE': "' '",
            'TAB': 'KEY_TAB',
            'BACKSPACE': 'KEY_BACKSPACE',
            'DELETE': 'KEY_DELETE',
            'ESCAPE': 'KEY_ESC',
            'UP': 'KEY_UP_ARROW',
            'DOWN': 'KEY_DOWN_ARROW',
            'LEFT': 'KEY_LEFT_ARROW',
            'RIGHT': 'KEY_RIGHT_ARROW',
            
            # Modifier keys
            'MOD': 'KEY_GUI',
            'CTRL': 'KEY_CTRL',
            'SHIFT': 'KEY_SHIFT',
            'ALT': 'KEY_ALT',
        }
        
        # Check for Android-specific keys first
        if key in android_mappings:
            return android_mappings[key]
        
        # Single letter keys
        if len(key) == 1 and key.isalpha():
            return f"'{key}'"
        
        # Number keys
        if key.isdigit():
            return f"'{key}'"
        
        # Default fallback
        return f"'{key}'"
    
    def get_device_info(self) -> Dict[str, Any]:
        """Get device information for Android."""
        return {
            'name': self.device_name,
            'platform': self.platform,
            'framework': self.framework,
            'price_range': 'Varies',
            'difficulty': 'Advanced',
            'features': [
                'Android-specific keyboard shortcuts',
                'Touch-based navigation support',
                'App automation capabilities',
                'Mobile security features',
                'Android system integration',
                'Accessibility automation',
                'Developer options access'
            ],
            'setup_notes': [
                'Enable USB debugging on target device',
                'Grant HID device permissions',
                'Install appropriate Android drivers',
                'Test in controlled environment',
                'Verify Android version compatibility'
            ],
            'notes': 'Generates Android-specific automation code. Requires Android device with HID support and appropriate permissions.'
        }
    
    def _generate_main_code(self, script: HappyFrogScript) -> List[str]:
        """Generate the main execution code with ATTACKMODE detection."""
        lines = []
        
        # Check if ATTACKMODE ANDROID is present for immediate execution
        has_attackmode = any(
            cmd.command_type == CommandType.ATTACKMODE and 
            cmd.parameters and 
            'ANDROID' in ' '.join(cmd.parameters).upper()
            for cmd in script.commands
        )
        
        if self.production_mode:
            if has_attackmode:
                lines.append("  // Production code - executes immediately on device connection")
                lines.append("  // ATTACKMODE ANDROID detected - running payload automatically")
                lines.append("")
                lines.append("  // Wait for Android to recognize the device")
                lines.append("  DigiKeyboard.delay(2000);")
                lines.append("")
            else:
                lines.append("  // Production code - main execution function")
                lines.append("  // Wait for Android to recognize the device")
                lines.append("  DigiKeyboard.delay(2000);")
                lines.append("")
        else:
            # Educational mode - always use main() function
            lines.append("  // Main execution loop")
            lines.append("  // Wait for Android to recognize the device")
            lines.append("  DigiKeyboard.delay(2000);")
            lines.append("")
        
        # Process each command
        for i, command in enumerate(script.commands):
            lines.extend(self.encode_command(command))
            lines.append("")  # Add blank line for readability
        
        return lines 