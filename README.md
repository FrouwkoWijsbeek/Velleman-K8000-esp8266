# Velleman-K8000-esp8266
ESP8266/ESP32 integration for the classic Velleman K8000 I/O board. Includes custom ESPHome components for the TDA8444 DAC and full support for PCF8574 digital I/O via I2C.

Preparation & Structure
Instead of a separate .h file, you now use a folder structure in your ESPHome configuration folder (e.g. /config/esphome/my_components/).
Folder name: Name the folder after your component (e.g. my_sensor).
Files: A basic component requires at least:
__init__.py: Defines the configuration validation in Python
.sensor.py (or binary_sensor.py, etc.): Associates the YAML settings with the C++ code
.my_sensor.h & my_sensor.cpp: The actual logic running on the ESP.

