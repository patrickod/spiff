Sensors
-------

Spiff is intended to be the central brain of a hackerspace. As such, it
includes functionality for tracking various sensors in the space.

There are five basic types of sensors:

-  number
-  string
-  binary
-  json
-  temp
-  boolean

The type of sensor is just a hint to tell API users how to display the
data if the exact purpose of the sensor is unknown. For example, the
spiff web UI will show a history graph for number sensors. The sensor
types adhere to the SpaceAPI standard: http://hackerspaces.nl/spaceapi/

To update a sensor, send a POST request to the sensor's page (i.e.
/sensors/1) with a single 'data' parameter containing the new sensor
data:

$ curl --data "data={'test': true}" http://example.com/sensors/1

The data can be anything: an image, a number, a basic string that says
"Hello!", more strutured JSON data, or whatever else you want to put in
there. Spiff doesn't care (except for `Boolean Sensors`_, it just stores the data until someone else
wants it.

Boolean Sensors
~~~~~~~~~~~~~~~

Spiff's REST API translates certain values into native values for requested
serialization formats, and for the :ref:`Open Sensor`. 

Accepted values that mean false:

- The string "false" (case-insensitive)
- The string "0"
- An empty string

Anything else is interpreted as true.

Pamela
~~~~~~

Pamela is described as a "very cool way to visualize any kind of data".
You can find it at http://www.hackerspace.be/Pamela

Spiff is totally 100% compatible with Pamela's basic API.

To use pamela's ARP scanner with Spiff:

::

    $ ./pamela/scanner/pamela-scanner.sh -i "eth0" -o \
        "http://example.com/sensors/1" -t mac.csv -d \
        "/var/lib/dhcpd/dhcpd.leases"

Please see Pamela's documentation for more details.

Sensor Actions
~~~~~~~~~~~~~~

Spiff can do stuff when sensors are updated. There are 4 kinds of actions that
can be added via the Django admin interface:

- http: Sends a HTTP GET request to the given url
- exec: Runs a command via subprocess.call_
- python: Executes some python code. A spiff.sensors.models.Sensor object is available in the 'sensor' variable.
- script: Writes a blob of text to a temporary file, performs chmod +x, and runs it.

.. _subprocess.call: http://docs.python.org/2/library/subprocess.html#subprocess.call

.. warning::

   Be extremely careful with the exec, python, and script actions! The commands
   are ran by the python process, which also means don't run spiff as root ever!
   Scary things can happen! Don't forget that your members trust you with the
   information you keep in spiff!

.. _`subprocess.call`: 
