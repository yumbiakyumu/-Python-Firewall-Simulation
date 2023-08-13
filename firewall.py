import random

def generate_random_ip():
    """Generate a random IP address."""
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    """Check if the IP address matches any firewall rule and return the action."""
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"  # Default action if no rule matches

def main():
    # Define the firewall rules (key: IP address, value: action)
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

    # Simulate network traffic
    for _ in range(12):  # Loop 12 times for simulation
        ip_address = generate_random_ip()  # Generate a random IP address
        action = check_firewall_rules(ip_address, firewall_rules)  # Check if IP matches any rule
        random_number = random.randint(0, 9999)  # Generate a random number
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()  # Execute the main function if the script is run as the main program
