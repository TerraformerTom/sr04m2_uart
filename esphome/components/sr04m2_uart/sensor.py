#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace sr04m2_uart {

class SR04M2UARTSensor : public sensor::Sensor, public Component, public uart::UARTDevice {
 public:
  SR04M2UARTSensor(uart::UARTComponent *parent) : uart::UARTDevice(parent) {}

  void loop() override {
    while (this->available()) {
      if (this->read() == 0xFF && this->available() >= 3) {
        uint8_t high = this->read();
        uint8_t low  = this->read();
        uint8_t sum  = this->read();
        if (sum == ((0xFF + high + low) & 0xFF)) {
          float dist_cm = ((high << 8) | low) / 10.0f;
          publish_state(dist_cm);
        }
      }
    }
  }
};

}  // namespace sr04m2_uart
}  // namespace esphome
