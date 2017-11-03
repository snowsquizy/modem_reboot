#!/usr/bin/env python3  
########################################################
# Confirm internet connection.  If internet is down reboot adsl modem
# Andrew Taylor @ 2016# Version 0.2
######################################################## 

########################################################
## Libraries Imports
# Regular expressions
import re
# Subprocesses
import subprocess
# SSH Connection
import paramiko

########################################################
## Variables
# ADSL Modem IP Address
modem = "192.168.1.1"
# Ping Target
host = "www.google.com.au"
# ADSL Modem User
user = "XXXX"
# ADSL Modem Password
m_password = "XXXX"
# Expression for packet loss 
noconnection = "100% packet loss"
# ADSL Modem Reboot Command
command_run = "reboot"

########################################################
# Confirm Packet connection to external website
ping = subprocess.Popen(
  ["ping", "-c", "2", host],    
  stdout = subprocess.PIPE,    
  stderr = subprocess.PIPE
  )
out, error = ping.communicate()

########################################################
# Connect to ADSL Modem and Reboot
if re.search(noconnection,str(out),flags=0):        
  # Create SSH Connection        
  client = paramiko.SSHClient()        
  # Load System Host Keys         
  client.load_system_host_keys()        
  # If connection is not in Host Keys add it        
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())        
  # Open SSH Connection to Modem        
  client.connect(modem,username=user,password=m_password)        
  # Run Reboot command        
  client.exec_command(command_run)        
  # Close SSH Connection        
  client.close()
