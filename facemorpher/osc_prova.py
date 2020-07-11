

from docopt import docopt;
import shutil;
import os;
import time
import random
from pythonosc import udp_client
ip = "127.0.0.1"
port = 5005
i=0
while (True):
    time.sleep(0.1)
    if (i < 500):
        i += 1
        client = udp_client.SimpleUDPClient(ip, port)
        client.send_message("/filter", 155*random.random())
    else:
        break;

