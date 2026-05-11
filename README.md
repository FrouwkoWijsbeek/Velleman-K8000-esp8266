# Velleman-K8000-esp8266
ESP8266/ESP32 integration for the classic Velleman K8000 I/O board. Includes custom ESPHome components for the TDA8444 DAC and full support for PCF8574 digital I/O via I2C.

Preparation & Structure
Instead of a separate .h file, you now use a folder structure in your ESPHome configuration folder (e.g. /config/esphome/my_components/).
Folder name: Name the folder after your component (e.g. my_sensor).
Files: A basic component requires at least:
__init__.py: Defines the configuration validation in Python
.sensor.py (or binary_sensor.py, etc.): Associates the YAML settings with the C++ code
.my_sensor.h & my_sensor.cpp: The actual logic running on the ESP.

# ESPHome Velleman K8000 Integration

Give your classic **Velleman K8000** board a second life! This project provides a modern bridge between the legendary K8000 I/O board and **Home Assistant** using an ESP8266 (or ESP32) and ESPHome.

## Features
- **TDA8444 DAC Support**: Custom C++ component to control all 8 analog outputs (6-bit resolution).
- **16 Digital I/O**: Full control over the two onboard PCF8574 chips for inputs and outputs.
- **Standalone Chaser Effect**: A high-performance 16-channel "Knight Rider" animation script running locally on the ESP.
- **Web Interface**: Built-in web server to control your board from any browser.

## Project Structure
To use this as an **External Component**, ensure your GitHub repository follows this structure:
- `components/tda8444/tda8444.h`
- `components/tda8444/__init__.py`

## Installation

Add this repository to your ESPHome YAML configuration:

```yaml
external_components:
  - source:
      type: git
      url: https://github.com
    components: [ tda8444 ]

i2c:
  sda: GPIO4
  scl: GPIO5
  scan: true

tda8444:
  id: dac_chip
  address: 0x21

# Example: Control Analog Output 1
number:
  - platform: template
    name: "K8000 Analog Out 1"
    min_value: 0
    max_value: 63
    step: 1
    set_action:
      then:
        - lambda: 'id(dac_chip).set_channel_value(0, (uint8_t)x);'
```

## Hardware Connection
The K8000 works on 5V logic. When using an ESP8266 or ESP32 (3.3V), it is highly recommended to use an **I2C Logic Level Shifter** to protect your pins and ensure stable communication.

## Credits
Original hardware by Velleman. ESPHome implementation developed for the community.
