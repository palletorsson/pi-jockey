import urllib2
import time 

# list the ip:s
hosts_list =  ["192.168.0.100:5000"] #,"192.168.0.101:5000","192.168.0.102:5000"]

# How long is the video?
video_length = 60 

# Loop until we stop the program
while True: 
    try:
        for host in hosts_list:      
            url = "http://" + host +"/video/start/"
            response = urllib2.urlopen(url)
        print "Video start - requested"

    except: 
        print "Request Error"

    time.sleep(video_length) # wait for length of the video in minuter

    try:
        for host in hosts_list: 
            url = "http://" + host +"/video/stop/"
            response = urllib2.urlopen(url)

        print "video stop requested"

    except: 
        print "Request Error"

    time.sleep(3) # wait for 3 second 


