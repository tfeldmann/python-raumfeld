python-raumfeld
===============

A pythonic library for discovering and controlling Teufel Raumfeld devices.

Example Usage:

```python
import raumfeld

devices = raumfeld.discover()
speaker = device[0]

speaker.play()

speaker.mute = False
print(speaker.volume)

speaker.pause()
´´´
