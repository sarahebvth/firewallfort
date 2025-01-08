import subprocess
import logging

# Configure logging
logging.basicConfig(filename='firewallfort.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FirewallFort:
    def __init__(self):
        self.check_admin_rights()

    def check_admin_rights(self):
        try:
            # Check if the script is running with admin rights
            subprocess.check_call('net session', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            logging.error("This script requires administrative privileges.")
            raise PermissionError("This script requires administrative privileges.")

    def enable_firewall(self):
        try:
            subprocess.check_call('netsh advfirewall set allprofiles state on', shell=True)
            logging.info("Firewall enabled for all profiles.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to enable firewall: {e}")

    def block_inbound_traffic(self):
        try:
            subprocess.check_call('netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound', shell=True)
            logging.info("Inbound traffic blocked for all profiles.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to block inbound traffic: {e}")

    def allow_outbound_traffic(self):
        try:
            subprocess.check_call('netsh advfirewall set allprofiles firewallpolicy allowoutbound', shell=True)
            logging.info("Outbound traffic allowed for all profiles.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to allow outbound traffic: {e}")

    def configure_firewall(self):
        self.enable_firewall()
        self.block_inbound_traffic()
        self.allow_outbound_traffic()

if __name__ == "__main__":
    firewall_fort = FirewallFort()
    firewall_fort.configure_firewall()
    logging.info("FirewallFort configuration complete.")