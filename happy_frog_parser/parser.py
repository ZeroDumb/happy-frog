"""
Happy Frog - Happy Frog Script Parser

This module implements a parser for Happy Frog Script v1.0, converting script files
into an internal representation that can be processed by encoders.

Educational Purpose: This demonstrates lexical analysis, parsing, and abstract
syntax tree construction - fundamental concepts in compiler design and language processing.

Author: ZeroDumb
License: GNU GPLv3
"""

import re
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum


class HappyFrogScriptError(Exception):
    """Custom exception for Happy Frog Script parsing errors."""
    pass


class CommandType(Enum):
    """Enumeration of supported Happy Frog Script commands."""
    DELAY = "DELAY"
    STRING = "STRING"
    ENTER = "ENTER"
    SPACE = "SPACE"
    TAB = "TAB"
    BACKSPACE = "BACKSPACE"
    DELETE = "DELETE"
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    HOME = "HOME"
    END = "END"
    INSERT = "INSERT"
    PAGE_UP = "PAGE_UP"
    PAGE_DOWN = "PAGE_DOWN"
    ESCAPE = "ESCAPE"
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"
    F10 = "F10"
    F11 = "F11"
    F12 = "F12"
    CTRL = "CTRL"
    SHIFT = "SHIFT"
    ALT = "ALT"
    MOD = "MOD"  # Modifier key (Windows/Command/Super)
    MODIFIER_COMBO = "MODIFIER_COMBO"  # For combos like MOD r
    PAUSE = "PAUSE"  # Pause execution (Ducky Script compatibility)
    
    # Advanced Ducky Script features
    REPEAT = "REPEAT"  # Repeat previous command n times
    DEFAULT_DELAY = "DEFAULT_DELAY"  # Set default delay between commands
    DEFAULTDELAY = "DEFAULT_DELAY"  # Alternative syntax
    
    # Conditional logic (Happy Frog exclusive)
    IF = "IF"  # Conditional execution
    ELSE = "ELSE"  # Else block
    ENDIF = "ENDIF"  # End conditional block
    WHILE = "WHILE"  # While loop
    ENDWHILE = "ENDWHILE"  # End while loop
    
    # Happy Frog exclusive features
    RANDOM_DELAY = "RANDOM_DELAY"  # Random delay for human-like behavior
    LOG = "LOG"  # Logging for debugging
    VALIDATE = "VALIDATE"  # Validate environment before execution
    SAFE_MODE = "SAFE_MODE"  # Enable safe mode restrictions
    
    # BadUSB compatibility commands
    ATTACKMODE = "ATTACKMODE"  # BadUSB attack mode configuration
    
    # EvilCrow-Cable specialty commands
    RELEASE = "RELEASE"  # Release all pressed keys
    WIFI_SEND = "WIFI_SEND"  # Send data over WiFi serial
    WIFI_CONNECT = "WIFI_CONNECT"  # Connect to WiFi network
    SHELLWIN = "SHELLWIN"  # Trigger Windows remote shell
    SHELLNIX = "SHELLNIX"  # Trigger Linux remote shell
    SHELLMAC = "SHELLMAC"  # Trigger macOS remote shell
    
    # Android-specific commands
    ANDROID_HOME = "ANDROID_HOME"  # Android home button
    ANDROID_BACK = "ANDROID_BACK"  # Android back button
    ANDROID_MENU = "ANDROID_MENU"  # Android menu button
    ANDROID_APP_SWITCH = "ANDROID_APP_SWITCH"  # Android app switcher
    ANDROID_NOTIFICATIONS = "ANDROID_NOTIFICATIONS"  # Android notifications panel
    ANDROID_QUICK_SETTINGS = "ANDROID_QUICK_SETTINGS"  # Android quick settings
    ANDROID_SCREENSHOT = "ANDROID_SCREENSHOT"  # Android screenshot
    ANDROID_VOLUME_UP = "ANDROID_VOLUME_UP"  # Android volume up
    ANDROID_VOLUME_DOWN = "ANDROID_VOLUME_DOWN"  # Android volume down
    ANDROID_MUTE = "ANDROID_MUTE"  # Android mute
    ANDROID_POWER = "ANDROID_POWER"  # Android power button
    ANDROID_OPEN_APP = "ANDROID_OPEN_APP"  # Android open app
    ANDROID_CLOSE_APP = "ANDROID_CLOSE_APP"  # Android close app
    ANDROID_CLEAR_RECENTS = "ANDROID_CLEAR_RECENTS"  # Android clear recent apps
    ANDROID_GOOGLE_ASSISTANT = "ANDROID_GOOGLE_ASSISTANT"  # Android Google Assistant
    ANDROID_SPLIT_SCREEN = "ANDROID_SPLIT_SCREEN"  # Android split screen
    ANDROID_PIP_MODE = "ANDROID_PIP_MODE"  # Android picture-in-picture
    ANDROID_ACCESSIBILITY = "ANDROID_ACCESSIBILITY"  # Android accessibility
    ANDROID_DEVELOPER_OPTIONS = "ANDROID_DEVELOPER_OPTIONS"  # Android developer options
    
    COMMENT = "COMMENT"
    REM = "REM"  # Alternative comment syntax


