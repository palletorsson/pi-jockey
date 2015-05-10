# pi-jockey
Networking solutions for media control with Raspberry Pi.

Remake this process for each Raspberry - media station  

* Open the command prompt (terminal). 
* Install pip file. Enter:
$ sudo apt-get install python-pip

* Install Flask. Enter:
$ sudo pip install Flask


* Clone Repo and cd into directory. Enter:
$ git clone https://github.com/palletorsson/pi-jockey.git
$ cd pi-jocky

* Add media and configure the media-server. Do: 
* Add video to the video directory in the pi-jocky directory
* Configure the script media-server.py matching the video name
* Add ip to the hosts_list for each Raspberry media-server.py script.

* Open the Raspberry Pi /boot/config.txt and setting hdmi_drive=2

* Connect all Raspberry (media station) to you router. 

* Form the control computer

* Log on to the wireless network 192.168.0.1 
* Configure your router to force ip adresses to mac-adresses of each Raspberry (media station) 

* Restart the each media station  

* On each media-server waiting for requests: 
$ python media-server.py (I will soon add supervisor)


On the control server start the server script

* Clone Repo and cd into directory. Enter:
$ git clone https://github.com/palletorsson/pi-jockey.git
$ cd pi-jocky
$ python controller.py (I will soon add supervisor)

