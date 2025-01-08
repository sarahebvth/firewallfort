# FirewallFort

FirewallFort is a Python-based tool designed to bolster Windows Firewall settings and controls, providing enhanced network protection against intrusions. It configures the firewall to block all inbound network traffic while allowing outbound traffic, ensuring a secure environment.

## Features

- Enables Windows Firewall for all network profiles.
- Blocks all inbound network traffic to prevent unauthorized access.
- Allows outbound network traffic to ensure normal operation of applications.

## Requirements

- Python 3.x
- Administrative privileges on Windows

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/FirewallFort.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd FirewallFort
   ```

## Usage

1. Open a terminal or command prompt with administrative privileges.
2. Run the script:
   ```bash
   python firewallfort.py
   ```

## Logging

FirewallFort logs its activity to a file named `firewallfort.log` in the same directory as the script. This log file records successful operations and any errors encountered during execution.

## Disclaimer

This tool modifies Windows Firewall settings and should be used with caution. Ensure you have proper authorization and understand the implications of these changes in your network environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.