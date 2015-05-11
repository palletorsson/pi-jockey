from flask import Flask
import subprocess
import time

print "Server started"
#videofileplaying = False
video_filename = "bigbuck.mp4"

app = Flask(__name__)


@app.route("/video/start/")
def startVideo():
    print "Incoming video request"
    global videofileplaying

    try:
        return_code = videofileplaying.poll()
        if return_code == None:
            videofileplaying.stdin.write('q')
            print "Video was playing, video file stopped"
    except:
        print "no video playing"

    videofileplaying=subprocess.Popen(["omxplayer", "-b" ,"-o", "hdmi" ,"video/"+video_filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    return "Video file played, lol"

@app.route("/video/stop/")
def stopVideo():
    return_string = "Test : Video stop"
    blackclip=subprocess.Popen(["omxplayer", "-b" ,"-o", "hdmi" ,"video/black.mp4"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    print "Test : Stopping video"
    try:
        videofileplaying.stdin.write('q')
        return_string = return_string + " >>  Video stopped"
        print "Video stopped"
    except:
        print "hmm - no video to stop"
        return_string = return_string + " >>  No video found to be stopped"
    return return_string

if __name__ == "__main__":
    app.run(host="0.0.0.0")

