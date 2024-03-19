"""Constants for localtuya integration."""

from homeassistant.const import EntityCategory, Platform

DOMAIN = "localtuya"

DATA_DISCOVERY = "discovery"

# Order on priority
SUPPORTED_PROTOCOL_VERSIONS = ["3.3", "3.1", "3.2", "3.4", "3.5"]


# Platforms in this list must support config flows
PLATFORMS = {
    "Alarm Control Panel": Platform.ALARM_CONTROL_PANEL,
    "Binary Sensor": Platform.BINARY_SENSOR,
    "Button": Platform.BUTTON,
    "Climate": Platform.CLIMATE,
    "Cover": Platform.COVER,
    "Fan": Platform.FAN,
    "Humidifier": Platform.HUMIDIFIER,
    "Light": Platform.LIGHT,
    "Number": Platform.NUMBER,
    "Remote": Platform.REMOTE,
    "Select": Platform.SELECT,
    "Sensor": Platform.SENSOR,
    "Siren": Platform.SIREN,
    "Switch": Platform.SWITCH,
    "Vacuum": Platform.VACUUM,
}

ATTR_CURRENT = "current"
ATTR_CURRENT_CONSUMPTION = "current_consumption"
ATTR_VOLTAGE = "voltage"
ATTR_UPDATED_AT = "updated_at"

# Tuya Devices
CONF_TUYA_IP = "ip"
CONF_TUYA_GWID = "gwId"
CONF_TUYA_VERSION = "version"

# config flow
CONF_LOCAL_KEY = "local_key"
CONF_ENABLE_DEBUG = "enable_debug"
CONF_PROTOCOL_VERSION = "protocol_version"
CONF_NODE_ID = "node_id"
CONF_GATEWAY_ID = "gateway_id"
CONF_DPS_STRINGS = "dps_strings"
CONF_MODEL = "model"
CONF_PRODUCT_KEY = "product_key"
CONF_PRODUCT_NAME = "product_name"
CONF_USER_ID = "user_id"
CONF_ENABLE_ADD_ENTITIES = "add_entities"


CONF_ADD_DEVICE = "add_device"
CONF_EDIT_DEVICE = "edit_device"
CONF_CONFIGURE_CLOUD = "configure_cloud"
CONF_NO_CLOUD = "no_cloud"
CONF_MANUAL_DPS = "manual_dps_strings"
CONF_DEFAULT_VALUE = "dps_default_value"
CONF_RESET_DPIDS = "reset_dpids"
CONF_PASSIVE_ENTITY = "is_passive_entity"
CONF_DEVICE_SLEEP_TIME = "device_sleep_time"

# ALARM
CONF_ALARM_SUPPORTED_STATES = "alarm_supported_states"

# Binary_sensor, Siren
CONF_STATE_ON = "state_on"

# light
CONF_BRIGHTNESS_LOWER = "brightness_lower"
CONF_BRIGHTNESS_UPPER = "brightness_upper"
CONF_COLOR = "color"
CONF_COLOR_MODE = "color_mode"
CONF_COLOR_TEMP_MIN_KELVIN = "color_temp_min_kelvin"
CONF_COLOR_TEMP_MAX_KELVIN = "color_temp_max_kelvin"
CONF_COLOR_TEMP_REVERSE = "color_temp_reverse"
CONF_MUSIC_MODE = "music_mode"
CONF_SCENE_VALUES = "scene_values"
CONF_SCENE_VALUES_FRIENDLY = "scene_values_friendly"

# switch
CONF_CURRENT = "current"
CONF_CURRENT_CONSUMPTION = "current_consumption"
CONF_VOLTAGE = "voltage"

# cover
CONF_COMMANDS_SET = "commands_set"
CONF_POSITIONING_MODE = "positioning_mode"
CONF_CURRENT_POSITION_DP = "current_position_dp"
CONF_SET_POSITION_DP = "set_position_dp"
CONF_POSITION_INVERTED = "position_inverted"
CONF_SPAN_TIME = "span_time"

