# AlertMuse

Alert Muse utilizes the [Muse](http://www.choosemuse.com/) Headband's EEG data, parses it, and notifies the user through a vibration of the [Pebble](https://www.pebble.com/pebble-time-smartwatch-features) Time that they need to wake up. It does so by monitoring the alpha and theta waves of the user, since those are the primary indicators for the start of the NREM-1 phase of the sleep cycle. This can have many applications, specifically geared towards drowsy drivers, but can be used when studying or at work when trying to stay awake.

Made by:
  + [Dor Rondel](https://github.com/Dor-Ron)
  + [Sherry Ko](https://github.com/Kotisheu)
  + [Daniel Zabari](https://github.com/Zabari)
  + [Renzhentaxi Baerde](https://github.com/renzhentaxi)

For HackCooper 2016


## Requirements
---

  + Muse Headband

  + Pebble Watch

  + MUSEIO

## Instructions
---

Install Dependencies through:

1) Connect devices to computer through bluetooth

In your terminal type:

2) `pip3 install -r requirements.txt`

3) `muse-io --device <Muse-YourID> --osc osc.udp://localhost:5000`

4) `python3 server.py`

5) `python3 parse_eeg.py`
