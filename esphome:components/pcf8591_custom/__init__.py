import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

# Definieer de namespace
tda8444_custom_ns = cg.esphome_ns.namespace('tda8444_custom')
TDA8444 = tda8444_custom_ns.class_('TDA8444', cg.Component)

# Dit is wat 'tda8444_custom:' in YAML mogelijk maakt
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TDA8444),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