# fan
CONF_FAN_SPEED_CONTROL = "fan_speed_control"
CONF_FAN_OSCILLATING_CONTROL = "fan_oscillating_control"
CONF_FAN_SPEED_MIN = "fan_speed_min"
CONF_FAN_SPEED_MAX = "fan_speed_max"
CONF_FAN_ORDERED_LIST = "fan_speed_ordered_list"
CONF_FAN_DIRECTION = "fan_direction"
CONF_FAN_DIRECTION_FWD = "fan_direction_forward"
CONF_FAN_DIRECTION_REV = "fan_direction_reverse"
CONF_FAN_DPS_TYPE = "fan_dps_type"

# sensor
CONF_SCALING = "scaling"
CONF_STATE_CLASS = "state_class"

# climate
CONF_TARGET_TEMPERATURE_DP = "target_temperature_dp"
CONF_CURRENT_TEMPERATURE_DP = "current_temperature_dp"
CONF_TEMPERATURE_STEP = "temperature_step"
CONF_MIN_TEMP = "min_temperature"
CONF_MAX_TEMP = "max_temperature"
CONF_PRECISION = "precision"
CONF_TARGET_PRECISION = "target_precision"
CONF_HVAC_MODE_DP = "hvac_mode_dp"
CONF_HVAC_MODE_SET = "hvac_mode_set"
CONF_PRESET_DP = "preset_dp"
CONF_PRESET_SET = "preset_set"
CONF_HEURISTIC_ACTION = "heuristic_action"
CONF_HVAC_ACTION_DP = "hvac_action_dp"
CONF_HVAC_ACTION_SET = "hvac_action_set"
CONF_HVAC_ADD_OFF = "hvac_add_off"
CONF_ECO_DP = "eco_dp"
CONF_ECO_VALUE = "eco_value"
CONF_FAN_SPEED_LIST = "fan_speed_list"

# vacuum
CONF_POWERGO_DP = "powergo_dp"
CONF_IDLE_STATUS_VALUE = "idle_status_value"
CONF_RETURNING_STATUS_VALUE = "returning_status_value"
CONF_DOCKED_STATUS_VALUE = "docked_status_value"
CONF_BATTERY_DP = "battery_dp"
CONF_MODE_DP = "mode_dp"
CONF_MODES = "modes"
CONF_FAN_SPEED_DP = "fan_speed_dp"
CONF_FAN_SPEEDS = "fan_speeds"
CONF_CLEAN_TIME_DP = "clean_time_dp"
CONF_CLEAN_AREA_DP = "clean_area_dp"
CONF_CLEAN_RECORD_DP = "clean_record_dp"
CONF_LOCATE_DP = "locate_dp"
CONF_FAULT_DP = "fault_dp"
CONF_PAUSED_STATE = "paused_state"
CONF_RETURN_MODE = "return_mode"
CONF_STOP_STATUS = "stop_status"
CONF_PAUSE_DP = "pause_dp"

# number
CONF_MIN_VALUE = "min_value"
CONF_MAX_VALUE = "max_value"
CONF_STEPSIZE = "step_size"

# select
CONF_OPTIONS = "select_options"
CONF_OPTIONS_FRIENDLY = "select_options_friendly"

# button
CONF_TRIGGER_TYPES = "trigger_types"

# Remote
CONF_RECEIVE_DP = "receive_dp"

# States
ATTR_STATE = "raw_state"
CONF_RESTORE_ON_RECONNECT = "restore_on_reconnect"

# Categories
ENTITY_CATEGORY = {
    "None": None,
    "Configuration": EntityCategory.CONFIG,
    "Diagnostic": EntityCategory.DIAGNOSTIC,
}

# Default Categories
DEFAULT_CATEGORIES = {
    "CONTROL": ["switch", "climate", "fan", "vacuum", "light"],
    "CONFIG": ["select", "number", "button"],
    "DIAGNOSTIC": ["sensor", "binary_sensor"],
}
