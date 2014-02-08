RESTduino
=========

RESTful interface to pyduino library

Functionality implemented
-------------------------

The functionalities of pyduino that are currently exposed via this API are:

- digital_read
- digital_write
- analog_read
- analog_write

Usage
-----

In order to use the library, you will need to install the python3 requirements described in ``requirements.txt`` and follow the pyduino installation instructions (incluiding loading the arduino sketch (``pyduino_sketch.ino``) in the board).

Then, run the server with:

    python restduino.py

and you will have a rest interface at port 5000.

For example, you can light up the built-in LED at pin 13 with curl:

    curl http://localhost:5000/digital/13 -d "value=1" -X PUT 
