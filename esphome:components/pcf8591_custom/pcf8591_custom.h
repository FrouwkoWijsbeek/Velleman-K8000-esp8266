#include "esphome.h"
#include <Wire.h>

namespace pcf8591_custom {

using namespace esphome;

class CustomPCF8591 : public PollingComponent {
 public:
  sensor::Sensor *ain0_sensor{nullptr};
  sensor::Sensor *ain1_sensor{nullptr};
  sensor::Sensor *ain2_sensor{nullptr};
  sensor::Sensor *ain3_sensor{nullptr};

  void set_ain0_sensor(sensor::Sensor *s) { ain0_sensor = s; }
  void set_ain1_sensor(sensor::Sensor *s) { ain1_sensor = s; }
  void set_ain2_sensor(sensor::Sensor *s) { ain2_sensor = s; }
  void set_ain3_sensor(sensor::Sensor *s) { ain3_sensor = s; }
  

  CustomPCF8591() : PollingComponent(1000) {}

  void setup() override {
    Wire.begin();
  }

  void update() override {
    Wire.beginTransmission(0x49);
    Wire.write(0x04); // Auto-increment mode
    Wire.endTransmission();

    Wire.requestFrom(0x49, 5);
    if (Wire.available()) {
      Wire.read(); // Dummy byte
      if (ain0_sensor) ain0_sensor->publish_state(Wire.read());
      if (ain1_sensor) ain1_sensor->publish_state(Wire.read());
      if (ain2_sensor) ain2_sensor->publish_state(Wire.read());
      if (ain3_sensor) ain3_sensor->publish_state(Wire.read());
    }
  }
};

} // namespace pcf8591_custom
