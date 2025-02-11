# Cursor Auto ID Modifier

This script automates the process of managing the Cursor IDE installation and configuration. It provides functionality to check, install, and configure Cursor with specific versions while handling the trial management process.

## Features

- 🔍 Automatic OS detection (Windows, macOS, Linux)
- 📦 Version checking and management
- 🗑️ Clean uninstallation of previous versions
- ⚙️ Automated installation of specific Cursor versions
- 🔄 Trial reset functionality
- 🛠️ Automatic configuration file management

## Prerequisites

- Python 3.6 or higher
- Operating System: Windows 10/11, macOS, or Linux
- Administrative privileges (for installation/uninstallation)

## Installation

1. Clone or download this repository
2. Ensure Python is installed on your system
3. No additional Python packages are required as the script uses standard library modules

## Usage

Run the script using Python:

```bash
python AutoIDModifier.py
```

The script will automatically:

1. Detect your operating system
2. Check if Cursor is installed and verify its version
3. Only uninstall if necessary (if version doesn't match or not installed)
4. Install the correct version if needed
5. Handle the trial management process
6. Configure the necessary files

## Process Steps

1. **OS Detection**: Automatically identifies your operating system
2. **Version Check**: Verifies if Cursor is installed and checks its version
3. **Smart Uninstallation**: Only uninstalls if the version doesn't match
4. **Installation**: Installs the correct version (v0.44.11)
5. **Account Setup**: Guides through temporary email account creation
6. **Configuration**: Modifies necessary system files
7. **Restart**: Automatically restarts Cursor with new configuration

## Troubleshooting

If you encounter any issues:

1. Ensure you have administrative privileges
2. Check if Cursor is completely closed before running the script
3. Make sure no other instances of Cursor are running
4. Verify that all paths are accessible to your user account

## Important Notes

- The script requires administrative privileges for installation/uninstallation
- Backup your Cursor settings before running if you have important configurations
- The script will automatically handle the cleanup of old files
- Internet connection is required for downloading and account creation

## Security

- The script only modifies Cursor-related files and settings
- No sensitive data is collected or transmitted
- All modifications are local to your system
- Temporary email services are used for account creation

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify your system meets all prerequisites
3. Ensure you're running the latest version of the script

## Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring they comply with all relevant terms of service and licensing agreements. 