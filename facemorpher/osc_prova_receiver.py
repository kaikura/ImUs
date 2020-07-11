import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server





if __name__ == "__main__":
  ip="127.0.0.1"
  port=5005

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/filter", print)


  server = osc_server.ThreadingOSCUDPServer(
      (ip, port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()