@dataclass
class HappyFrogCommand:
    """Represents a single Happy Frog Script command with its parameters."""
    command_type: CommandType
    line_number: int
    raw_text: str
    parameters: Optional[List[str]] = None
    
    def __post_init__(self):
        if self.parameters is None:
            self.parameters = []


@dataclass
class HappyFrogScript:
    """Represents a complete parsed Happy Frog Script."""
    commands: List[HappyFrogCommand]
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class HappyFrogParser:
    """
    Parser for Happy Frog Script v1.0 files.
    
    This parser implements a simple line-by-line parsing approach that's easy
    to understand and extend. It demonstrates basic lexical analysis and
    command recognition patterns.
    """
    
    def __init__(self):
        """Initialize the parser with command patterns."""
        # Define regex patterns for different command types
        self.command_patterns = {
            # Modifier+key combos (e.g., MOD r, CTRL ALT DEL) - must have at least 2 parts
            CommandType.MODIFIER_COMBO: re.compile(r'^(MOD|CTRL|SHIFT|ALT)(?:\s+(MOD|CTRL|SHIFT|ALT|[A-Z0-9]+))+$', re.IGNORECASE),
            # Delay command: DELAY <value> - captures any value for validation
            CommandType.DELAY: re.compile(r'^DELAY\s+(.+)$', re.IGNORECASE),
            
            # String command: STRING <text>
            CommandType.STRING: re.compile(r'^STRING\s+(.+)$', re.IGNORECASE),
            
            # Simple commands with no parameters
            CommandType.ENTER: re.compile(r'^ENTER$', re.IGNORECASE),
            CommandType.SPACE: re.compile(r'^SPACE$', re.IGNORECASE),
            CommandType.TAB: re.compile(r'^TAB$', re.IGNORECASE),
            CommandType.BACKSPACE: re.compile(r'^BACKSPACE$', re.IGNORECASE),
            CommandType.DELETE: re.compile(r'^DELETE$', re.IGNORECASE),
            
            # Arrow keys
            CommandType.UP: re.compile(r'^UP$', re.IGNORECASE),
            CommandType.DOWN: re.compile(r'^DOWN$', re.IGNORECASE),
            CommandType.LEFT: re.compile(r'^LEFT$', re.IGNORECASE),
            CommandType.RIGHT: re.compile(r'^RIGHT$', re.IGNORECASE),
            
            # Navigation keys
            CommandType.HOME: re.compile(r'^HOME$', re.IGNORECASE),
            CommandType.END: re.compile(r'^END$', re.IGNORECASE),
            CommandType.INSERT: re.compile(r'^INSERT$', re.IGNORECASE),
            CommandType.PAGE_UP: re.compile(r'^PAGE_UP$', re.IGNORECASE),
            CommandType.PAGE_DOWN: re.compile(r'^PAGE_DOWN$', re.IGNORECASE),
            CommandType.ESCAPE: re.compile(r'^ESCAPE$', re.IGNORECASE),
            
            # Function keys
            CommandType.F1: re.compile(r'^F1$', re.IGNORECASE),
            CommandType.F2: re.compile(r'^F2$', re.IGNORECASE),
            CommandType.F3: re.compile(r'^F3$', re.IGNORECASE),
            CommandType.F4: re.compile(r'^F4$', re.IGNORECASE),
            CommandType.F5: re.compile(r'^F5$', re.IGNORECASE),
            CommandType.F6: re.compile(r'^F6$', re.IGNORECASE),
            CommandType.F7: re.compile(r'^F7$', re.IGNORECASE),
            CommandType.F8: re.compile(r'^F8$', re.IGNORECASE),
            CommandType.F9: re.compile(r'^F9$', re.IGNORECASE),
            CommandType.F10: re.compile(r'^F10$', re.IGNORECASE),
            CommandType.F11: re.compile(r'^F11$', re.IGNORECASE),
            CommandType.F12: re.compile(r'^F12$', re.IGNORECASE),
            
            # Modifier keys (single keys)
            CommandType.CTRL: re.compile(r'^CTRL$', re.IGNORECASE),
            CommandType.SHIFT: re.compile(r'^SHIFT$', re.IGNORECASE),
            CommandType.ALT: re.compile(r'^ALT$', re.IGNORECASE),
            CommandType.MOD: re.compile(r'^MOD$', re.IGNORECASE),  # Modifier key
            
            # Execution control
            CommandType.PAUSE: re.compile(r'^PAUSE$', re.IGNORECASE),  # Pause execution
            
            # Advanced Ducky Script features
            CommandType.REPEAT: re.compile(r'^REPEAT\s+(\d+)$', re.IGNORECASE),  # REPEAT n
            CommandType.DEFAULT_DELAY: re.compile(r'^(DEFAULT_DELAY|DEFAULTDELAY)\s+(\d+)$', re.IGNORECASE),  # DEFAULT_DELAY or DEFAULTDELAY n
            
            # Conditional logic (Happy Frog exclusive)
            CommandType.IF: re.compile(r'^IF\s+(.+)$', re.IGNORECASE),  # IF condition
            CommandType.ELSE: re.compile(r'^ELSE$', re.IGNORECASE),  # ELSE
            CommandType.ENDIF: re.compile(r'^ENDIF$', re.IGNORECASE),  # ENDIF
            CommandType.WHILE: re.compile(r'^WHILE\s+(.+)$', re.IGNORECASE),  # WHILE condition
            CommandType.ENDWHILE: re.compile(r'^ENDWHILE$', re.IGNORECASE),  # ENDWHILE
            
            # Happy Frog exclusive features
            CommandType.RANDOM_DELAY: re.compile(r'^RANDOM_DELAY\s+(\d+)\s+(\d+)$', re.IGNORECASE),  # RANDOM_DELAY min max
            CommandType.LOG: re.compile(r'^LOG\s+(.+)$', re.IGNORECASE),  # LOG message
            CommandType.VALIDATE: re.compile(r'^VALIDATE\s+(.+)$', re.IGNORECASE),  # VALIDATE condition
            CommandType.SAFE_MODE: re.compile(r'^SAFE_MODE\s+(ON|OFF)$', re.IGNORECASE),  # SAFE_MODE ON/OFF
            
            # BadUSB compatibility commands
            CommandType.ATTACKMODE: re.compile(r'^ATTACKMODE\s+(.+)$', re.IGNORECASE),  # ATTACKMODE configuration
            
            # EvilCrow-Cable specialty commands
            CommandType.RELEASE: re.compile(r'^RELEASE$', re.IGNORECASE),  # RELEASE all keys
            CommandType.WIFI_SEND: re.compile(r'^WIFI_SEND\s+(.+)$', re.IGNORECASE),  # WIFI_SEND data
            CommandType.WIFI_CONNECT: re.compile(r'^WIFI_CONNECT\s+(\S+)\s+(\S+)$', re.IGNORECASE),  # WIFI_CONNECT ssid password
            CommandType.SHELLWIN: re.compile(r'^SHELLWIN\s+(\S+)$', re.IGNORECASE),  # SHELLWIN ip
            CommandType.SHELLNIX: re.compile(r'^SHELLNIX\s+(\S+)$', re.IGNORECASE),  # SHELLNIX ip
            CommandType.SHELLMAC: re.compile(r'^SHELLMAC\s+(\S+)$', re.IGNORECASE),  # SHELLMAC ip
            
            # Android-specific commands
            CommandType.ANDROID_HOME: re.compile(r'^ANDROID_HOME$', re.IGNORECASE),  # ANDROID_HOME
            CommandType.ANDROID_BACK: re.compile(r'^ANDROID_BACK$', re.IGNORECASE),  # ANDROID_BACK
            CommandType.ANDROID_MENU: re.compile(r'^ANDROID_MENU$', re.IGNORECASE),  # ANDROID_MENU
            CommandType.ANDROID_APP_SWITCH: re.compile(r'^ANDROID_APP_SWITCH$', re.IGNORECASE),  # ANDROID_APP_SWITCH
            CommandType.ANDROID_NOTIFICATIONS: re.compile(r'^ANDROID_NOTIFICATIONS$', re.IGNORECASE),  # ANDROID_NOTIFICATIONS
            CommandType.ANDROID_QUICK_SETTINGS: re.compile(r'^ANDROID_QUICK_SETTINGS$', re.IGNORECASE),  # ANDROID_QUICK_SETTINGS
            CommandType.ANDROID_SCREENSHOT: re.compile(r'^ANDROID_SCREENSHOT$', re.IGNORECASE),  # ANDROID_SCREENSHOT
            CommandType.ANDROID_VOLUME_UP: re.compile(r'^ANDROID_VOLUME_UP$', re.IGNORECASE),  # ANDROID_VOLUME_UP
            CommandType.ANDROID_VOLUME_DOWN: re.compile(r'^ANDROID_VOLUME_DOWN$', re.IGNORECASE),  # ANDROID_VOLUME_DOWN
            CommandType.ANDROID_MUTE: re.compile(r'^ANDROID_MUTE$', re.IGNORECASE),  # ANDROID_MUTE
            CommandType.ANDROID_POWER: re.compile(r'^ANDROID_POWER$', re.IGNORECASE),  # ANDROID_POWER
            CommandType.ANDROID_OPEN_APP: re.compile(r'^ANDROID_OPEN_APP\s+(.+)$', re.IGNORECASE),  # ANDROID_OPEN_APP app_name
            CommandType.ANDROID_CLOSE_APP: re.compile(r'^ANDROID_CLOSE_APP$', re.IGNORECASE),  # ANDROID_CLOSE_APP
            CommandType.ANDROID_CLEAR_RECENTS: re.compile(r'^ANDROID_CLEAR_RECENTS$', re.IGNORECASE),  # ANDROID_CLEAR_RECENTS
            CommandType.ANDROID_GOOGLE_ASSISTANT: re.compile(r'^ANDROID_GOOGLE_ASSISTANT$', re.IGNORECASE),  # ANDROID_GOOGLE_ASSISTANT
            CommandType.ANDROID_SPLIT_SCREEN: re.compile(r'^ANDROID_SPLIT_SCREEN$', re.IGNORECASE),  # ANDROID_SPLIT_SCREEN
            CommandType.ANDROID_PIP_MODE: re.compile(r'^ANDROID_PIP_MODE$', re.IGNORECASE),  # ANDROID_PIP_MODE
            CommandType.ANDROID_ACCESSIBILITY: re.compile(r'^ANDROID_ACCESSIBILITY$', re.IGNORECASE),  # ANDROID_ACCESSIBILITY
            CommandType.ANDROID_DEVELOPER_OPTIONS: re.compile(r'^ANDROID_DEVELOPER_OPTIONS$', re.IGNORECASE),  # ANDROID_DEVELOPER_OPTIONS
            
            # Comments
            CommandType.COMMENT: re.compile(r'^#(.*)$', re.IGNORECASE),
            CommandType.REM: re.compile(r'^REM(?:\s+(.+))?$', re.IGNORECASE),  # REM with optional text
        }
    
    def parse_file(self, file_path: str) -> HappyFrogScript:
        """
        Parse a Happy Frog Script file and return a structured representation.
        
        Args:
            file_path: Path to the .txt file containing Happy Frog Script
            
        Returns:
            HappyFrogScript object containing parsed commands
            
        Raises:
            HappyFrogScriptError: If parsing fails
            FileNotFoundError: If the file doesn't exist
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return self.parse_string(content, file_path)
        except FileNotFoundError:
            raise HappyFrogScriptError(f"File not found: {file_path}")
        except Exception as e:
            raise HappyFrogScriptError(f"Error reading file {file_path}: {str(e)}")
    
    def parse_string(self, content: str, source_name: str = "<string>") -> HappyFrogScript:
        """
        Parse Happy Frog Script content from a string.
        
        Args:
            content: String containing Happy Frog Script commands
            source_name: Name of the source (for error reporting)
            
        Returns:
            HappyFrogScript object containing parsed commands
        """
        commands = []
        lines = content.split('\n')
        
        for line_number, line in enumerate(lines, 1):
            # Skip empty lines
            if not line.strip():
                continue
                
            try:
                command = self._parse_line(line.strip(), line_number)
                if command:
                    commands.append(command)
            except HappyFrogScriptError as e:
                # Add context to the error
                raise HappyFrogScriptError(
                    f"Error in {source_name}, line {line_number}: {str(e)}"
                )
        
        metadata = {
            'source': source_name,
            'total_commands': len(commands),
            'total_lines': len(lines)
        }
        
        return HappyFrogScript(commands=commands, metadata=metadata)
    
    def _parse_line(self, line: str, line_number: int) -> Optional[HappyFrogCommand]:
        """
        Parse a single line of Happy Frog Script.
        
        Args:
            line: The line to parse
            line_number: Line number for error reporting
            
        Returns:
            HappyFrogCommand object or None if line should be ignored
            
        Raises:
            HappyFrogScriptError: If the line cannot be parsed
        """
        # Try to match each command pattern
        for command_type, pattern in self.command_patterns.items():
            match = pattern.match(line)
            if match:
                # Special handling for MODIFIER_COMBO
                if command_type == CommandType.MODIFIER_COMBO:
                    # Split the line into parts (e.g., MOD r -> [MOD, r])
                    parts = line.strip().split()
                    return HappyFrogCommand(
                        command_type=CommandType.MODIFIER_COMBO,
                        line_number=line_number,
                        raw_text=line,
                        parameters=parts
                    )
                return self._create_command(command_type, line, line_number, match)
        
        # If no pattern matches, it's an unknown command
        raise HappyFrogScriptError(f"Unknown command: {line}")
    
    def _create_command(self, command_type: CommandType, raw_text: str, 
                       line_number: int, match) -> HappyFrogCommand:
        """
        Create a HappyFrogCommand object from a regex match.
        
        Args:
            command_type: Type of command
            raw_text: Original text of the command
            line_number: Line number
            match: Regex match object
            
        Returns:
            HappyFrogCommand object
        """
        parameters = []
        
        # Extract parameters based on command type
        if command_type == CommandType.DELAY:
            # DELAY command has a parameter (validation happens in encoder)
            parameters = [match.group(1)]
                
        elif command_type in [CommandType.STRING, CommandType.REM]:
            # STRING and REM commands capture the rest of the line
            parameters = [match.group(1)] if match.group(1) else ['']
            
        elif command_type == CommandType.COMMENT:
            # COMMENT command captures everything after #
            parameters = [match.group(1)]
            
        # Advanced Ducky Script features
        elif command_type == CommandType.REPEAT:
            # REPEAT command has a numeric parameter
            parameters = [match.group(1)]
        elif command_type == CommandType.DEFAULT_DELAY:
            # DEFAULT_DELAY or DEFAULTDELAY command has a numeric parameter in group(2)
            parameters = [match.group(2)]
            
        # Conditional logic (Happy Frog exclusive)
        elif command_type in [CommandType.IF, CommandType.WHILE]:
            # IF and WHILE commands capture the condition
            parameters = [match.group(1)]
            
        elif command_type in [CommandType.ELSE, CommandType.ENDIF, CommandType.ENDWHILE]:
            # These commands have no parameters
            parameters = []
            
        # Happy Frog exclusive features
        elif command_type == CommandType.RANDOM_DELAY:
            # RANDOM_DELAY has two numeric parameters (min, max)
            parameters = [match.group(1), match.group(2)]
            
        elif command_type in [CommandType.LOG, CommandType.VALIDATE]:
            # LOG and VALIDATE commands capture the message/condition
            parameters = [match.group(1)]
            
        elif command_type == CommandType.SAFE_MODE:
            # SAFE_MODE has ON/OFF parameter
            parameters = [match.group(1)]
            
        # BadUSB compatibility commands
        elif command_type == CommandType.ATTACKMODE:
            # ATTACKMODE command captures the configuration
            parameters = [match.group(1)]
            
        # EvilCrow-Cable specialty commands
        elif command_type == CommandType.RELEASE:
            # RELEASE command has no parameters
            parameters = []
            
        elif command_type == CommandType.WIFI_SEND:
            # WIFI_SEND command captures the data to send
            parameters = [match.group(1)]
            
        elif command_type == CommandType.WIFI_CONNECT:
            # WIFI_CONNECT command captures SSID and password
            parameters = [match.group(1), match.group(2)]
            
        elif command_type in [CommandType.SHELLWIN, CommandType.SHELLNIX, CommandType.SHELLMAC]:
            # Shell commands capture the IP address
            parameters = [match.group(1)]
            
        # Android-specific commands
        elif command_type == CommandType.ANDROID_OPEN_APP:
            # ANDROID_OPEN_APP command captures the app name
            parameters = [match.group(1)]
            
        elif command_type in [CommandType.ANDROID_HOME, CommandType.ANDROID_BACK, CommandType.ANDROID_MENU,
                             CommandType.ANDROID_APP_SWITCH, CommandType.ANDROID_NOTIFICATIONS,
                             CommandType.ANDROID_QUICK_SETTINGS, CommandType.ANDROID_SCREENSHOT,
                             CommandType.ANDROID_VOLUME_UP, CommandType.ANDROID_VOLUME_DOWN,
                             CommandType.ANDROID_MUTE, CommandType.ANDROID_POWER,
                             CommandType.ANDROID_CLOSE_APP, CommandType.ANDROID_CLEAR_RECENTS,
                             CommandType.ANDROID_GOOGLE_ASSISTANT, CommandType.ANDROID_SPLIT_SCREEN,
                             CommandType.ANDROID_PIP_MODE, CommandType.ANDROID_ACCESSIBILITY,
                             CommandType.ANDROID_DEVELOPER_OPTIONS]:
            # Android commands with no parameters
            parameters = []
            
        # For all other commands, no parameters are extracted
        
        return HappyFrogCommand(
            command_type=command_type,
            line_number=line_number,
            raw_text=raw_text,
            parameters=parameters
        )
    
    def validate_script(self, script: HappyFrogScript) -> List[str]:
        """
        Validate a parsed script for common issues.
        
        Args:
            script: Parsed HappyFrogScript object
            
        Returns:
            List of warning messages (empty if no issues)
        """
        warnings = []
        
        # Check for common issues
        if not script.commands:
            warnings.append("Script contains no commands")
            
        # Check for very long delays that might indicate errors
        for cmd in script.commands:
            if cmd.command_type == CommandType.DELAY:
                try:
                    delay_ms = int(cmd.parameters[0])
                    if delay_ms > 60000:  # More than 1 minute
                        warnings.append(
                            f"Line {cmd.line_number}: Very long delay ({delay_ms}ms) - "
                            "this might be an error"
                        )
                except (ValueError, IndexError):
                    pass
        
        return warnings 