"""
Pi-jockey settings for pi-jockey project.
For more information on this project, see
https://github.com/palletorsson/pi-jockey
"""

import os

# Videos

video_timing = {
    'videos': [
    {
        'file': 'big_buck_bunny_720_stereo.mp4',
        'length': '10',
        'start_at': '60',
        'screen': '1'
    }, 
    {
        'file': 'AR_CHINACITY_2_512kb.mp4', 
        'length': '7',
        'start_at': '0',
        'screen': '1'     
    }]
}

# Sound

Sound = {
    'Sound_1': {
        'name': 'rulz_no_rules',
        'file': 'test.mp3',
        'lenght': '340',
    }
}

# paths of project 
PROJECT_ROOT        = os.path.abspath(os.path.join(os.path.dirname(__file__)))
VIDEO_ROOT          = os.path.join(PROJECT_ROOT, 'video')
SOUND_ROOT          = os.path.join(PROJECT_ROOT, 'sound')

DEFAULT_VIDEO 		= 'AR_TURNMANGA_512kb.mp4'
DEFAULT_VIDEO_TRANS = 'black.mp4'


# ip2mac

ip = {
    'ip_1': {
        'ip': '192.168.0.110',
        'mac': '00:99:77:44:22:11',
    }
}

