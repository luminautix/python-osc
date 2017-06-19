""" OSC client for ETC EOS Family Lighting Control 

This code works only after special changes to the original python-osc library
"""

from pythonosc import osc_message_builder
from pythonosc import udp_client

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")      
  parser.add_argument("--port", type=int, default=5005, help="The port the OSC server is listening on")   
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)
  
  client.send_message("eos/key/clear_cmdline", "" )
  client.send_message("eos/key/go_to_cue", "" )
  client.send_message("eos/key/8", "" )
  client.send_message("eos/key/time", "" )
  client.send_message("eos/key/0", "" )
  client.send_message("eos/key/enter", "" )
