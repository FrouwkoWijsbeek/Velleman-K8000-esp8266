import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, number
from esphome.const import CONF_ID, STATE_CLASS_MEASUREMENT

pcf8591_custom_ns = cg.esphome_ns.namespace('pcf8591_custom')
CustomPCF8591 = pcf8591_custom_ns.class_('CustomPCF8591', cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CustomPCF8591),
    cv.Optional("ain0"): sensor.sensor_schema(state_class=STATE_CLASS_MEASUREMENT, accuracy_decimals=2),
    cv.Optional("ain1"): sensor.sensor_schema(state_class=STATE_CLASS_MEASUREMENT, accuracy_decimals=2),
    cv.Optional("ain2"): sensor.sensor_schema(state_class=STATE_CLASS_MEASUREMENT, accuracy_decimals=2),
    cv.Optional("ain3"): sensor.sensor_schema(state_class=STATE_CLASS_MEASUREMENT, accuracy_decimals=2),
}).extend(cv.polling_component_schema('1s'))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if "ain0" in config:
        sens = await sensor.new_sensor(config["ain0"])
        cg.add(var.set_ain0_sensor(sens))
    if "ain1" in config:
        sens = await sensor.new_sensor(config["ain1"])
        cg.add(var.set_ain1_sensor(sens))
    if "ain2" in config:
        sens = await sensor.new_sensor(config["ain2"])
        cg.add(var.set_ain2_sensor(sens))
    if "ain3" in config:
        sens = await sensor.new_sensor(config["ain3"])
        cg.add(var.set_ain3_sensor(sens))


