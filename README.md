# zteErrorGrapher

ZteErrorGrapher is a simple python script that displays a real time graph based on the FEC errors number displayed on the ZTE modem's status page. It could be usefull tool to help you diagnose your xDSL line problems.


# Supported Modems

The script has been tested with the ZXHN H267A V1.0 modem running 
firmware version V1.0.2_VDFT21 but it should work with other ZTE modems.

# Running the script

1) Clone the repository
2) cd zteErrorGrapher
3) python3 zteErrorGrapher.py modem_ip username password refresh_interval

## Requirments and Dependecies

 - Python3
 - Matplotlib
 - Selenium
