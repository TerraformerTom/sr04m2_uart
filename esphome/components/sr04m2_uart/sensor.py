import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import UNIT_CENTIMETER, ICON_WATER, DEVICE_CLASS_DISTANCE, STATE_CLASS_MEASUREMENT

sr04m2_uart_ns = cg.esphome_ns.namespace('sr04m2_uart')
SR04M2UARTSensor = sr04m2_uart_ns.class_('SR04M2UARTSensor', sensor.Sensor, cg.PollingComponent, uart.UARTDevice)

CONFIG_SCHEMA = sensor.sensor_schema(
    unit_of_measurement=UNIT_CENTIMETER,
    icon=ICON_WATER,
    accuracy_decimals=1,
    device_class=DEVICE_CLASS_DISTANCE,
    state_class=STATE_CLASS_MEASUREMENT,
).extend({
    cv.GenerateID(): cv.declare_id(SR04M2UARTSensor),
    cv.GenerateID('uart_id'): cv.use_id(uart.UARTComponent),
    cv.Optional("update_interval", default="5s"): cv.update_interval
}).extend(cv.polling_component_schema("5s"))

async def to_code(config):
    var = cg.new_Pvariable(config[cv.ID], config[cv.CONF_UPDATE_INTERVAL])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    await uart.register_uart_device(var, config)
