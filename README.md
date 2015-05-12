# pi-jockey
Networking solutions for media control with Raspberry Pi.
---
Install pip, flask and python script, etc. 
---

( Remake this process for each Raspberry - media station. Start the command prompt (terminal))



1: Prepare to set ip adress from router config

Enter:
$ sudo apt-get update

1.1 Change your host name.

Enter:
$ sudo nano /etc/hosts

change: 127.0.1.1 		raspberrypi
to: 127.0.1.1 			pi-n

(here n is a number)
Exit and save

Enter:
* $ sudo nano /etc/hostname

change: raspberrypi
to: pi-n

(here n is a number)
Exit and save

1.2 Set up dhcp

$ nano /etc/network/interfaces
To setup eth0 to dhcp, enter:

auto eth0
iface eth0 inet dhcp

Exit and save

2. Configure your router (from another computer logon to the wireless network)

* What is your Mac adress. Enter.

$ ifconfig

(Note your Mac adress) 

* Log on to the wireless network 192.168.0.1 

* Configure your router to force ip adresses to Mac Adresses of each Raspberry (media station) under the Lan tab. 

3. Install pip file. Enter:

$ sudo apt-get install python-pip

4. Install Flask. Enter:

$ sudo pip install Flask

5. Clone Repo and cd into directory. Enter:

$ git clone https://github.com/palletorsson/pi-jockey.git

6. Supervisor for securing start and restart of script. Enter:

$ sudo apt-get install supervisor 
$ sudo nano /etc/supervisor/conf.d/flask_project.conf

Add these lines. Enter or Copy and Paste:
 
[program:flask]
command = python media-server.py
directory = /home/pi/pi-jockey/
user = pi

Exit and save

7. activate Hdmi sound
* $ nano /boot/config.txt 
set 
hdmi_drive=2
 

8. Add Media
* Add video to the video directory in the pi-jocky directory.
* Add sound to the sound directory in the pi-jocky directory.

9. Edit the settings

* Configure setting.py matching the video name.

10 Add ip to the hosts_list for each Raspberry media-server.py script.

11. Restart and test the pi



* Connect all Raspberry (media station) to you router. 

* Form the control computer

* Restart the each media station  

* On each media-server waiting for requests: 


On the control server start the server script

* Clone Repo and cd into directory. Enter:

$ git clone https://github.com/palletorsson/pi-jockey.git

$ cd pi-jocky

$ python controller.py (I will soon add supervisor)

