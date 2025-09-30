"""Nautobot development configuration file."""

# pylint: disable=invalid-envvar-default
import os
import sys

from nautobot.core.settings import *  # noqa: F403  # pylint: disable=wildcard-import,unused-wildcard-import
from nautobot.core.settings_funcs import is_truthy, parse_redis_connection


#
# Debug
#

DEBUG = is_truthy(os.getenv("NAUTOBOT_DEBUG", False))

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"


#
# Security and Reverse Proxy Settings
#

# Required: List of allowed hostnames/IPs that can access Nautobot
ALLOWED_HOSTS = ['nautobot.arpa', '192.168.4.32', 'localhost']

# Handle SSL termination at Caddy reverse proxy level
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Trust origins for CSRF protection when using HTTPS
CSRF_TRUSTED_ORIGINS = ['https://nautobot.arpa']

# USE_X_FORWARDED_HOST is True by default in Nautobot - no need to set explicitly


#
# Logging
#

LOG_LEVEL = "DEBUG" if DEBUG else "INFO"


#
# Redis
#

# Redis Cacheops
CACHEOPS_REDIS = parse_redis_connection(redis_database=1)

#
# Celery settings are not defined here because they can be overloaded with
# environment variables. By default they use `CACHES["default"]["LOCATION"]`.
#

# Enable installed plugins. Add the name of each plugin to the list.
# PLUGINS = ["nautobot_example_plugin"]
PLUGINS = []

# Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
PLUGINS_CONFIG = {
    "nautobot_example_plugin": {},
}
