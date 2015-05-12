# pi-jockey
Networking solutions for media control with Raspberry Pi.
---
Install pip, flask and python script, etc. 
---
- Remake this process for each Raspberry - media station  

* At the command prompt (terminal). 

part 1: Prepare to set ip adress from router config

- $ sudo nano /etc/hosts

- change 127.0.1.1 		raspberrypi
- to 127.0.1.1 			pi-n

do. exit and save

* $ sudo nano /etc/hostname

- raspberrypi
- to pi-n

* set up dhcp

$ nano /etc/network/interfaces
To setup eth0 to dhcp, enter:

auto eth0
iface eth0 inet dhcp

* What is your Mac adress. Enter.
- $ ifconfig

* Log on to the wireless network 192.168.0.1 

* Configure your router to force ip adresses to Mac Adresses of each Raspberry (media station) under the Lan tab. 

* Install pip file. Enter:

$ sudo apt-get install python-pip

* Install Flask. Enter:

$ sudo pip install Flask

* Clone Repo and cd into directory. Enter:

$ git clone https://github.com/palletorsson/pi-jockey.git

$ cd pi-jocky

* Supervisor for securing start and restart of script. Enter:

$ sudo apt-get install supervisor 
$ sudo nano /etc/supervisor/conf.d/flask_project.conf

* Add these lines. Enter or Copy and Paste:
 
[program:flask]
command = python media-server.py

directory = /home/pi/pi-jockey/

user = pi

* Save. Hit:
- Ctrl X 
- Y 

* Add media and configure the media-server. Do: 

* Add video to the video directory in the pi-jocky directory

* Configure the script media-server.py matching the video name

* Add ip to the hosts_list for each Raspberry media-server.py script.

* Open the Raspberry Pi /boot/config.txt and setting hdmi_drive=2

* Connect all Raspberry (media station) to you router. 

* Form the control computer

* Restart the each media station  

* On each media-server waiting for requests: 


On the control server start the server script

* Clone Repo and cd into directory. Enter:

$ git clone https://github.com/palletorsson/pi-jockey.git

$ cd pi-jocky

$ python controller.py (I will soon add supervisor)

