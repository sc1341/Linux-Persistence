# Linux-Persistence
A Python script that automatically creates a similar systemd daemon to existing daemons which is intended to establish persistence on a machine.

# Example Usage

`sudo ./create_service.py "python3 -m http.server 8080" --description "Python HTTP Server" --self-delete`

`sudo ./create_service.py "python3 -m http.server 8080" --description "Python HTTP Server" --user ubuntu --group ubuntu --working-directory /home/ubuntu/webcontent/`

`sudo ./create_service.py "/opt/my_app/my_app" --description "My Custom App" --user appuser --group appuser --working-directory /opt/my_app/`

