import socket
import psutil
import subprocess

#Determine Total CPU Utilization
cpu_utilization = psutil.cpu_percent(5)

#Determine if syslog is running.
service = "syslog"
p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
(output, err) = p.communicate()

if cpu_utilization < 90 and output == b'active\n':
    status = "up\n"
elif output == b'inactive\n':
    status = "down\n"
elif cpu_utilization > 90 and output == b'active\n':
    status = "50\n"

# specify Host and Port
host = ''
port = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(10)
while True:
    c, addr = s.accept()
    while True:
        c.send(status.encode())
        c.close()
        break
