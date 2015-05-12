from flask import Flask
import subprocess
import time
import settings

print settings.DEFAULT_VIDEO

print "Server started"

app = Flask(__name__)


@app.route("/video/start/<int:video_id>/")
def startVideo(video_id=None):
    print "Incoming video request"
    global videofileplaying

    try:
        return_code = videofileplaying.poll()
        if return_code == None:
            videofileplaying.stdin.write('q')
            print "Video was playing, video file stopped"
    except:
        print "no video playing"

    videofileplaying=subprocess.Popen(["omxplayer", "-b" ,"-o", "hdmi" ,"video/"+settings.DEFAULT_VIDEO], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    return "Video file played, lol"

@app.route("/video/stop/")
def stopVideo():
    return_string = "Test : Video stop"
    blackclip=subprocess.Popen(["omxplayer", "-b" ,"-o", "hdmi" ,"video/"+settings.DEFAULT_VIDEO_TRAN], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
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

