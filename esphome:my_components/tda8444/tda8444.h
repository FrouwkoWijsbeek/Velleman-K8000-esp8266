#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/core/log.h"

namespace esphome {
namespace tda8444 {

// Voeg deze regel toe om de TAG te definiëren voor de logger
static const char *const TAG = "tda8444";

class TDA8444 : public Component, public i2c::I2CDevice {
 public:
  void setup() override {
    ESP_LOGCONFIG(TAG, "TDA8444 initialiseren op adres 0x%02X...", this->address_);
    
    for (uint8_t i = 0; i < 8; i++) {
      this->set_channel_value(i, 0);
    }
  }

  void set_channel_value(uint8_t channel, uint8_t value) {
    if (channel > 7) return;
    if (value > 63) value = 63;

    uint8_t instruction = channel & 0x07;
    
    if (!this->write_byte(instruction, value)) {
      ESP_LOGE(TAG, "Fout bij schrijven naar kanaal %d!", channel);
    } else {
      ESP_LOGD(TAG, "Kanaal %d ingesteld op: %d", channel, value);
    }
  }

  void dump_config() override {
    ESP_LOGCONFIG(TAG, "TDA8444 DAC:");
    LOG_I2C_DEVICE(this);
  }
};

}  // namespace tda8444
}  // namespace esphome
