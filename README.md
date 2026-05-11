# Velleman-K8000-esp8266
The Velleman K8000 Fully controlled with an ESP 8266 and controllable via website
I made a chasing light as a demo.
External components must be created in the ESP home folder.

Preparation & Structure
Instead of a separate .h file, you now use a folder structure in your ESPHome configuration folder (e.g. /config/esphome/my_components/).
Folder name: Name the folder after your component (e.g. my_sensor).
Files: A basic component requires at least:
__init__.py: Defines the configuration validation in Python
.sensor.py (or binary_sensor.py, etc.): Associates the YAML settings with the C++ code
.my_sensor.h & my_sensor.cpp: The actual logic running on the ESP.

