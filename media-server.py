
#!/usr/bin/env python2
from omxplayer import OMXPlayer
from flask import Flask
import subprocess
import time
import sys
import settings
from os import listdir
from os.path import isfile, join
from random import randint
from threading import Thread

import pygame

print settings.DEFAULT_VIDEO

print "Server started"

app = Flask(__name__)

global transclip
global videofileplaying

mypath = "video"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


@app.route("/video/start/rand/")
def randVideo(video_id=None):
    print "Incoming video request"
    try:
        pygame.init()
        pygame.display.init()
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        the_screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        the_screen.fill((0,0,0))
        pygame.display.set_caption("Video Player")
        time.sleep(1)
        pygame.display.update()
        pygame.quit()
    except:
       print "no blackscreen"

    try:
        return_code = transclip.poll()
        if return_code == None:
            transclip.stdin.write('q')
            print "Transition was playing, video file stopped"
    except:
        print "no transvideo playing"


    try:
        return_code = videofileplaying.poll()
        if return_code == None:
            videofileplaying.stdin.write('q')
            print "Video was playing, video file stopped"
    except:
        print "no video playing"

    try:
        randing = randint(0,len(onlyfiles)-1)
    except:
        randing = 1

    videopath = mypath+"/"+onlyfiles[randing]

    videofileplaying=subprocess.Popen(["omxplayer", "-b" ,"-o", "hdmi" , videopath], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    return "Video file played, lol"


@app.route("/video/start/<int:video_id>/")
def startVideo(video_id=None):
    print "Incoming video request"
    try:
        return_code = transclip.poll()
        if return_code == None:
            transclip.stdin.write('q')
            print "Transition was playing, video file stopped"
    except:
        print "no transvideo playing"

    try:
        return_code = videofileplaying.poll()
        if return_code == None:
            videofileplaying.stdin.write('q')
            print "Video was playing, video file stopped"
    except:
        print "no video playing"

    try:
        randing = randint(0,len(onlyfiles)-1)
    except:
        randing = 1

    videofileplaying=subprocess.Popen(["omxplayer", "-b" ,"-o", "hdmi" ,mypath+"/"+str(video_id)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    return "Video file played, lol"

@app.route("/video/stop/")
def stopVideo():


    return_string = "Test : Video stop"
    blackclip=subprocess.Popen(["omxplayer", "-b" ,"-o", "hdmi" ,"video/"+settings.DEFAULT_VIDEO_TRANS], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    print "Test : Stopping video"

    try:
       
        videofileplaying.stdin.write('q')
        return_string = return_string + " >>  Video stopped"
        print "Video stopped"
    except:
        print "hmm - no video to stop"
        return_string = return_string + " >>  No video found to be stopped"
    return return_string


@app.route("/video/go/<video_name>/<int:start>/<int:length>")
def playVideoGo(video_name, start=0, length=0):
    print "Incoming video request"
    videofile_path = "video/"+ video_name 
    # TODO check is file en with mp4 or mov
    print "video to play: " + videofile_path  
    video = OMXPlayer(videofile_path, pause=True)
   
    # set video clip duration
    if start > 0:
        video.set_position(start)

    # set video clip duration
    if length == 0:
        dur = video.duration()
        durint = int(dur)
        video.play()
        time.sleep(durint)  
    else:
        video.play()
        print length
        time.sleep(length)

    print("Stop playing")
    video.quit()
    return "Video file played, lol"



@app.route("/video/test/")
def testVideo(video_id=None):
    print "Incoming video request"
    vid1 = OMXPlayer(TEST_MEDIA_FILE_1, pause=True)
    print("Start playing")
    vid1.set_position(70)
    dur = vid1.duration()
    print dur
    vid1.play()
    sleep(2)
    print("Stop playing")
    vid1.pause()
    time.sleep(2)
    vid1.load(TEST_MEDIA_FILE_2)
    vid1.play()
    sleep(2)
    print("Exit")
    vid1.quit()


def startblackclip(full_length):
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.init()
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    the_screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    the_screen.fill((0,0,0))
    #myfont = pygame.font.SysFont('monospace', 64)
    #label = myfont.render('Video Player', 1, (255,255,0))
    #the_screen.blit(label, (200,300))
    pygame.display.update()
    pygame.display.set_caption('Video Player')
    pygame.display.update()
    time.sleep(full_length)
    pygame.quit()


if __name__ == "__main__":
    time.sleep(3)
    Thread(target=startblackclip, args=[30]).start()
    app.run(host="0.0.0.0")
  

