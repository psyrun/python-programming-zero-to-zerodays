import subprocess
print("Turn on super user mode and run python3")
interface = subprocess.call("ifconfig",shell="True")
print("+[] Changing the mac address for eth0 \n Enter ethernet device")
device_name=input("device_name >")
print("Enter new MAC")
new_mac=input("new_mac >")
subprocess.call("ifconfig " + device_name +" down ",shell="True")
subprocess.call("ifconfig " + device_name + " hw ether " + new_mac,shell="True")
subprocess.call("ifconfig " + device_name +" up ",shell="True")
print("completed like a samurai")
