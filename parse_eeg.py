import argparse

from pythonosc import dispatcher, osc_server
from urllib import request, parse

URL = "http://104.131.44.27/?ch1={}&ch2={}&ch3={}&ch4={}"

def make_POST(data_dict, url):
    '''Make a post request with eeg data'''
    data = parse.urlencode(data_dict).encode()
    req  = request.Request(url, data=data) # this will make the method "POST"
    resp = request.urlopen(req)

def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    '''print eeg data'''
    print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)
    waves = {
        'channel1': ch1,
        'channel2': ch2,
        'channel3': ch3,
        'channel4': ch4
    }
    make_POST(waves, URL.format(ch1, ch2, ch3, ch4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/elements/alpha_absolute", eeg_handler, "EEG")  # get alpha waves only

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
