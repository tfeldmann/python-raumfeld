Quickstart
==========

.. code:: python

    import raumfeld

    # discovery returns a list of RaumfeldDevices
    devices = raumfeld.discover(timeout=1, retries=1)
    if len(devices) > 0:
        speaker = devices[0]

        # now you can control your raumfeld speaker
        speaker.mute = True     # mute
        print(speaker.volume)   # print current volume
        speaker.volume = 50     # set volume

        speaker.pause()
        speaker.play()
    else:
        print('No devices found.')
