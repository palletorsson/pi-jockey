import urllib2
from threading import Thread
import time 
import settings
import json 

# list the ip:s
hosts_list =  ["0.0.0.0:5000"] #,"192.168.0.101:5000","192.168.0.102:5000"]
host = '127.0.0.1:5000'
startup_time = 2
time.sleep(startup_time) # wait for other ip:s to start

videos = settings.video_timing['videos'] 

def open_url(url):
    response = urllib2.urlopen(url)   

time.sleep(3)

for video in videos:   
    

    url = "http://" + host +"/video/go/" + video['file'] + "/" + video['start_at'] + "/" + video['length']
    print url

    Thread(target=open_url, args=[url]).start()
    
    print "requested video: " + video['file']
    #video_nr = video_nr + 1
    time.sleep(float(video['length']) -2.0)

