import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID

# Definieer de namespace
tda8444_ns = cg.esphome_ns.namespace("tda8444")
TDA8444 = tda8444_ns.class_("TDA8444", cg.Component, i2c.I2CDevice)

# De crux: gebruik i2c.i2c_device_schema(default_address) 
# en NIET cv.i2c_device_schema
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TDA8444),
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x21))

async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    await cg.register_component(var, config)
    # Gebruik de i2c register functie
    await i2c.register_i2c_device(var, config)

