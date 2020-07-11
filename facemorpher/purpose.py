"""
::

  Face averager

  Usage: purpose.py --principale=<images_folder> --secondario=<images_folder> --A=<images_folder> --B=<images_folder> --C=<images_folder> --destinazione=<images_folder>


  Options:
    -h, --help             Show this screen.
    --principale=<folder>  Folder to images (.jpg, .jpeg, .png) #direttorio esattamente tre immagini di cui fare il morphing
    --secondario=<folder>  Folder to images (.jpg, .jpeg, .png) #direttorio che dev'essere vuoto
    --A=<folder>      Folder to images (.jpg, .jpeg, .png) #direttorio che dev'essere vuoto
    --B=<folder>      Folder to images (.jpg, .jpeg, .png) #direttorio che dev'essere vuoto
    --C=<folder>      Folder to images (.jpg, .jpeg, .png) #direttorio che dev'essere vuoto
    --destinazione=<folder>      Folder to images (.jpg, .jpeg, .png) #file destinazione del video di morphing


"""
import os
import sys


sys.path.append('/Users/Manuk/Downloads/face_morpher-dlib')

from facemorpher import averager
from facemorpher import morpher

from docopt import docopt
import shutil
import time
import random
from pythonosc import udp_client

from facemorpher.averager import list_imgpaths


def main():

    questo = os.getcwd();

    args = docopt(__doc__, version='io')
    principale = args['--principale'];   #direttorio contenente le immagini
    secondario = args['--secondario'];   #direttroio :D:Dlol che dev'essere vuoto
    direttorioA = args['--A'];   #direttorio che dev'essere vuoto
    direttorioB = args['--B'];   #direttorio che dev'essere vuoto
    direttorioC = args['--C'];   #direttorio che dev'essere vuoto
    destinazione = args['--destinazione'];   #file destinazione del video di morphing

    shutil.copy(principale + "/image1.jpg", direttorioA + "/image1.jpg")
    shutil.copy(principale + "/image1.jpg", direttorioB + "/image1.jpg")
    shutil.copy(principale + "/image2.jpg", direttorioA + "/image2.jpg")
    shutil.copy(principale + "/image2.jpg", direttorioC + "/image2.jpg")
    shutil.copy(principale + "/image3.jpg", direttorioB + "/image3.jpg")
    shutil.copy(principale + "/image3.jpg", direttorioC + "/image3.jpg")

    time.sleep(1)
    averager(list_imgpaths(direttorioA), out_filename='result1.png');
    averager(list_imgpaths(direttorioB), out_filename='result2.png');
    averager(list_imgpaths(direttorioC), out_filename='result3.png');
    averager(list_imgpaths(principale), out_filename='result4.png');

    shutil.move(questo+"/result1.png", secondario + "/result1.png")
    shutil.move(questo+"/result2.png", secondario + "/result2.png")
    shutil.move(questo+"/result3.png", secondario + "/result3.png")
    shutil.move(questo+"/result4.png", secondario + "/result4.png")

    morpher(list_imgpaths(secondario), out_video=destinazione)


    i=0
    client = udp_client.SimpleUDPClient("127.0.0.1", 5005)
    client.send_message("/filter", random.random())
    # while(True):
    #     time.sleep(0.1)
    #     if(i<5000):
    #         i+=1




if __name__ == "__main__":
  main()
