"""
Happy Frog - Device Manager

This module manages all supported devices and provides a unified interface
for device selection and code generation across different platforms.

Educational Purpose: Demonstrates device abstraction and multi-platform support.

Author: ZeroDumb
License: GNU GPLv3
"""

from typing import List, Dict, Any, Optional, Type
from happy_frog_parser import HappyFrogScript, HappyFrogCommand, CommandType

# Import all device encoders
from devices.raspberry_pi_pico import RaspberryPiPicoEncoder
from devices.arduino_leonardo import ArduinoLeonardoEncoder
from devices.teensy_4 import Teensy4Encoder
from devices.digispark import DigiSparkEncoder
from devices.esp32 import ESP32Encoder
from devices.xiao_rp2040 import XiaoRP2040Encoder
from devices.evilcrow_cable import EvilCrowCableEncoder


class DeviceManager:
    """
    Manages all supported devices and provides device selection capabilities.
    
    This class acts as a central hub for all device-specific encoders,
    allowing users to easily switch between different devices and platforms.
    """
    
    def __init__(self):
        """Initialize the device manager with all supported devices."""
        self.devices = {
            'raspberry_pi_pico': {
                'name': 'Raspberry Pi Pico',
                'encoder_class': RaspberryPiPicoEncoder,
                'description': 'Low-cost, high-performance device with CircuitPython support',
                'difficulty': 'Beginner',
                'price_range': '$4-8',
                'best_for': ['Education', 'Cost-effective projects', 'CircuitPython learning']
            },
            'arduino_leonardo': {
                'name': 'Arduino Leonardo',
                'encoder_class': ArduinoLeonardoEncoder,
                'description': 'Classic choice with native USB HID support',
                'difficulty': 'Intermediate',
                'price_range': '$15-25',
                'best_for': ['Traditional Arduino projects', 'Security research', 'Reliable HID emulation']
            },
            'teensy_4': {
                'name': 'Teensy 4.0',
                'encoder_class': Teensy4Encoder,
                'description': 'High-performance device for advanced applications',
                'difficulty': 'Advanced',
                'price_range': '$25-35',
                'best_for': ['High-performance applications', 'Advanced security research', 'Complex automation']
            },
            'digispark': {
                'name': 'DigiSpark',
                'encoder_class': DigiSparkEncoder,
                'description': 'Ultra-compact device for portable applications',
                'difficulty': 'Beginner',
                'price_range': '$2-5',
                'best_for': ['Portable projects', 'Ultra-compact applications', 'Cost-sensitive projects']
            },
            'esp32': {
                'name': 'ESP32',
                'encoder_class': ESP32Encoder,
                'description': 'WiFi-enabled device for wireless applications',
                'difficulty': 'Intermediate',
                'price_range': '$5-15',
                'best_for': ['Wireless applications', 'IoT projects', 'Remote control scenarios']
            },
            'xiao_rp2040': {
                'name': 'Seeed Xiao RP2040',
                'encoder_class': XiaoRP2040Encoder,
                'description': 'Affordable, compact RP2040 device for CircuitPython HID emulation',
                'difficulty': 'Beginner',
                'price_range': '$5-10',
                'best_for': ['Education', 'Compact projects', 'CircuitPython HID']
            },
            'evilcrow_cable': {
                'name': 'EvilCrow-Cable',
                'encoder_class': EvilCrowCableEncoder,
                'description': 'Specialized BadUSB device with built-in USB-C connectors',
                'difficulty': 'Advanced',
                'price_range': '$15-30',
                'best_for': ['Advanced security research', 'BadUSB demonstrations', 'Stealth operations']
            },
        }
    
    def list_devices(self) -> List[Dict[str, Any]]:
        """List all supported devices with their information."""
        device_list = []
        for device_id, device_info in self.devices.items():
            device_list.append({
                'id': device_id,
                'name': device_info['name'],
                'description': device_info['description'],
                'difficulty': device_info['difficulty'],
                'price_range': device_info['price_range'],
                'best_for': device_info['best_for']
            })
        return device_list
    
    def get_device_info(self, device_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific device."""
        if device_id not in self.devices:
            return None
        
        device_info = self.devices[device_id].copy()
        device_info['id'] = device_id
        
        # Get additional info from the encoder
        encoder_class = device_info['encoder_class']
        encoder_instance = encoder_class()
        device_info.update(encoder_instance.get_device_info())
        
        return device_info
    
    def create_encoder(self, device_id: str):
        """Create an encoder instance for the specified device."""
        if device_id not in self.devices:
            raise ValueError(f"Unknown device: {device_id}")
        
        encoder_class = self.devices[device_id]['encoder_class']
        return encoder_class()
    
    def encode_script(self, script: HappyFrogScript, device_id: str, output_file: Optional[str] = None, production_mode: bool = False) -> str:
        """Encode a script for a specific device."""
        encoder = self.create_encoder(device_id)
        
        # Set production mode if supported
        if hasattr(encoder, 'set_production_mode'):
            encoder.set_production_mode(production_mode)
        
        # Generate device-specific code
        code_lines = []
        
        # Add header
        code_lines.extend(encoder.generate_header(script))
        
        # Add main execution code - use device-specific method if available
        if hasattr(encoder, '_generate_main_code'):
            code_lines.extend(encoder._generate_main_code(script))
        else:
            code_lines.extend(self._generate_main_code(encoder, script))
        
        # Add footer
        code_lines.extend(encoder.generate_footer())
        
        # Join all lines
        code = '\n'.join(code_lines)
        
        # Write to file if specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(code)
        
        return code
    
    def _generate_main_code(self, encoder, script: HappyFrogScript) -> List[str]:
        """Generate the main execution code for a device."""
        lines = []
        
        # Process each command
        for i, command in enumerate(script.commands):
            lines.extend(encoder.encode_command(command))
            lines.append("")  # Add blank line for readability
        
        return lines
    
    def recommend_device(self, criteria: Dict[str, Any]) -> str:
        """Recommend a device based on user criteria."""
        recommendations = []
        
        for device_id, device_info in self.devices.items():
            score = 0
            
            # Price criteria
            if 'max_price' in criteria:
                price_range = device_info['price_range']
                max_price = self._extract_max_price(price_range)
                if max_price <= criteria['max_price']:
                    score += 3
            
            # Difficulty criteria
            if 'difficulty' in criteria:
                if device_info['difficulty'].lower() == criteria['difficulty'].lower():
                    score += 2
            
            # Use case criteria
            if 'use_case' in criteria:
                use_case = criteria['use_case'].lower()
                for best_for in device_info['best_for']:
                    if use_case in best_for.lower():
                        score += 2
            
            # Wireless requirement
            if criteria.get('wireless', False) and device_id == 'esp32':
                score += 5
            
            # Compact requirement
            if criteria.get('compact', False) and device_id == 'digispark':
                score += 4
            
            # Performance requirement
            if criteria.get('high_performance', False) and device_id == 'teensy_4':
                score += 4
            
            recommendations.append((device_id, score))
        
        # Sort by score and return the best match
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[0][0] if recommendations else 'raspberry_pi_pico'
    
    def _extract_max_price(self, price_range: str) -> int:
        """Extract the maximum price from a price range string."""
        try:
            # Extract numbers from strings like "$4-8" or "$15-25"
            import re
            numbers = re.findall(r'\d+', price_range)
            if numbers:
                return max(int(num) for num in numbers)
        except:
            pass
        return 50  # Default fallback
    
    def get_device_comparison(self) -> Dict[str, Any]:
        """Get a comparison table of all devices."""
        comparison = {
            'headers': ['Device', 'Price', 'Difficulty', 'Best For', 'Key Features'],
            'rows': []
        }
        
        for device_id, device_info in self.devices.items():
            encoder = self.create_encoder(device_id)
            device_details = encoder.get_device_info()
            
            comparison['rows'].append([
                device_info['name'],
                device_info['price_range'],
                device_info['difficulty'],
                ', '.join(device_info['best_for']),
                ', '.join(device_details['features'][:3])  # First 3 features
            ])
        
        return comparison
    
    def validate_device_support(self, device_id: str, script: HappyFrogScript) -> List[str]:
        """Validate if a device can support all commands in a script."""
        warnings = []
        
        if device_id not in self.devices:
            warnings.append(f"Unknown device: {device_id}")
            return warnings
        
        # Check for device-specific limitations
        if device_id == 'digispark':
            # DigiSpark has limited memory
            if len(script.commands) > 50:
                warnings.append("DigiSpark has limited memory - large scripts may not fit")
        
        elif device_id == 'esp32':
            # ESP32 requires Bluetooth connection
            warnings.append("ESP32 requires Bluetooth connection to target device")
        
        # Check for advanced features that might not be supported
        advanced_commands = [CommandType.RANDOM_DELAY, CommandType.LOG, CommandType.VALIDATE]
        for command in script.commands:
            if command.command_type in advanced_commands:
                warnings.append(f"Advanced command '{command.command_type.value}' may have limited support on {device_id}")
        
        return warnings 