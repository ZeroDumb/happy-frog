"""
Happy Frog - Device Support Package

This package provides device-specific code generation for various microcontrollers
used in educational HID emulation projects.

Educational Purpose: This demonstrates microcontroller programming, HID emulation,
and cross-platform code generation concepts.

Author: ZeroDumb
License: GNU GPLv3
"""

from .device_manager import DeviceManager
from .xiao_rp2040 import XiaoRP2040Encoder
from .esp32 import ESP32Encoder
from .digispark import DigiSparkEncoder
from .teensy_4 import Teensy4Encoder
from .raspberry_pi_pico import RaspberryPiPicoEncoder
from .arduino_leonardo import ArduinoLeonardoEncoder
from .evilcrow_cable import EvilCrowCableEncoder

__version__ = "1.0.0"
__author__ = "ZeroDumb"
__license__ = "GNU GPLv3"

__all__ = [
    # Device manager
    "DeviceManager",
    
    # Encoder classes
    "XiaoRP2040Encoder",
    "ESP32Encoder", 
    "DigiSparkEncoder",
    "Teensy4Encoder",
    "RaspberryPiPicoEncoder",
    "ArduinoLeonardoEncoder",
    "EvilCrowCableEncoder",
] 